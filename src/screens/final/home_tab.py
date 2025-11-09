"""
Home Tab - Enhanced Daily Quest Display
Shows personalized daily quest with pattern insights
"""
import customtkinter as ctk
from src.screens.enhanced_quest_screen import EnhancedQuestScreen


class HomeTab(ctk.CTkFrame):
    """
    Home tab showing:
    - Daily personalized quest
    - Pattern insights
    - Quick stats
    - Motivational message
    """

    def __init__(self, parent, db, context_engine, audio):
        super().__init__(parent, fg_color="transparent")

        self.db = db
        self.context_engine = context_engine
        self.audio = audio

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.setup_ui()

    def setup_ui(self):
        """Build home UI"""
        # Header section
        header = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=15)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        profile = self.db.get_user_profile()

        # Welcome message
        ctk.CTkLabel(
            header,
            text=f"Welcome back, Champion! 🏆",
            font=("Arial", 28, "bold"),
            text_color="#FFD700"
        ).pack(pady=(20, 5))

        # Champion message (context-aware)
        champion_msg = self.context_engine.get_champion_message(profile)
        ctk.CTkLabel(
            header,
            text=champion_msg,
            font=("Arial", 14),
            text_color="#00AAFF",
            wraplength=600
        ).pack(pady=(0, 15))

        # Stats row
        stats_frame = ctk.CTkFrame(header, fg_color="transparent")
        stats_frame.pack(pady=(10, 20))

        stats = [
            (f"Level {profile['level']}", "🎯"),
            (f"{profile['xp']} XP", "⭐"),
            (f"{profile['streak']} Day Streak", "🔥"),
            (f"{profile['quests_completed']} Quests", "✅")
        ]

        for i, (text, icon) in enumerate(stats):
            stat_box = ctk.CTkFrame(stats_frame, fg_color="#2a2a2a", corner_radius=8)
            stat_box.grid(row=0, column=i, padx=10, pady=5)

            ctk.CTkLabel(
                stat_box,
                text=icon,
                font=("Arial", 20)
            ).pack(pady=(10, 0), padx=20)

            ctk.CTkLabel(
                stat_box,
                text=text,
                font=("Arial", 12, "bold")
            ).pack(pady=(0, 10), padx=20)

        # Main content area (scrollable)
        main_scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        main_scroll.grid(row=1, column=0, sticky="nsew")
        main_scroll.grid_columnconfigure(0, weight=1)

        # Today's Quest section
        self.show_daily_quest(main_scroll)

        # Pattern Insights
        self.show_pattern_insights(main_scroll)

        # Quick Actions
        self.show_quick_actions(main_scroll)

    def show_daily_quest(self, parent):
        """Display today's personalized quest"""
        quest_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        quest_section.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            quest_section,
            text="📋 Today's Quest",
            font=("Arial", 24, "bold"),
            text_color="#00AAFF"
        ).pack(pady=(20, 10))

        # Get daily quest
        quest_data = self.context_engine.select_daily_quest()
        quest = quest_data['quest']

        # Quest card
        quest_card = ctk.CTkFrame(quest_section, fg_color="#2a2a2a", corner_radius=12)
        quest_card.pack(fill="x", padx=20, pady=(10, 20))

        # Quest title
        ctk.CTkLabel(
            quest_card,
            text=quest[2],  # title
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 5), padx=20)

        # Quest description
        ctk.CTkLabel(
            quest_card,
            text=quest[3],  # description
            font=("Arial", 14),
            text_color="#AAAAAA",
            wraplength=500
        ).pack(pady=(0, 10), padx=20)

        # Quest details row
        details_frame = ctk.CTkFrame(quest_card, fg_color="transparent")
        details_frame.pack(pady=10)

        details = [
            (f"⏱️ {quest[5]} min", "#00AAFF"),
            (f"⭐ {quest[4]} XP", "#FFD700"),
            (f"📊 Difficulty {quest[6]}/5", "#FF6600")
        ]

        for i, (text, color) in enumerate(details):
            ctk.CTkLabel(
                details_frame,
                text=text,
                font=("Arial", 13),
                text_color=color
            ).grid(row=0, column=i, padx=15)

        # Why this quest?
        why_frame = ctk.CTkFrame(quest_card, fg_color="#1a1a1a", corner_radius=8)
        why_frame.pack(fill="x", padx=20, pady=(10, 20))

        ctk.CTkLabel(
            why_frame,
            text="💡 Why this quest today?",
            font=("Arial", 13, "bold"),
            text_color="#FFD700"
        ).pack(pady=(10, 5), padx=15)

        ctk.CTkLabel(
            why_frame,
            text=quest_data['reason'],
            font=("Arial", 12),
            text_color="#CCCCCC",
            wraplength=450,
            justify="left"
        ).pack(pady=(0, 10), padx=15)

        # Start quest button
        ctk.CTkButton(
            quest_card,
            text="▶ Start Enhanced Quest",
            command=lambda: self.start_quest(quest[0]),
            width=250,
            height=50,
            font=("Arial", 16, "bold"),
            fg_color="#0066CC",
            hover_color="#0088EE"
        ).pack(pady=(10, 25))

    def show_pattern_insights(self, parent):
        """Show pattern recognition insights"""
        insights_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        insights_section.grid(row=1, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            insights_section,
            text="🔍 Pattern Insights",
            font=("Arial", 20, "bold"),
            text_color="#00AAFF"
        ).pack(pady=(20, 10))

        # Get insights from context engine
        profile = self.db.get_user_profile()
        insights = self.context_engine.get_pattern_insights()

        if insights:
            for insight in insights[:3]:  # Show top 3
                insight_card = ctk.CTkFrame(
                    insights_section,
                    fg_color="#2a2a2a",
                    corner_radius=10
                )
                insight_card.pack(fill="x", padx=20, pady=5)

                ctk.CTkLabel(
                    insight_card,
                    text=insight['title'],
                    font=("Arial", 14, "bold"),
                    text_color="#FFD700"
                ).pack(pady=(15, 5), padx=15, anchor="w")

                ctk.CTkLabel(
                    insight_card,
                    text=insight['message'],
                    font=("Arial", 12),
                    text_color="#CCCCCC",
                    wraplength=500,
                    justify="left"
                ).pack(pady=(0, 15), padx=15, anchor="w")
        else:
            ctk.CTkLabel(
                insights_section,
                text="Complete more quests to unlock pattern insights!",
                font=("Arial", 13),
                text_color="#888888"
            ).pack(pady=(0, 20))

    def show_quick_actions(self, parent):
        """Show quick action buttons"""
        actions_section = ctk.CTkFrame(parent, fg_color="transparent")
        actions_section.grid(row=2, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            actions_section,
            text="⚡ Quick Actions",
            font=("Arial", 18, "bold")
        ).pack(pady=(10, 15))

        button_frame = ctk.CTkFrame(actions_section, fg_color="transparent")
        button_frame.pack()

        actions = [
            ("🛡️ Need Shield?", self.open_shield, "#CC0000"),
            ("📝 Quick Reflection", self.open_reflection, "#0066CC"),
            ("📊 View Progress", self.open_progress, "#00AA00")
        ]

        for i, (text, command, color) in enumerate(actions):
            ctk.CTkButton(
                button_frame,
                text=text,
                command=command,
                width=180,
                height=50,
                font=("Arial", 14),
                fg_color=color,
                hover_color=self.lighten_color(color)
            ).grid(row=0, column=i, padx=10)

    def start_quest(self, quest_id):
        """Launch enhanced quest screen"""
        # Clear parent and show quest screen
        for widget in self.master.winfo_children():
            widget.destroy()

        quest_screen = EnhancedQuestScreen(
            self.master,
            self.db,
            self.on_quest_complete,
            self.on_quest_back
        )
        quest_screen.grid(row=0, column=0, sticky="nsew")

    def on_quest_complete(self, quest_id, xp_earned, was_primary):
        """Quest completed - rebuild home"""
        self.setup_ui()

    def on_quest_back(self):
        """Back from quest - rebuild home"""
        self.setup_ui()

    def open_shield(self):
        """Open shield mode"""
        # TODO: Navigate to shield tab
        pass

    def open_reflection(self):
        """Open reflection"""
        # TODO: Navigate to reflection tab
        pass

    def open_progress(self):
        """Open progress"""
        # TODO: Navigate to progress tab
        pass

    def lighten_color(self, color):
        """Lighten a hex color for hover effect"""
        # Simple approach: just return a lighter variant
        lighter_colors = {
            "#CC0000": "#EE0000",
            "#0066CC": "#0088EE",
            "#00AA00": "#00CC00"
        }
        return lighter_colors.get(color, color)
