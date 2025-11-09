"""
BackToLife Progress Screen
View stats, achievements, and progress
"""
import customtkinter as ctk


class ProgressScreen(ctk.CTkFrame):
    def __init__(self, parent, db, on_back):
        super().__init__(parent, corner_radius=0)

        self.db = db
        self.on_back = on_back

        self.grid_columnconfigure(0, weight=1)
        self.setup_ui()

    def setup_ui(self):
        """Build progress screen UI"""
        # Header
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        header_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkButton(
            header_frame,
            text="← Back",
            command=self.on_back,
            width=100,
            height=40
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(
            header_frame,
            text="📊 Your Progress",
            font=("Arial", 32, "bold")
        ).grid(row=0, column=1, padx=20)

        # Get statistics
        stats = self.db.get_stats()
        profile = stats['profile']

        # Main stats cards
        stats_container = ctk.CTkFrame(self, fg_color="transparent")
        stats_container.grid(row=1, column=0, sticky="ew", pady=20)
        stats_container.grid_columnconfigure((0, 1, 2), weight=1)

        # Level card
        level_card = self.create_stat_card(
            stats_container,
            "🏆 Level",
            str(profile['level']),
            f"{profile['xp']} XP total"
        )
        level_card.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Streak card
        streak_card = self.create_stat_card(
            stats_container,
            "🔥 Current Streak",
            f"{profile['streak']} days",
            f"Best: {profile['best_streak']} days"
        )
        streak_card.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Total quests card
        total_card = self.create_stat_card(
            stats_container,
            "✅ Total Quests",
            str(stats['total_quests']),
            f"{stats['quests_this_week']} this week"
        )
        total_card.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        # XP Progress bar
        xp_progress_frame = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=10)
        xp_progress_frame.grid(row=2, column=0, sticky="ew", pady=20, ipady=20)

        ctk.CTkLabel(
            xp_progress_frame,
            text="Progress to Next Level",
            font=("Arial", 16, "bold")
        ).pack(pady=(10, 5))

        # Calculate progress
        current_xp = profile['xp']
        xp_for_next = self.db.xp_for_next_level(current_xp)
        level_base_xp = (profile['level'] - 1) * 100
        progress_in_level = current_xp - level_base_xp
        progress_percent = progress_in_level / 100

        # Progress bar
        progress_bar = ctk.CTkProgressBar(
            xp_progress_frame,
            width=600,
            height=30
        )
        progress_bar.set(progress_percent)
        progress_bar.pack(pady=10)

        ctk.CTkLabel(
            xp_progress_frame,
            text=f"{progress_in_level}/100 XP  •  {xp_for_next} XP to Level {profile['level'] + 1}",
            font=("Arial", 14),
            text_color="#888888"
        ).pack(pady=(5, 10))

        # Quest breakdown by category
        category_frame = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=10)
        category_frame.grid(row=3, column=0, sticky="ew", pady=20)

        ctk.CTkLabel(
            category_frame,
            text="Quests by Category",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 10))

        # List categories
        categories = stats['quests_by_category']
        if categories:
            for category, count in categories[:8]:  # Top 8 categories
                category_item = ctk.CTkFrame(category_frame, fg_color="#2a2a2a", corner_radius=5)
                category_item.pack(fill="x", padx=20, pady=5)

                category_name = category.replace('_', ' ').title()
                ctk.CTkLabel(
                    category_item,
                    text=f"{category_name}: {count} quests",
                    font=("Arial", 14),
                    anchor="w"
                ).pack(side="left", padx=15, pady=10)

        else:
            ctk.CTkLabel(
                category_frame,
                text="Complete your first quest to see stats here!",
                font=("Arial", 14),
                text_color="#888888"
            ).pack(pady=20)

        # Motivational message
        if profile['level'] >= 10:
            message = "You're a legend in the making."
        elif profile['level'] >= 5:
            message = "The champion is waking up."
        elif stats['total_quests'] >= 1:
            message = "Every journey begins with a single step."
        else:
            message = "Your journey starts today."

        ctk.CTkLabel(
            self,
            text=message,
            font=("Arial", 16, "italic"),
            text_color="#888888"
        ).grid(row=4, column=0, pady=30)

    def create_stat_card(self, parent, title, value, subtitle):
        """Create a stat display card"""
        card = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=10)

        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 14),
            text_color="#888888"
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 32, "bold")
        ).pack(pady=5)

        ctk.CTkLabel(
            card,
            text=subtitle,
            font=("Arial", 12),
            text_color="#888888"
        ).pack(pady=(5, 15))

        return card
