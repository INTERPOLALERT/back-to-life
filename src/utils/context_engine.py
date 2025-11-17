"""
BackToLife Context Engine
Intelligently selects daily quests based on user patterns and current state
"Knows you more than you know yourself"
"""
import random
from datetime import datetime, timedelta
from src.data.quest_database import get_quests_by_category, get_random_quest_by_difficulty


class ContextEngine:
    def __init__(self, db):
        self.db = db

    def select_daily_quest(self):
        """
        Main quest selection algorithm
        Analyzes user state and selects the most appropriate quest
        Returns dict with 'quest' and 'reason' keys
        """
        # Get current context
        time_of_day = self.get_time_of_day()
        day_of_week = datetime.now().strftime('%A')
        user_profile = self.db.get_user_profile()

        # Get recent history
        quest_history = self.get_recent_quest_counts()
        last_reflection = self.get_last_reflection()

        # Determine priority domain
        priority_domain = self.determine_priority_domain(
            quest_history, last_reflection, user_profile
        )

        # Calculate appropriate difficulty
        difficulty = self.calculate_difficulty(user_profile, last_reflection)

        # Select specific quest
        quest = self.select_quest_from_domain(
            priority_domain, difficulty, time_of_day
        )

        # Generate reason for this quest selection
        reason = self._generate_quest_reason(
            priority_domain, difficulty, time_of_day, user_profile, last_reflection
        )

        return {
            'quest': quest,
            'reason': reason
        }

    def get_time_of_day(self):
        """Categorize current time"""
        hour = datetime.now().hour
        if 5 <= hour < 12:
            return 'morning'
        elif 12 <= hour < 17:
            return 'afternoon'
        elif 17 <= hour < 22:
            return 'evening'
        else:
            return 'night'

    def get_recent_quest_counts(self):
        """Count quests by category in last 7 days"""
        self.db.cursor.execute('''
            SELECT q.category, COUNT(*) as count
            FROM quest_history qh
            JOIN quests q ON qh.quest_id = q.id
            WHERE DATE(qh.completed_date) >= DATE('now', '-7 days')
            GROUP BY q.category
        ''')
        results = self.db.cursor.fetchall()
        return {row[0]: row[1] for row in results}

    def get_last_reflection(self):
        """Get most recent reflection data"""
        self.db.cursor.execute('''
            SELECT * FROM reflections
            ORDER BY date DESC
            LIMIT 1
        ''')
        row = self.db.cursor.fetchone()
        if row:
            return {
                'date': row[1],
                'mood_rating': row[2],
                'energy_level': row[5],
                'relationship_stress': row[6]
            }
        return None

    def determine_priority_domain(self, quest_history, last_reflection, profile):
        """
        Determine which domain needs attention most
        This is the core intelligence of the app
        """
        # Priority rules based on patterns

        # 1. Check for neglected domains (not done in 3+ days)
        all_categories = [
            'BODY_RECOVERY', 'HYGIENE', 'EATING_DRINKING',
            'ORGANIZATION', 'SOCIAL_RECOVERY', 'FINANCIAL',
            'ACADEMIC', 'CREATIVE', 'CRYPTO_AI', 'FORTNITE'
        ]

        neglected_domains = []
        for category in all_categories:
            if quest_history.get(category, 0) == 0:
                neglected_domains.append(category)

        # 2. Body recovery is highest priority if not done recently
        if 'BODY_RECOVERY' in neglected_domains:
            return 'BODY_RECOVERY'

        # 3. Hygiene if not done in 2+ days
        if 'HYGIENE' in neglected_domains:
            return 'HYGIENE'

        # 4. Check mood/energy from reflection
        if last_reflection:
            energy = last_reflection.get('energy_level', 5)
            relationship_stress = last_reflection.get('relationship_stress', 5)

            # Low energy = simple body or hygiene quest
            if energy <= 3:
                return random.choice(['BODY_RECOVERY', 'EATING_DRINKING'])

            # High relationship stress = boundary or self-care quest
            if relationship_stress >= 7:
                return random.choice(['FINANCIAL', 'CREATIVE', 'SOCIAL_RECOVERY'])

        # 5. Balance check - find least done category
        if quest_history:
            least_done = min(quest_history, key=quest_history.get)
            return least_done

        # 6. Default to body recovery for beginners
        return 'BODY_RECOVERY'

    def calculate_difficulty(self, profile, last_reflection):
        """
        Calculate appropriate difficulty level (1-5)
        Based on streak, level, and current state
        """
        base_difficulty = 1

        # Adjust based on level (every 5 levels, increase difficulty)
        level_modifier = min(profile['level'] // 5, 2)
        base_difficulty += level_modifier

        # Adjust based on streak (good streak = can handle more)
        if profile['streak'] >= 7:
            base_difficulty += 1
        elif profile['streak'] >= 14:
            base_difficulty += 2

        # Reduce difficulty if low energy/mood
        if last_reflection:
            energy = last_reflection.get('energy_level', 5)
            if energy <= 3:
                base_difficulty = max(1, base_difficulty - 1)

        # Cap at 5
        return min(base_difficulty, 5)

    def select_quest_from_domain(self, category, difficulty, time_of_day):
        """
        Select specific quest from chosen domain
        Considers time of day and difficulty
        """
        # Time-specific adjustments
        if time_of_day == 'morning':
            # Morning quests should be gentle
            difficulty = max(1, difficulty - 1)
            # Favor body, hydration, hygiene in morning
            if category not in ['BODY_RECOVERY', 'EATING_DRINKING', 'HYGIENE']:
                if random.random() < 0.3:  # 30% chance to override
                    category = random.choice(['BODY_RECOVERY', 'EATING_DRINKING'])

        elif time_of_day == 'night':
            # Night is good for reflection, organization, creative work
            if category in ['SOCIAL_RECOVERY']:  # Avoid social quests at night
                category = random.choice(['ORGANIZATION', 'CREATIVE', 'ACADEMIC'])

        # Get quest from database
        quest = get_random_quest_by_difficulty(self.db, category, difficulty)

        # If no quest found (shouldn't happen), get any easy quest
        if not quest:
            quest = get_random_quest_by_difficulty(self.db, 'BODY_RECOVERY', 1)

        return quest

    def select_bonus_quests(self, primary_quest, count=3):
        """
        Select optional bonus quests for the day
        Should be from different categories than primary
        """
        primary_category = primary_quest[1]  # category is index 1

        bonus_quests = []
        categories_to_try = [
            'EATING_DRINKING', 'HYGIENE', 'ORGANIZATION',
            'CREATIVE', 'BODY_RECOVERY', 'CRYPTO_AI', 'FORTNITE'
        ]

        # Remove primary category
        categories_to_try = [c for c in categories_to_try if c != primary_category]

        # Get one quest from each category
        for category in categories_to_try[:count]:
            quest = get_random_quest_by_difficulty(self.db, category, 2)
            if quest:
                bonus_quests.append(quest)

        return bonus_quests[:count]

    def should_show_shield_mode_reminder(self):
        """
        Determine if Shield Mode reminder should be shown
        Based on patterns of stress
        """
        # Check recent shield activations
        self.db.cursor.execute('''
            SELECT COUNT(*) FROM shield_activations
            WHERE DATE(activation_time) = DATE('now')
        ''')
        today_activations = self.db.cursor.fetchone()[0]

        # Check last reflection for high stress
        reflection = self.get_last_reflection()
        if reflection and reflection.get('relationship_stress', 0) >= 8:
            return True

        # If already used shield today, don't remind
        if today_activations > 0:
            return False

        return False

    def get_champion_message(self, user_profile):
        """
        Generate personalized champion message based on progress
        """
        level = user_profile['level']
        streak = user_profile['streak']

        if streak == 0:
            return "Every champion starts somewhere. Today is your day."
        elif streak == 1:
            return "You're back. The champion is waking up."
        elif streak < 7:
            return f"Day {streak}. You're building momentum."
        elif streak < 14:
            return f"{streak} days strong. The champion is remembering."
        elif streak < 30:
            return f"{streak} days. You're not the same person who started."
        elif streak < 60:
            return f"{streak} days! The world better get ready."
        else:
            return f"{streak} days of greatness. The legend continues."

    def adapt_quest_on_failure(self, quest_id):
        """
        If user fails a quest, select an easier version next time
        This ensures quests stay in "impossible to fail" range
        """
        quest = self.db.cursor.execute(
            'SELECT * FROM quests WHERE id = ?', (quest_id,)
        ).fetchone()

        if not quest:
            return None

        category = quest[1]
        current_difficulty = quest[5]

        # Get easier quest from same category
        new_difficulty = max(1, current_difficulty - 1)
        easier_quest = get_random_quest_by_difficulty(
            self.db, category, new_difficulty
        )

        return easier_quest

    def get_context_aware_why_message(self, quest, time_of_day):
        """
        Enhance the quest's why message with context-aware details
        """
        # Quest tuple structure: id, category, title, description, duration, xp, difficulty, tier, why_text, instructions
        base_why = quest[8] if len(quest) > 8 else "You can do this."  # why_text is index 8

        # Add time-specific context
        if time_of_day == 'morning':
            return f"☀️ Morning: {base_why}"
        elif time_of_day == 'evening':
            return f"🌙 Evening: {base_why}"

        return base_why

    def _generate_quest_reason(self, priority_domain, difficulty, time_of_day, user_profile, last_reflection):
        """Generate human-readable reason for quest selection"""
        reasons = []

        # Domain-specific reasons
        domain_reasons = {
            'BODY_RECOVERY': "Your body needs gentle movement to rebuild strength",
            'HYGIENE': "Self-care builds self-respect, one small step at a time",
            'EATING_DRINKING': "Nourishing your body is the foundation of recovery",
            'ORGANIZATION': "A clear space helps clear your mind",
            'SOCIAL_RECOVERY': "Reconnecting with others, at your own pace",
            'FINANCIAL': "Financial stability reduces stress and builds confidence",
            'ACADEMIC': "Your education matters, even in tiny steps",
            'CREATIVE': "Creativity is how your soul breathes",
            'CRYPTO_AI': "Engaging your interests in a balanced way",
            'FORTNITE': "Gaming as a tool for skill-building and joy"
        }

        reason = domain_reasons.get(priority_domain, "This quest is selected to help you move forward")

        # Add context based on why this domain was chosen
        if last_reflection:
            energy = last_reflection.get('energy_level', 5)
            if energy <= 3:
                reason += ". Your energy is low, so we're keeping it gentle."
            elif energy >= 7:
                reason += ". You have good energy today - let's use it wisely."

        # Add time context
        if time_of_day == 'morning':
            reason += " Perfect for starting your day."
        elif time_of_day == 'evening':
            reason += " A good way to wind down your day."

        # Add streak encouragement
        streak = user_profile.get('streak', 0)
        if streak > 0:
            reason += f" You're {streak} days strong!"

        return reason

    def get_pattern_insights(self):
        """
        Analyze user patterns and return insights
        Returns list of insight dicts with 'title' and 'message'
        """
        insights = []
        user_profile = self.db.get_user_profile()

        # Insight 1: Completion patterns by time
        self.db.cursor.execute('''
            SELECT
                CASE
                    WHEN CAST(strftime('%H', completed_date) AS INTEGER) < 12 THEN 'Morning'
                    WHEN CAST(strftime('%H', completed_date) AS INTEGER) < 17 THEN 'Afternoon'
                    ELSE 'Evening'
                END as time_period,
                COUNT(*) as count
            FROM quest_history
            WHERE DATE(completed_date) >= DATE('now', '-30 days')
            GROUP BY time_period
            ORDER BY count DESC
        ''')
        time_results = self.db.cursor.fetchall()

        if time_results and len(time_results) > 0:
            best_time = time_results[0][0]
            best_count = time_results[0][1]
            total = sum(r[1] for r in time_results)
            if total > 0:
                percentage = int((best_count / total) * 100)
                insights.append({
                    'title': 'Best Time of Day',
                    'message': f"You complete {percentage}% of your quests in the {best_time.lower()}. That's your power time!"
                })

        # Insight 2: Domain strengths
        self.db.cursor.execute('''
            SELECT q.category, COUNT(*) as count
            FROM quest_history qh
            JOIN quests q ON qh.quest_id = q.id
            WHERE DATE(qh.completed_date) >= DATE('now', '-30 days')
            GROUP BY q.category
            ORDER BY count DESC
            LIMIT 1
        ''')
        domain_result = self.db.cursor.fetchone()

        if domain_result:
            top_domain = domain_result[0].replace('_', ' ').title()
            count = domain_result[1]
            insights.append({
                'title': 'Strongest Domain',
                'message': f"{top_domain} is your most consistent area with {count} completed quests this month."
            })

        # Insight 3: Streak achievement
        best_streak = user_profile.get('best_streak', 0)
        current_streak = user_profile.get('streak', 0)

        if best_streak > 0:
            if current_streak == best_streak:
                insights.append({
                    'title': 'Record Streak!',
                    'message': f"You're at your all-time best: {best_streak} days in a row. Legendary! 🏆"
                })
            else:
                insights.append({
                    'title': 'Previous Best',
                    'message': f"Your best streak was {best_streak} days. You've proven you can do it again."
                })

        # Insight 4: Progress velocity
        quests_completed = user_profile.get('quests_completed', 0)
        if quests_completed >= 10:
            insights.append({
                'title': 'Total Progress',
                'message': f"You've completed {quests_completed} quests total. Each one is proof you're rebuilding."
            })

        # If no insights, add encouragement
        if not insights:
            insights.append({
                'title': 'Just Getting Started',
                'message': "Complete more quests to unlock pattern insights about your progress!"
            })

        return insights
