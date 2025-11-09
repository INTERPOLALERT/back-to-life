"""
Progress Tab - Stats and Analytics
Comprehensive progress tracking and insights
"""
import customtkinter as ctk
from datetime import datetime, timedelta


class ProgressTab(ctk.CTkFrame):
    """
    Progress tracking with:
    - Overall stats
    - Domain breakdown
    - Streaks and achievements
    - Visual progress graphs
    - Pattern insights
    """

    def __init__(self, parent, db, audio):
        super().__init__(parent, fg_color="transparent")

        self.db = db
        self.audio = audio

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.setup_ui()

    def setup_ui(self):
        """Build progress UI"""
        # Scrollable main area
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=0, column=0, sticky="nsew")
        scroll.grid_columnconfigure(0, weight=1)

        # Header
        header = ctk.CTkFrame(scroll, fg_color="#1a1a1a", corner_radius=15)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header,
            text="📊 Your Progress",
            font=("Arial", 28, "bold"),
            text_color="#00AAFF"
        ).pack(pady=(20, 5))

        profile = self.db.get_user_profile()

        ctk.CTkLabel(
            header,
            text=f"Level {profile['level']} • {profile['quests_completed']} Quests Completed",
            font=("Arial", 14),
            text_color="#888888"
        ).pack(pady=(0, 20))

        # Main stats grid
        self.show_main_stats(scroll, profile)

        # Domain breakdown
        self.show_domain_breakdown(scroll)

        # Streaks and achievements
        self.show_achievements(scroll, profile)

        # Recent activity
        self.show_recent_activity(scroll)

        # Insights
        self.show_insights(scroll)

    def show_main_stats(self, parent, profile):
        """Display main statistics"""
        stats_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        stats_section.grid(row=1, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            stats_section,
            text="Overview",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 15))

        # Stats grid
        stats_grid = ctk.CTkFrame(stats_section, fg_color="transparent")
        stats_grid.pack(pady=(0, 20), padx=20)

        stats = [
            ("Total XP", profile['xp'], "⭐", "#FFD700"),
            ("Current Level", profile['level'], "🎯", "#00AAFF"),
            ("Quest Streak", f"{profile['streak']} days", "🔥", "#FF6600"),
            ("Quests Done", profile['quests_completed'], "✅", "#00AA00"),
            ("This Week", self.get_week_count(), "📅", "#00AAFF"),
            ("This Month", self.get_month_count(), "📆", "#00AAFF")
        ]

        for i, (label, value, icon, color) in enumerate(stats):
            stat_card = ctk.CTkFrame(stats_grid, fg_color="#2a2a2a", corner_radius=10)
            stat_card.grid(row=i // 3, column=i % 3, padx=10, pady=10, sticky="nsew")

            ctk.CTkLabel(
                stat_card,
                text=icon,
                font=("Arial", 28)
            ).pack(pady=(15, 5), padx=40)

            ctk.CTkLabel(
                stat_card,
                text=str(value),
                font=("Arial", 24, "bold"),
                text_color=color
            ).pack(pady=0, padx=40)

            ctk.CTkLabel(
                stat_card,
                text=label,
                font=("Arial", 12),
                text_color="#888888"
            ).pack(pady=(0, 15), padx=40)

        # XP Progress to next level
        progress_frame = ctk.CTkFrame(stats_section, fg_color="#2a2a2a", corner_radius=10)
        progress_frame.pack(fill="x", padx=20, pady=(10, 20))

        next_level_xp = profile['level'] * 100
        progress_value = min(1.0, profile['xp'] / next_level_xp)

        ctk.CTkLabel(
            progress_frame,
            text=f"Progress to Level {profile['level'] + 1}",
            font=("Arial", 15, "bold")
        ).pack(pady=(15, 5))

        progress_bar = ctk.CTkProgressBar(
            progress_frame,
            width=600,
            height=20
        )
        progress_bar.set(progress_value)
        progress_bar.pack(pady=10)

        ctk.CTkLabel(
            progress_frame,
            text=f"{profile['xp']} / {next_level_xp} XP",
            font=("Arial", 13),
            text_color="#888888"
        ).pack(pady=(0, 15))

    def show_domain_breakdown(self, parent):
        """Show progress by domain"""
        domain_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        domain_section.grid(row=2, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            domain_section,
            text="Progress by Life Domain",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 15))

        # Get domain stats
        domains = [
            ("BODY_RECOVERY", "💪", "Physical Recovery"),
            ("BASIC_FUNCTION", "🧠", "Basic Function"),
            ("RELATIONSHIP", "❤️", "Relationship"),
            ("ACADEMIC", "📚", "Academic"),
            ("EMOTIONAL", "😊", "Emotional"),
            ("SOCIAL", "👥", "Social"),
            ("EXECUTIVE", "⚙️", "Executive Function"),
            ("CREATIVE", "🎨", "Creative"),
            ("PROFESSIONAL", "💼", "Professional"),
            ("LONG_TERM", "🎯", "Long-term Goals")
        ]

        for domain_id, icon, domain_name in domains:
            domain_card = ctk.CTkFrame(domain_section, fg_color="#2a2a2a", corner_radius=8)
            domain_card.pack(fill="x", padx=20, pady=5)

            # Header
            header_frame = ctk.CTkFrame(domain_card, fg_color="transparent")
            header_frame.pack(fill="x", padx=15, pady=10)

            ctk.CTkLabel(
                header_frame,
                text=f"{icon} {domain_name}",
                font=("Arial", 15, "bold")
            ).pack(side="left")

            # Get domain stats from database
            domain_stats = self.db.get_domain_stats(domain_id)
            completed = domain_stats.get('completed', 0)
            total = domain_stats.get('total', 0)

            if total > 0:
                percentage = int((completed / total) * 100)
                progress_value = completed / total
            else:
                percentage = 0
                progress_value = 0

            ctk.CTkLabel(
                header_frame,
                text=f"{completed}/{total} ({percentage}%)",
                font=("Arial", 13),
                text_color="#888888"
            ).pack(side="right")

            # Progress bar
            progress_bar = ctk.CTkProgressBar(
                domain_card,
                width=650,
                height=12
            )
            progress_bar.set(progress_value)
            progress_bar.pack(padx=15, pady=(0, 10))

    def show_achievements(self, parent, profile):
        """Show achievements and streaks"""
        achievements_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        achievements_section.grid(row=3, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            achievements_section,
            text="Achievements & Milestones",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 15))

        # Achievement cards
        achievements = [
            {
                'icon': '🏆',
                'title': 'First Quest',
                'description': 'Completed your first quest',
                'unlocked': profile['quests_completed'] >= 1
            },
            {
                'icon': '🔥',
                'title': '7-Day Streak',
                'description': 'Maintained streak for a week',
                'unlocked': profile['streak'] >= 7
            },
            {
                'icon': '⭐',
                'title': 'Level 5',
                'description': 'Reached level 5',
                'unlocked': profile['level'] >= 5
            },
            {
                'icon': '💪',
                'title': 'Body Recovery Started',
                'description': 'Completed first physical quest',
                'unlocked': True  # TODO: Check domain completion
            },
            {
                'icon': '📚',
                'title': 'Knowledge Seeker',
                'description': 'Completed 10 flashcard reviews',
                'unlocked': False  # TODO: Check flashcard stats
            },
            {
                'icon': '🎯',
                'title': 'Consistent Warrior',
                'description': 'Completed quests 30 days in a row',
                'unlocked': profile['streak'] >= 30
            }
        ]

        achievements_grid = ctk.CTkFrame(achievements_section, fg_color="transparent")
        achievements_grid.pack(pady=(0, 20), padx=20)

        for i, achievement in enumerate(achievements):
            card = ctk.CTkFrame(
                achievements_grid,
                fg_color="#2a2a2a" if achievement['unlocked'] else "#1a1a1a",
                corner_radius=10
            )
            card.grid(row=i // 3, column=i % 3, padx=10, pady=10, sticky="nsew")

            # Icon (grayscale if locked)
            icon_label = ctk.CTkLabel(
                card,
                text=achievement['icon'],
                font=("Arial", 32)
            )
            icon_label.pack(pady=(15, 5), padx=30)
            if not achievement['unlocked']:
                icon_label.configure(text_color="#444444")

            ctk.CTkLabel(
                card,
                text=achievement['title'],
                font=("Arial", 14, "bold"),
                text_color="#FFD700" if achievement['unlocked'] else "#666666"
            ).pack(pady=0, padx=30)

            ctk.CTkLabel(
                card,
                text=achievement['description'],
                font=("Arial", 11),
                text_color="#AAAAAA" if achievement['unlocked'] else "#444444",
                wraplength=150
            ).pack(pady=(5, 15), padx=30)

            if achievement['unlocked']:
                ctk.CTkLabel(
                    card,
                    text="✓ UNLOCKED",
                    font=("Arial", 10, "bold"),
                    text_color="#00AA00"
                ).pack(pady=(0, 10))
            else:
                ctk.CTkLabel(
                    card,
                    text="🔒 Locked",
                    font=("Arial", 10),
                    text_color="#666666"
                ).pack(pady=(0, 10))

    def show_recent_activity(self, parent):
        """Show recent quest completions"""
        activity_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        activity_section.grid(row=4, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            activity_section,
            text="Recent Activity",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 15))

        # Get recent quest history
        history = self.db.get_quest_history(limit=10)

        if history:
            for entry in history:
                activity_card = ctk.CTkFrame(activity_section, fg_color="#2a2a2a", corner_radius=8)
                activity_card.pack(fill="x", padx=20, pady=5)

                # Quest info
                quest = self.db.get_quest(entry['quest_id'])
                if quest:
                    info_frame = ctk.CTkFrame(activity_card, fg_color="transparent")
                    info_frame.pack(fill="x", padx=15, pady=12)

                    ctk.CTkLabel(
                        info_frame,
                        text="✅",
                        font=("Arial", 18)
                    ).pack(side="left", padx=(0, 10))

                    text_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
                    text_frame.pack(side="left", fill="x", expand=True)

                    ctk.CTkLabel(
                        text_frame,
                        text=quest[2],  # title
                        font=("Arial", 14, "bold"),
                        anchor="w"
                    ).pack(anchor="w")

                    # Format timestamp
                    time_ago = self.format_time_ago(entry['completed_at'])
                    ctk.CTkLabel(
                        text_frame,
                        text=f"{time_ago} • +{entry['xp_earned']} XP",
                        font=("Arial", 11),
                        text_color="#888888",
                        anchor="w"
                    ).pack(anchor="w")
        else:
            ctk.CTkLabel(
                activity_section,
                text="No activity yet. Complete your first quest!",
                font=("Arial", 13),
                text_color="#888888"
            ).pack(pady=(0, 20))

    def show_insights(self, parent):
        """Show pattern insights"""
        insights_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        insights_section.grid(row=5, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            insights_section,
            text="Pattern Insights",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 15))

        # Sample insights (would come from context engine)
        insights = [
            {
                'icon': '📈',
                'title': 'Completion Patterns',
                'message': 'You complete more quests in the morning (65% vs 35% afternoon/evening)',
                'color': '#00AAFF'
            },
            {
                'icon': '💪',
                'title': 'Strongest Domain',
                'message': 'Physical Recovery is your most consistent domain with 80% completion rate',
                'color': '#00AA00'
            },
            {
                'icon': '🔥',
                'title': 'Best Streak',
                'message': f"Your best streak was {self.db.get_best_streak()} days. Current: {self.db.get_user_profile()['streak']} days",
                'color': '#FF6600'
            }
        ]

        for insight in insights:
            card = ctk.CTkFrame(insights_section, fg_color="#2a2a2a", corner_radius=10)
            card.pack(fill="x", padx=20, pady=8)

            header = ctk.CTkFrame(card, fg_color="transparent")
            header.pack(fill="x", padx=15, pady=12)

            ctk.CTkLabel(
                header,
                text=insight['icon'],
                font=("Arial", 20)
            ).pack(side="left", padx=(0, 10))

            text_frame = ctk.CTkFrame(header, fg_color="transparent")
            text_frame.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(
                text_frame,
                text=insight['title'],
                font=("Arial", 14, "bold"),
                text_color=insight['color'],
                anchor="w"
            ).pack(anchor="w")

            ctk.CTkLabel(
                text_frame,
                text=insight['message'],
                font=("Arial", 12),
                text_color="#CCCCCC",
                wraplength=600,
                justify="left",
                anchor="w"
            ).pack(anchor="w")

    def get_week_count(self):
        """Get quests completed this week"""
        # TODO: Implement actual query
        return 5

    def get_month_count(self):
        """Get quests completed this month"""
        # TODO: Implement actual query
        return 18

    def format_time_ago(self, timestamp):
        """Format timestamp as relative time"""
        try:
            if isinstance(timestamp, str):
                completed_time = datetime.fromisoformat(timestamp)
            else:
                completed_time = timestamp

            now = datetime.now()
            delta = now - completed_time

            if delta.days > 0:
                return f"{delta.days} day{'s' if delta.days != 1 else ''} ago"
            elif delta.seconds >= 3600:
                hours = delta.seconds // 3600
                return f"{hours} hour{'s' if hours != 1 else ''} ago"
            elif delta.seconds >= 60:
                minutes = delta.seconds // 60
                return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
            else:
                return "Just now"
        except:
            return "Recently"
