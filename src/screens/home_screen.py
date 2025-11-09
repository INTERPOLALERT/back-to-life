"""
BackToLife Home Screen
Main quest display and daily interaction
"""
import customtkinter as ctk
from datetime import datetime
import time


class HomeScreen(ctk.CTkFrame):
    def __init__(self, parent, db, context_engine, current_quest, bonus_quests,
                 on_quest_complete, show_progress, show_reflection, show_shield_mode):
        super().__init__(parent, corner_radius=0)

        self.db = db
        self.context_engine = context_engine
        self.current_quest = current_quest
        self.bonus_quests = bonus_quests
        self.on_quest_complete = on_quest_complete
        self.show_progress = show_progress
        self.show_reflection = show_reflection
        self.show_shield_mode = show_shield_mode

        self.quest_start_time = None
        self.timer_running = False

        self.grid_columnconfigure(0, weight=1)
        self.setup_ui()

    def setup_ui(self):
        """Build the home screen UI"""
        # Header with title and XP
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        header_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            header_frame,
            text="BackToLife",
            font=("Arial", 28, "bold")
        ).grid(row=0, column=0, padx=10, sticky="w")

        # User stats
        profile = self.db.get_user_profile()
        stats_text = f"🏆 Level {profile['level']} | {profile['xp']} XP | {profile['streak']} Day Streak"
        ctk.CTkLabel(
            header_frame,
            text=stats_text,
            font=("Arial", 14)
        ).grid(row=0, column=1, padx=10, sticky="e")

        # Champion message
        champion_msg = self.context_engine.get_champion_message(profile)
        ctk.CTkLabel(
            self,
            text=champion_msg,
            font=("Arial", 16, "italic"),
            text_color="#888888"
        ).grid(row=1, column=0, sticky="ew", pady=(0, 30))

        # Main quest area
        if self.current_quest:
            self.show_quest_card()
        else:
            self.show_completion_message()

        # Bonus quests section
        if self.bonus_quests:
            self.show_bonus_quests()

        # Shield Mode button
        shield_button = ctk.CTkButton(
            self,
            text="🛡️ SHIELD MODE",
            command=self.show_shield_mode,
            width=200,
            height=50,
            font=("Arial", 16),
            fg_color="#444444",
            hover_color="#666666"
        )
        shield_button.grid(row=10, column=0, pady=20)

        # Bottom navigation
        nav_frame = ctk.CTkFrame(self, fg_color="transparent")
        nav_frame.grid(row=11, column=0, sticky="ew", pady=(20, 0))
        nav_frame.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkButton(
            nav_frame,
            text="📊 Progress",
            command=self.show_progress,
            width=150,
            height=40
        ).grid(row=0, column=0, padx=10)

        ctk.CTkButton(
            nav_frame,
            text="📝 Reflection",
            command=self.show_reflection,
            width=150,
            height=40
        ).grid(row=0, column=1, padx=10)

        ctk.CTkButton(
            nav_frame,
            text="⚙️ Settings",
            command=self.show_settings,
            width=150,
            height=40
        ).grid(row=0, column=2, padx=10)

    def show_quest_card(self):
        """Display the main quest card"""
        quest = self.current_quest

        # Quest card
        quest_card = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=15)
        quest_card.grid(row=2, column=0, sticky="ew", pady=20, ipady=20)

        # Quest category badge
        category_name = quest[1].replace('_', ' ').title()
        ctk.CTkLabel(
            quest_card,
            text=f"🎯 {category_name}",
            font=("Arial", 14),
            text_color="#888888"
        ).pack(pady=(10, 5))

        # Quest title
        ctk.CTkLabel(
            quest_card,
            text=quest[2],  # title
            font=("Arial", 32, "bold"),
            wraplength=600
        ).pack(pady=10)

        # Quest description
        ctk.CTkLabel(
            quest_card,
            text=quest[3],  # description
            font=("Arial", 16),
            text_color="#CCCCCC",
            wraplength=600
        ).pack(pady=5)

        # Time indicator
        time_of_day = self.context_engine.get_time_of_day()
        current_time = datetime.now().strftime("%I:%M %p")
        ctk.CTkLabel(
            quest_card,
            text=f"⏰ Right Now: {current_time}",
            font=("Arial", 14),
            text_color="#888888"
        ).pack(pady=10)

        # Why this quest
        why_text = self.context_engine.get_context_aware_why_message(quest, time_of_day)
        why_frame = ctk.CTkFrame(quest_card, fg_color="#2a2a2a", corner_radius=10)
        why_frame.pack(pady=15, padx=30, fill="x")

        ctk.CTkLabel(
            why_frame,
            text=f"💡 {why_text}",
            font=("Arial", 14),
            text_color="#FFAA00",
            wraplength=550
        ).pack(pady=15, padx=15)

        # Instructions
        instructions_frame = ctk.CTkFrame(quest_card, fg_color="#0a0a0a", corner_radius=10)
        instructions_frame.pack(pady=15, padx=30, fill="x")

        ctk.CTkLabel(
            instructions_frame,
            text=quest[9],  # instructions (index 9)
            font=("Arial", 14),
            wraplength=550
        ).pack(pady=15, padx=15)

        # Start quest button
        self.start_button = ctk.CTkButton(
            quest_card,
            text="START QUEST",
            command=self.start_quest,
            width=300,
            height=60,
            font=("Arial", 24, "bold"),
            fg_color="#00AA00",
            hover_color="#00CC00"
        )
        self.start_button.pack(pady=20)

    def show_completion_message(self):
        """Show message when today's quest is already complete"""
        completion_card = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=15)
        completion_card.grid(row=2, column=0, sticky="ew", pady=20, ipady=40)

        ctk.CTkLabel(
            completion_card,
            text="✨ TODAY'S QUEST COMPLETE ✨",
            font=("Arial", 36, "bold"),
            text_color="#00FF00"
        ).pack(pady=30)

        ctk.CTkLabel(
            completion_card,
            text="You did it, Champion.",
            font=("Arial", 20)
        ).pack(pady=10)

        ctk.CTkLabel(
            completion_card,
            text="Rest now, or try a bonus quest below.",
            font=("Arial", 16),
            text_color="#888888"
        ).pack(pady=20)

    def show_bonus_quests(self):
        """Display optional bonus quests"""
        # Bonus header
        bonus_header = ctk.CTkFrame(self, fg_color="transparent")
        bonus_header.grid(row=3, column=0, sticky="ew", pady=(20, 10))

        ctk.CTkLabel(
            bonus_header,
            text="OPTIONAL BONUS QUESTS:",
            font=("Arial", 18, "bold"),
            text_color="#888888"
        ).pack()

        # Bonus quests list
        bonus_frame = ctk.CTkFrame(self, fg_color="transparent")
        bonus_frame.grid(row=4, column=0, sticky="ew", pady=10)

        for i, quest in enumerate(self.bonus_quests[:3]):
            quest_item = ctk.CTkFrame(bonus_frame, fg_color="#1a1a1a", corner_radius=10)
            quest_item.pack(fill="x", pady=5, padx=10)

            # Quest info
            info_frame = ctk.CTkFrame(quest_item, fg_color="transparent")
            info_frame.pack(side="left", fill="both", expand=True, padx=15, pady=10)

            ctk.CTkLabel(
                info_frame,
                text=quest[2],  # title
                font=("Arial", 16, "bold"),
                anchor="w"
            ).pack(anchor="w")

            ctk.CTkLabel(
                info_frame,
                text=f"{quest[1].replace('_', ' ').title()} • +{quest[5]} XP",
                font=("Arial", 12),
                text_color="#888888",
                anchor="w"
            ).pack(anchor="w")

            # Complete button
            ctk.CTkButton(
                quest_item,
                text="Complete",
                command=lambda q=quest: self.complete_bonus_quest(q),
                width=120,
                height=40
            ).pack(side="right", padx=15)

    def start_quest(self):
        """Start the quest timer"""
        self.quest_start_time = time.time()
        self.timer_running = True

        # Change button to complete
        self.start_button.configure(
            text="COMPLETE QUEST",
            command=self.complete_quest,
            fg_color="#FF6600",
            hover_color="#FF8800"
        )

    def complete_quest(self):
        """Mark quest as complete"""
        if not self.quest_start_time:
            self.quest_start_time = time.time()

        completion_time = int(time.time() - self.quest_start_time)

        # Record completion
        quest_id = self.current_quest[0]
        xp_earned = self.current_quest[5]  # xp_value

        self.on_quest_complete(quest_id, xp_earned, was_primary=True)

    def complete_bonus_quest(self, quest):
        """Mark bonus quest as complete"""
        quest_id = quest[0]
        xp_earned = quest[5]

        self.on_quest_complete(quest_id, xp_earned, was_primary=False)

    def show_settings(self):
        """Show settings dialog"""
        settings = ctk.CTkToplevel(self)
        settings.title("Settings")
        settings.geometry("400x300")
        settings.transient(self.master)

        frame = ctk.CTkFrame(settings)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            frame,
            text="⚙️ Settings",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            frame,
            text="Settings coming soon...",
            font=("Arial", 14)
        ).pack(pady=20)

        ctk.CTkButton(
            frame,
            text="Close",
            command=settings.destroy,
            width=150
        ).pack(pady=20)
