"""
BackToLife Database Service
Manages all local data storage using SQLite
"""
import sqlite3
import os
from datetime import datetime
from pathlib import Path


class Database:
    def __init__(self, db_path="backtolife_data.db"):
        """Initialize database connection"""
        # Store in user's home directory
        home = Path.home()
        self.db_dir = home / ".backtolife"
        self.db_dir.mkdir(exist_ok=True)
        self.db_path = self.db_dir / db_path
        self.conn = None
        self.cursor = None
        self.init_database()

    def connect(self):
        """Connect to database"""
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self.conn

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

    def init_database(self):
        """Initialize all database tables"""
        self.connect()

        # User profile table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_profile (
                id INTEGER PRIMARY KEY,
                created_date TEXT,
                current_level INTEGER DEFAULT 1,
                total_xp INTEGER DEFAULT 0,
                current_streak INTEGER DEFAULT 0,
                best_streak INTEGER DEFAULT 0,
                last_quest_date TEXT
            )
        ''')

        # Quest categories and master quest list
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS quests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                title TEXT,
                description TEXT,
                duration_minutes INTEGER,
                xp_value INTEGER,
                difficulty_level INTEGER,
                tier INTEGER,
                why_text TEXT,
                instructions TEXT
            )
        ''')

        # Completed quests history
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS quest_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quest_id INTEGER,
                completed_date TEXT,
                completion_time_seconds INTEGER,
                mood_before INTEGER,
                mood_after INTEGER,
                was_primary_quest BOOLEAN,
                xp_earned INTEGER,
                FOREIGN KEY (quest_id) REFERENCES quests(id)
            )
        ''')

        # Daily reflections
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reflections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                mood_rating INTEGER,
                what_worked TEXT,
                what_was_hard TEXT,
                grateful_for TEXT,
                energy_level INTEGER,
                relationship_stress INTEGER,
                notes TEXT
            )
        ''')

        # Life domain tracking
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS domain_tracking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                domain TEXT,
                metric_name TEXT,
                metric_value REAL,
                notes TEXT
            )
        ''')

        # Context engine data
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS context_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                time_of_day TEXT,
                day_of_week TEXT,
                parents_home BOOLEAN,
                mood_state TEXT,
                energy_level INTEGER,
                last_movement_minutes INTEGER
            )
        ''')

        # Shield mode activations
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS shield_activations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activation_time TEXT,
                duration_seconds INTEGER,
                trigger_reason TEXT,
                helpful_rating INTEGER
            )
        ''')

        # Achievements and milestones
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS achievements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                achievement_name TEXT,
                achievement_description TEXT,
                unlocked_date TEXT,
                category TEXT
            )
        ''')

        self.conn.commit()

        # Initialize user profile if not exists
        self.cursor.execute('SELECT COUNT(*) FROM user_profile')
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute('''
                INSERT INTO user_profile (id, created_date, current_level, total_xp)
                VALUES (1, ?, 1, 0)
            ''', (datetime.now().isoformat(),))
            self.conn.commit()

    def update_user_xp(self, xp_amount):
        """Add XP and check for level up"""
        profile = self.get_user_profile()
        new_xp = profile['xp'] + xp_amount
        new_level = self.calculate_level(new_xp)

        self.cursor.execute('''
            UPDATE user_profile
            SET total_xp = ?, current_level = ?
            WHERE id = 1
        ''', (new_xp, new_level))
        self.conn.commit()

        return new_level > profile['level']  # True if leveled up

    def calculate_level(self, xp):
        """Calculate level based on XP (100 XP per level)"""
        return (xp // 100) + 1

    def xp_for_next_level(self, current_xp):
        """Calculate XP needed for next level"""
        current_level = self.calculate_level(current_xp)
        next_level_xp = current_level * 100
        return next_level_xp - current_xp

    def complete_quest(self, quest_id, xp_earned, completion_time=0, was_primary=True):
        """Record quest completion"""
        today = datetime.now().date().isoformat()

        # Add to history
        self.cursor.execute('''
            INSERT INTO quest_history (
                quest_id, completed_date, completion_time_seconds,
                xp_earned, was_primary_quest
            )
            VALUES (?, ?, ?, ?, ?)
        ''', (quest_id, datetime.now().isoformat(), completion_time, xp_earned, was_primary))

        # Update XP
        leveled_up = self.update_user_xp(xp_earned)

        # Update streak
        profile = self.get_user_profile()
        last_date = profile['last_quest_date']

        if last_date:
            last_date_obj = datetime.fromisoformat(last_date).date()
            today_obj = datetime.now().date()
            days_diff = (today_obj - last_date_obj).days

            if days_diff == 1:
                # Consecutive day
                new_streak = profile['streak'] + 1
            elif days_diff == 0:
                # Same day
                new_streak = profile['streak']
            else:
                # Streak broken
                new_streak = 1
        else:
            new_streak = 1

        # Update streak and last quest date
        best_streak = max(profile['best_streak'], new_streak)
        self.cursor.execute('''
            UPDATE user_profile
            SET current_streak = ?, best_streak = ?, last_quest_date = ?
            WHERE id = 1
        ''', (new_streak, best_streak, today))

        self.conn.commit()
        return leveled_up

    def get_today_completed_quests(self):
        """Check if primary quest completed today"""
        today = datetime.now().date().isoformat()
        self.cursor.execute('''
            SELECT COUNT(*) FROM quest_history
            WHERE DATE(completed_date) = ? AND was_primary_quest = 1
        ''', (today,))
        return self.cursor.fetchone()[0] > 0

    def record_shield_activation(self, trigger_reason=""):
        """Record Shield Mode activation"""
        self.cursor.execute('''
            INSERT INTO shield_activations (activation_time, trigger_reason)
            VALUES (?, ?)
        ''', (datetime.now().isoformat(), trigger_reason))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_shield_duration(self, activation_id, duration_seconds, helpful_rating=0):
        """Update Shield Mode session with duration and rating"""
        self.cursor.execute('''
            UPDATE shield_activations
            SET duration_seconds = ?, helpful_rating = ?
            WHERE id = ?
        ''', (duration_seconds, helpful_rating, activation_id))
        self.conn.commit()

    def get_stats(self):
        """Get comprehensive statistics"""
        profile = self.get_user_profile()

        # Total quests completed
        self.cursor.execute('SELECT COUNT(*) FROM quest_history')
        total_quests = self.cursor.fetchone()[0]

        # Quests by category
        self.cursor.execute('''
            SELECT q.category, COUNT(*) as count
            FROM quest_history qh
            JOIN quests q ON qh.quest_id = q.id
            GROUP BY q.category
            ORDER BY count DESC
        ''')
        quests_by_category = self.cursor.fetchall()

        # This week's progress
        self.cursor.execute('''
            SELECT COUNT(*) FROM quest_history
            WHERE DATE(completed_date) >= DATE('now', '-7 days')
        ''')
        quests_this_week = self.cursor.fetchone()[0]

        return {
            'profile': profile,
            'total_quests': total_quests,
            'quests_by_category': quests_by_category,
            'quests_this_week': quests_this_week
        }

    def get_quest(self, quest_id):
        """Get quest by ID"""
        self.cursor.execute('SELECT * FROM quests WHERE id = ?', (quest_id,))
        return self.cursor.fetchone()

    def get_quest_history(self, limit=10):
        """Get recent quest completions with details"""
        self.cursor.execute('''
            SELECT
                qh.id,
                qh.quest_id,
                qh.completed_date as completed_at,
                qh.completion_time_seconds,
                qh.xp_earned,
                qh.was_primary_quest
            FROM quest_history qh
            ORDER BY qh.completed_date DESC
            LIMIT ?
        ''', (limit,))

        results = []
        for row in self.cursor.fetchall():
            results.append({
                'id': row[0],
                'quest_id': row[1],
                'completed_at': row[2],
                'completion_time': row[3],
                'xp_earned': row[4],
                'was_primary': row[5]
            })
        return results

    def get_user_profile(self):
        """Get current user profile data"""
        self.cursor.execute('SELECT COUNT(*) FROM quest_history')
        quests_completed = self.cursor.fetchone()[0]

        self.cursor.execute('SELECT * FROM user_profile WHERE id = 1')
        row = self.cursor.fetchone()
        if row:
            return {
                'level': row[2],
                'xp': row[3],
                'streak': row[4],
                'best_streak': row[5],
                'last_quest_date': row[6],
                'quests_completed': quests_completed
            }
        return None

    def get_best_streak(self):
        """Get best streak"""
        profile = self.get_user_profile()
        return profile['best_streak'] if profile else 0

    def get_domain_stats(self, domain):
        """Get stats for specific domain"""
        # Get total quests in domain
        self.cursor.execute('''
            SELECT COUNT(*) FROM quests WHERE category = ?
        ''', (domain,))
        total = self.cursor.fetchone()[0]

        # Get completed quests in domain
        self.cursor.execute('''
            SELECT COUNT(DISTINCT qh.quest_id)
            FROM quest_history qh
            JOIN quests q ON qh.quest_id = q.id
            WHERE q.category = ?
        ''', (domain,))
        completed = self.cursor.fetchone()[0]

        return {
            'total': total,
            'completed': completed
        }

    def save_reflection(self, date, mood, energy_level, sleep_quality, gratitude, notes=None):
        """Save daily reflection (updated signature)"""
        self.cursor.execute('''
            INSERT INTO reflections (
                date, mood_rating, energy_level, grateful_for, notes
            )
            VALUES (?, ?, ?, ?, ?)
        ''', (date, mood, energy_level, gratitude, notes))
        self.conn.commit()

    def get_reflection_by_date(self, date):
        """Get reflection for specific date"""
        self.cursor.execute('''
            SELECT * FROM reflections WHERE date = ?
        ''', (date,))
        row = self.cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'date': row[1],
                'mood': row[2] if isinstance(row[2], str) else 'okay',
                'energy_level': row[5] if len(row) > 5 else 5,
                'sleep_quality': 'okay',  # Default for now
                'gratitude': row[4] if len(row) > 4 else '',
                'notes': row[7] if len(row) > 7 else ''
            }
        return None

    def get_reflection_history(self, limit=7):
        """Get recent reflections"""
        self.cursor.execute('''
            SELECT * FROM reflections
            ORDER BY date DESC
            LIMIT ?
        ''', (limit,))

        results = []
        for row in self.cursor.fetchall():
            results.append({
                'id': row[0],
                'date': row[1],
                'mood': row[2] if isinstance(row[2], str) else 'okay',
                'energy_level': row[5] if len(row) > 5 else 5,
                'sleep_quality': 'okay',  # Default
                'gratitude': row[4] if len(row) > 4 else '',
                'notes': row[7] if len(row) > 7 else ''
            })
        return results

    def log_shield_activation(self):
        """Log shield mode activation"""
        return self.record_shield_activation()

    def clear_all_data(self):
        """Clear all user data (DANGEROUS!)"""
        # Clear all tables
        self.cursor.execute('DELETE FROM quest_history')
        self.cursor.execute('DELETE FROM reflections')
        self.cursor.execute('DELETE FROM domain_tracking')
        self.cursor.execute('DELETE FROM context_data')
        self.cursor.execute('DELETE FROM shield_activations')
        self.cursor.execute('DELETE FROM achievements')

        # Reset user profile
        self.cursor.execute('''
            UPDATE user_profile
            SET current_level = 1,
                total_xp = 0,
                current_streak = 0,
                best_streak = 0,
                last_quest_date = NULL
            WHERE id = 1
        ''')

        self.conn.commit()
