"""
BackToLife DEMO - Enhanced Quest System
Shows the full vision with all features integrated
"""
import customtkinter as ctk
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.database import Database
from src.screens.enhanced_quest_screen import EnhancedQuestScreen
from src.services.audio_service import get_audio_service


class DemoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # App configuration
        self.title("BackToLife DEMO - Full Enhanced Quest Experience")
        self.geometry("900x700")

        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Initialize database
        self.db = Database()

        # Initialize audio
        self.audio = get_audio_service()

        # Setup UI
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.show_welcome()

    def show_welcome(self):
        """Show welcome screen with demo explanation"""
        # Clear
        for widget in self.winfo_children():
            widget.destroy()

        # Welcome container
        welcome_frame = ctk.CTkFrame(self, fg_color="transparent")
        welcome_frame.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)
        welcome_frame.grid_columnconfigure(0, weight=1)

        # Title
        ctk.CTkLabel(
            welcome_frame,
            text="🏆 BackToLife DEMO 🏆",
            font=("Arial", 40, "bold"),
            text_color="#FFD700"
        ).grid(row=0, column=0, pady=(20, 10))

        # Subtitle
        ctk.CTkLabel(
            welcome_frame,
            text="The Complete Enhanced Quest Experience",
            font=("Arial", 20),
            text_color="#00AAFF"
        ).grid(row=1, column=0, pady=(0, 30))

        # Description
        desc_frame = ctk.CTkFrame(welcome_frame, fg_color="#1a1a1a", corner_radius=15)
        desc_frame.grid(row=2, column=0, sticky="ew", pady=20)

        desc_text = """This demo shows the FULL vision of BackToLife:

✨ Audio Guidance - Every step narrated with text-to-speech
🎯 Step-by-Step Coaching - Real-time guidance through each action
📚 Psychoeducation - Learn WHY your brain works this way
💡 Flashcards - Spaced repetition learning
🎓 Interactive Quiz - Test understanding (ADHD-friendly)
📊 Pattern Recognition - See insights you can't see yourself
📈 Skill Building - Progressive skill chains

This ONE quest demonstrates ALL the features that were missing
from the original build.

Quest: "Organize One Desktop File"
Duration: ~10 minutes
Features: ALL of them

Ready to see the future of BackToLife?"""

        ctk.CTkLabel(
            desc_frame,
            text=desc_text,
            font=("Arial", 14),
            wraplength=700,
            justify="left"
        ).pack(pady=30, padx=40)

        # Audio toggle
        audio_frame = ctk.CTkFrame(welcome_frame, fg_color="#2a2a2a", corner_radius=10)
        audio_frame.grid(row=3, column=0, sticky="ew", pady=20)

        self.audio_toggle_btn = ctk.CTkButton(
            audio_frame,
            text="🔊 Audio: ON",
            command=self.toggle_audio,
            width=200,
            height=50,
            font=("Arial", 14),
            fg_color="#00AA00",
            hover_color="#00CC00"
        )
        self.audio_toggle_btn.pack(pady=20)

        ctk.CTkLabel(
            audio_frame,
            text="(Audio guidance is a core feature - recommended to keep ON)",
            font=("Arial", 11),
            text_color="#888888"
        ).pack(pady=(0, 15))

        # Start button
        ctk.CTkButton(
            welcome_frame,
            text="▶ Start Enhanced Quest Demo",
            command=self.start_demo_quest,
            width=350,
            height=70,
            font=("Arial", 20, "bold"),
            fg_color="#0066CC",
            hover_color="#0088EE"
        ).grid(row=4, column=0, pady=30)

        # Info
        ctk.CTkLabel(
            welcome_frame,
            text="Note: This is a demonstration. No data will be saved permanently.",
            font=("Arial", 11),
            text_color="#666666"
        ).grid(row=5, column=0, pady=(0, 20))

    def toggle_audio(self):
        """Toggle audio on/off"""
        enabled = self.audio.toggle()
        if enabled:
            self.audio_toggle_btn.configure(
                text="🔊 Audio: ON",
                fg_color="#00AA00"
            )
        else:
            self.audio_toggle_btn.configure(
                text="🔇 Audio: OFF",
                fg_color="#666666"
            )

    def start_demo_quest(self):
        """Launch the enhanced quest demo"""
        # Clear
        for widget in self.winfo_children():
            widget.destroy()

        # Show enhanced quest screen
        enhanced_quest = EnhancedQuestScreen(
            self,
            self.db,
            self.on_demo_complete,
            self.show_welcome
        )
        enhanced_quest.grid(row=0, column=0, sticky="nsew")

    def on_demo_complete(self, quest_id, xp_earned, was_primary):
        """Demo quest completed"""
        # Show completion summary
        for widget in self.winfo_children():
            widget.destroy()

        summary_frame = ctk.CTkFrame(self, fg_color="transparent")
        summary_frame.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)
        summary_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            summary_frame,
            text="🎉 DEMO COMPLETE! 🎉",
            font=("Arial", 40, "bold"),
            text_color="#00FF00"
        ).grid(row=0, column=0, pady=(40, 20))

        summary_text = f"""You just experienced the FULL BackToLife vision:

✓ Psychoeducation explaining executive dysfunction
✓ Step-by-step audio guidance through organizing a file
✓ Pattern insights showing your completion patterns
✓ Flashcard teaching ADHD organization concepts
✓ Interactive quiz testing boundary-setting skills
✓ Skill progression showing your growth path

Total XP Earned: {xp_earned}

This is what the REAL app will feel like for EVERY quest:
- Teaching while doing (not separate modules)
- Audio guidance for accessibility
- Learning reinforcement through flashcards
- Skill building through practice
- Pattern recognition showing what you can't see

This is the app you actually need."""

        summary_box = ctk.CTkFrame(summary_frame, fg_color="#1a1a1a", corner_radius=15)
        summary_box.grid(row=1, column=0, sticky="ew", pady=30)

        ctk.CTkLabel(
            summary_box,
            text=summary_text,
            font=("Arial", 15),
            wraplength=700,
            justify="left"
        ).pack(pady=40, padx=40)

        # Buttons
        button_frame = ctk.CTkFrame(summary_frame, fg_color="transparent")
        button_frame.grid(row=2, column=0, pady=20)

        ctk.CTkButton(
            button_frame,
            text="🔄 Try Demo Again",
            command=self.show_welcome,
            width=200,
            height=50,
            font=("Arial", 14)
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            button_frame,
            text="✓ Exit Demo",
            command=self.quit,
            width=200,
            height=50,
            font=("Arial", 14),
            fg_color="#666666",
            hover_color="#888888"
        ).pack(side="left", padx=10)

        if self.audio.is_enabled():
            self.audio.speak(f"Demo complete! You experienced the full BackToLife vision. You earned {xp_earned} experience points. This is what every quest will feel like in the real app: teaching while doing, audio guidance, learning reinforcement, and skill building. This is the app you actually need, champion.")

    def run(self):
        """Start the application"""
        self.mainloop()


if __name__ == "__main__":
    app = DemoApp()
    app.run()
