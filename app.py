"""
BackToLife - Main Application
A comprehensive digital therapeutic app for life reconstruction
Tailored for Bradly's specific needs
"""
import customtkinter as ctk
import sys
import os
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.database import Database
from src.data.quest_database import initialize_quest_database
from src.utils.context_engine import ContextEngine
from src.screens.home_screen import HomeScreen
from src.screens.progress_screen import ProgressScreen
from src.screens.reflection_screen import ReflectionScreen
from src.screens.shield_mode_screen import ShieldModeScreen


class BackToLifeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # App configuration
        self.title("BackToLife - Your Champion Journey")
        self.geometry("800x600")

        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Initialize database
        self.db = Database()
        initialize_quest_database(self.db)

        # Initialize context engine
        self.context_engine = ContextEngine(self.db)

        # Get daily quest
        self.current_quest = None
        self.bonus_quests = []
        self.load_daily_quest()

        # Setup UI
        self.setup_ui()

    def setup_ui(self):
        """Setup main application UI"""
        # Main container
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create main content frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # Load home screen
        self.show_home_screen()

    def load_daily_quest(self):
        """Load today's quest(s)"""
        # Check if already completed today's primary quest
        completed_today = self.db.get_today_completed_quests()

        if not completed_today:
            # Select new quest
            self.current_quest = self.context_engine.select_daily_quest()
            if self.current_quest:
                self.bonus_quests = self.context_engine.select_bonus_quests(
                    self.current_quest, count=3
                )
        else:
            # Already completed, show celebration or bonus quests only
            self.current_quest = None
            # Get some bonus quests anyway
            temp_quest = self.context_engine.select_daily_quest()
            if temp_quest:
                self.bonus_quests = self.context_engine.select_bonus_quests(
                    temp_quest, count=5
                )

    def show_home_screen(self):
        """Display home screen with daily quest"""
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create home screen
        home = HomeScreen(
            self.main_frame,
            self.db,
            self.context_engine,
            self.current_quest,
            self.bonus_quests,
            self.on_quest_complete,
            self.show_progress,
            self.show_reflection,
            self.show_shield_mode
        )
        home.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def show_progress(self):
        """Display progress screen"""
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create progress screen
        progress = ProgressScreen(
            self.main_frame,
            self.db,
            self.show_home_screen
        )
        progress.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def show_reflection(self):
        """Display reflection screen"""
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create reflection screen
        reflection = ReflectionScreen(
            self.main_frame,
            self.db,
            self.show_home_screen
        )
        reflection.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def show_shield_mode(self):
        """Display Shield Mode screen"""
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create Shield Mode screen
        shield = ShieldModeScreen(
            self.main_frame,
            self.db,
            self.show_home_screen
        )
        shield.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def on_quest_complete(self, quest_id, xp_earned, was_primary=True):
        """Handle quest completion"""
        # Record in database
        leveled_up = self.db.complete_quest(
            quest_id, xp_earned, was_primary=was_primary
        )

        # Show celebration
        if leveled_up:
            self.show_level_up_celebration()
        else:
            self.show_quest_complete_celebration(xp_earned)

        # Reload quest
        self.load_daily_quest()
        self.show_home_screen()

    def show_quest_complete_celebration(self, xp_earned):
        """Show quest completion celebration"""
        celebration = ctk.CTkToplevel(self)
        celebration.title("Quest Complete!")
        celebration.geometry("400x300")
        celebration.transient(self)
        celebration.grab_set()

        # Center the window
        celebration.update_idletasks()
        x = (celebration.winfo_screenwidth() // 2) - (400 // 2)
        y = (celebration.winfo_screenheight() // 2) - (300 // 2)
        celebration.geometry(f"400x300+{x}+{y}")

        frame = ctk.CTkFrame(celebration)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            frame,
            text="✨ QUEST COMPLETE ✨",
            font=("Arial", 32, "bold")
        ).pack(pady=30)

        ctk.CTkLabel(
            frame,
            text=f"+{xp_earned} XP!",
            font=("Arial", 24),
            text_color="#00ff00"
        ).pack(pady=20)

        ctk.CTkLabel(
            frame,
            text="The champion is waking up.",
            font=("Arial", 16)
        ).pack(pady=20)

        ctk.CTkButton(
            frame,
            text="Continue",
            command=celebration.destroy,
            width=200,
            height=50,
            font=("Arial", 16)
        ).pack(pady=20)

    def show_level_up_celebration(self):
        """Show level up celebration"""
        profile = self.db.get_user_profile()
        new_level = profile['level']

        celebration = ctk.CTkToplevel(self)
        celebration.title("LEVEL UP!")
        celebration.geometry("500x400")
        celebration.transient(self)
        celebration.grab_set()

        # Center the window
        celebration.update_idletasks()
        x = (celebration.winfo_screenwidth() // 2) - (500 // 2)
        y = (celebration.winfo_screenheight() // 2) - (400 // 2)
        celebration.geometry(f"500x400+{x}+{y}")

        frame = ctk.CTkFrame(celebration)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            frame,
            text="🏆 LEVEL UP! 🏆",
            font=("Arial", 36, "bold"),
            text_color="#FFD700"
        ).pack(pady=30)

        ctk.CTkLabel(
            frame,
            text=f"LEVEL {new_level}",
            font=("Arial", 48, "bold"),
            text_color="#00ff00"
        ).pack(pady=20)

        ctk.CTkLabel(
            frame,
            text="You're becoming unstoppable.",
            font=("Arial", 18)
        ).pack(pady=20)

        ctk.CTkLabel(
            frame,
            text="The champion is returning.",
            font=("Arial", 16),
            text_color="#888888"
        ).pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Continue Journey",
            command=celebration.destroy,
            width=250,
            height=50,
            font=("Arial", 18)
        ).pack(pady=30)

    def run(self):
        """Start the application"""
        self.mainloop()


if __name__ == "__main__":
    app = BackToLifeApp()
    app.run()
