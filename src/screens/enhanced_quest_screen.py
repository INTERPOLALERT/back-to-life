"""
Enhanced Quest Screen - Full Teaching-While-Doing Experience

This demonstrates the complete vision:
- Psychoeducation before quest
- Step-by-step audio guidance during quest
- Pattern insights
- Flashcard learning after quest
- Interactive quiz
- Skill progression
"""
import customtkinter as ctk
from datetime import datetime
import time

from src.data.enhanced_quests import DEMO_QUEST
from src.services.audio_service import get_audio_service
from src.components.flashcard import FlashcardWidget, FlashcardManager
from src.components.quiz import QuizWidget


class EnhancedQuestScreen(ctk.CTkFrame):
    """
    Complete enhanced quest experience
    """

    def __init__(self, parent, db, on_complete, on_back):
        super().__init__(parent, corner_radius=0)

        self.db = db
        self.on_complete = on_complete
        self.on_back = on_back
        self.audio = get_audio_service()
        self.flashcard_manager = FlashcardManager(db)

        self.quest = DEMO_QUEST
        self.current_step = 0
        self.quest_start_time = None

        # Flow stages
        self.stage = 'intro'  # intro -> steps -> flashcard -> quiz -> complete

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.show_intro()

    def show_intro(self):
        """Show psychoeducation and pattern insights before quest"""
        # Clear screen
        for widget in self.winfo_children():
            widget.destroy()

        # Create scrollable frame
        scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        scroll_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        scroll_frame.grid_columnconfigure(0, weight=1)

        # Header
        ctk.CTkLabel(
            scroll_frame,
            text="Before We Begin...",
            font=("Arial", 32, "bold")
        ).grid(row=0, column=0, pady=(20, 10))

        # Psychoeducation
        psychoed = self.quest['psychoeducation']['before_quest']

        psychoed_frame = ctk.CTkFrame(scroll_frame, fg_color="#1a1a1a", corner_radius=15)
        psychoed_frame.grid(row=1, column=0, sticky="ew", pady=20)

        ctk.CTkLabel(
            psychoed_frame,
            text=f"📚 {psychoed['title']}",
            font=("Arial", 20, "bold"),
            text_color="#FFD700"
        ).pack(pady=(20, 10), padx=20)

        ctk.CTkLabel(
            psychoed_frame,
            text=psychoed['content'],
            font=("Arial", 14),
            wraplength=600,
            justify="left"
        ).pack(pady=10, padx=30)

        # Audio button
        ctk.CTkButton(
            psychoed_frame,
            text="🔊 Listen to This",
            command=lambda: self.audio.speak(psychoed['audio_script']),
            width=180,
            height=45,
            font=("Arial", 14),
            fg_color="#0066CC",
            hover_color="#0088EE"
        ).pack(pady=20)

        # Pattern insights
        if 'pattern_insights' in self.quest:
            insights = self.quest['pattern_insights']
            insight_frame = ctk.CTkFrame(scroll_frame, fg_color="#2a2a2a", corner_radius=10)
            insight_frame.grid(row=2, column=0, sticky="ew", pady=20)

            ctk.CTkLabel(
                insight_frame,
                text="📊 What I Know About You",
                font=("Arial", 18, "bold"),
                text_color="#00AAFF"
            ).pack(pady=(15, 10), padx=20)

            ctk.CTkLabel(
                insight_frame,
                text=insights['insight'],
                font=("Arial", 13),
                wraplength=600,
                justify="left",
                text_color="#CCCCCC"
            ).pack(pady=10, padx=30)

            # Stats
            stats_text = f"""Completion Rate: {insights['completion_rate']}
Best Time: {insights['best_time']}
Pattern: {insights['correlation']}"""

            ctk.CTkLabel(
                insight_frame,
                text=stats_text,
                font=("Arial", 11),
                text_color="#888888",
                justify="left"
            ).pack(pady=(5, 15), padx=30)

        # Start quest button
        ctk.CTkButton(
            scroll_frame,
            text="I'm Ready - Let's Do This",
            command=self.start_quest_steps,
            width=300,
            height=60,
            font=("Arial", 18, "bold"),
            fg_color="#00AA00",
            hover_color="#00CC00"
        ).grid(row=3, column=0, pady=30)

        # Auto-play intro audio
        if self.audio.is_enabled():
            self.audio.speak(psychoed['audio_script'])

    def start_quest_steps(self):
        """Begin step-by-step guided quest"""
        self.stage = 'steps'
        self.current_step = 0
        self.quest_start_time = time.time()
        self.show_step()

    def show_step(self):
        """Show current step with audio guidance"""
        # Clear screen
        for widget in self.winfo_children():
            widget.destroy()

        step = self.quest['steps'][self.current_step]
        total_steps = len(self.quest['steps'])

        # Main container
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(2, weight=1)

        # Progress indicator
        progress_text = f"Step {step['number']} of {total_steps}"
        ctk.CTkLabel(
            container,
            text=progress_text,
            font=("Arial", 14),
            text_color="#888888"
        ).grid(row=0, column=0, pady=(0, 10))

        # Progress bar
        progress = step['number'] / total_steps
        progress_bar = ctk.CTkProgressBar(container, width=400, height=8)
        progress_bar.set(progress)
        progress_bar.grid(row=1, column=0, pady=(0, 30))

        # Step card
        step_card = ctk.CTkFrame(container, fg_color="#1a1a1a", corner_radius=15)
        step_card.grid(row=2, column=0, sticky="ew", ipady=30)

        # Step title
        ctk.CTkLabel(
            step_card,
            text=step['title'],
            font=("Arial", 28, "bold")
        ).pack(pady=(30, 15))

        # Step instruction
        ctk.CTkLabel(
            step_card,
            text=step['instruction'],
            font=("Arial", 16),
            wraplength=500,
            text_color="#CCCCCC"
        ).pack(pady=10)

        # Why this step
        why_frame = ctk.CTkFrame(step_card, fg_color="#2a2a2a", corner_radius=10)
        why_frame.pack(pady=20, padx=40, fill="x")

        ctk.CTkLabel(
            why_frame,
            text=f"💡 Why: {step['why']}",
            font=("Arial", 13),
            text_color="#FFAA00",
            wraplength=450
        ).pack(pady=15, padx=20)

        # Audio guidance controls
        audio_frame = ctk.CTkFrame(step_card, fg_color="transparent")
        audio_frame.pack(pady=20)

        ctk.CTkButton(
            audio_frame,
            text="🔊 Hear Step Guidance",
            command=lambda: self.audio.speak(step['audio_script']),
            width=200,
            height=50,
            font=("Arial", 14),
            fg_color="#0066CC",
            hover_color="#0088EE"
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            audio_frame,
            text="⏸️ Stop Audio",
            command=self.audio.stop,
            width=140,
            height=50,
            font=("Arial", 14),
            fg_color="#444444",
            hover_color="#666666"
        ).pack(side="left", padx=10)

        # Navigation buttons
        nav_frame = ctk.CTkFrame(container, fg_color="transparent")
        nav_frame.grid(row=3, column=0, pady=30)

        if self.current_step > 0:
            ctk.CTkButton(
                nav_frame,
                text="← Previous Step",
                command=self.previous_step,
                width=150,
                height=45,
                font=("Arial", 14)
            ).pack(side="left", padx=10)

        if self.current_step < total_steps - 1:
            ctk.CTkButton(
                nav_frame,
                text="Next Step →",
                command=self.next_step,
                width=150,
                height=45,
                font=("Arial", 14),
                fg_color="#00AA00",
                hover_color="#00CC00"
            ).pack(side="left", padx=10)
        else:
            ctk.CTkButton(
                nav_frame,
                text="Complete Quest! ✓",
                command=self.finish_quest_steps,
                width=200,
                height=55,
                font=("Arial", 16, "bold"),
                fg_color="#00AA00",
                hover_color="#00CC00"
            ).pack(side="left", padx=10)

        # Auto-play step audio
        if self.audio.is_enabled():
            self.audio.speak(step['audio_script'])

    def next_step(self):
        """Move to next step"""
        if self.current_step < len(self.quest['steps']) - 1:
            self.current_step += 1
            self.show_step()

    def previous_step(self):
        """Go back to previous step"""
        if self.current_step > 0:
            self.current_step -= 1
            self.show_step()

    def finish_quest_steps(self):
        """Quest steps complete, show psychoeducation after"""
        self.stage = 'post_psychoed'
        self.show_post_psychoeducation()

    def show_post_psychoeducation(self):
        """Show what they learned after completing quest"""
        # Clear screen
        for widget in self.winfo_children():
            widget.destroy()

        # Container
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)
        container.grid_columnconfigure(0, weight=1)

        # Celebration
        ctk.CTkLabel(
            container,
            text="🎉 QUEST COMPLETE! 🎉",
            font=("Arial", 36, "bold"),
            text_color="#00FF00"
        ).grid(row=0, column=0, pady=(20, 10))

        # XP earned
        xp_text = f"+{self.quest['xp_value']} XP"
        ctk.CTkLabel(
            container,
            text=xp_text,
            font=("Arial", 24),
            text_color="#FFD700"
        ).grid(row=1, column=0, pady=10)

        # Post psychoeducation
        psychoed = self.quest['psychoeducation']['after_quest']

        psychoed_frame = ctk.CTkFrame(container, fg_color="#1a1a1a", corner_radius=15)
        psychoed_frame.grid(row=2, column=0, sticky="ew", pady=30)

        ctk.CTkLabel(
            psychoed_frame,
            text=f"🎓 {psychoed['title']}",
            font=("Arial", 20, "bold"),
            text_color="#00AAFF"
        ).pack(pady=(20, 10), padx=20)

        ctk.CTkLabel(
            psychoed_frame,
            text=psychoed['content'],
            font=("Arial", 14),
            wraplength=600,
            justify="left"
        ).pack(pady=10, padx=30)

        ctk.CTkButton(
            psychoed_frame,
            text="🔊 Listen to This",
            command=lambda: self.audio.speak(psychoed['audio_script']),
            width=180,
            height=45,
            font=("Arial", 14),
            fg_color="#0066CC",
            hover_color="#0088EE"
        ).pack(pady=20)

        # Continue to flashcard button
        ctk.CTkButton(
            container,
            text="Continue to Learning Moment →",
            command=self.show_flashcard,
            width=300,
            height=55,
            font=("Arial", 16),
            fg_color="#00AA00",
            hover_color="#00CC00"
        ).grid(row=3, column=0, pady=30)

        # Auto-play audio
        if self.audio.is_enabled():
            self.audio.speak(psychoed['audio_script'])

    def show_flashcard(self):
        """Show flashcard for spaced repetition learning"""
        self.stage = 'flashcard'

        # Clear screen
        for widget in self.winfo_children():
            widget.destroy()

        # Show flashcard widget
        flashcard_widget = FlashcardWidget(
            self,
            self.quest['flashcard'],
            self.on_flashcard_complete
        )
        flashcard_widget.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)

    def on_flashcard_complete(self, flashcard_id):
        """Flashcard learned, move to quiz"""
        # Record flashcard review
        self.flashcard_manager.record_review(flashcard_id, correct=True)

        # Show quiz
        self.show_quiz()

    def show_quiz(self):
        """Show interactive quiz"""
        self.stage = 'quiz'

        # Clear screen
        for widget in self.winfo_children():
            widget.destroy()

        # Show quiz widget
        quiz_widget = QuizWidget(
            self,
            self.quest['quiz'],
            self.on_quiz_complete
        )
        quiz_widget.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)

    def on_quiz_complete(self, correct, xp_bonus):
        """Quiz complete, show final celebration"""
        # Add bonus XP
        total_xp = self.quest['xp_value'] + xp_bonus

        # Record quest completion
        completion_time = int(time.time() - self.quest_start_time) if self.quest_start_time else 0

        # For demo, we'll just show completion
        # In real app, would call database
        self.show_final_celebration(total_xp)

    def show_final_celebration(self, total_xp):
        """Final celebration with skill progress"""
        # Clear screen
        for widget in self.winfo_children():
            widget.destroy()

        # Container
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)
        container.grid_columnconfigure(0, weight=1)

        # Celebration
        ctk.CTkLabel(
            container,
            text="⭐ MASTERY ACHIEVED ⭐",
            font=("Arial", 36, "bold"),
            text_color="#FFD700"
        ).grid(row=0, column=0, pady=(20, 10))

        # Total XP
        ctk.CTkLabel(
            container,
            text=f"+{total_xp} XP Total!",
            font=("Arial", 28),
            text_color="#00FF00"
        ).grid(row=1, column=0, pady=10)

        ctk.CTkLabel(
            container,
            text="(Quest XP + Quiz Bonus)",
            font=("Arial", 13),
            text_color="#888888"
        ).grid(row=2, column=0, pady=(0, 20))

        # Skill progression
        skill = self.quest['skill_chain']
        skill_frame = ctk.CTkFrame(container, fg_color="#1a1a1a", corner_radius=15)
        skill_frame.grid(row=3, column=0, sticky="ew", pady=30)

        ctk.CTkLabel(
            skill_frame,
            text=f"📈 Skill Progress: {skill['skill_name']}",
            font=("Arial", 20, "bold"),
            text_color="#00AAFF"
        ).pack(pady=(20, 10), padx=20)

        # Show progression
        for level_text in skill['progression']:
            ctk.CTkLabel(
                skill_frame,
                text=level_text,
                font=("Arial", 14),
                text_color="#CCCCCC",
                justify="left"
            ).pack(pady=3, padx=40, anchor="w")

        ctk.CTkLabel(
            skill_frame,
            text="",
            font=("Arial", 1)
        ).pack(pady=10)

        # Champion message
        champion_frame = ctk.CTkFrame(container, fg_color="#2a2a2a", corner_radius=10)
        champion_frame.grid(row=4, column=0, sticky="ew", pady=20)

        ctk.CTkLabel(
            champion_frame,
            text="The champion is waking up.",
            font=("Arial", 18, "italic"),
            text_color="#888888"
        ).pack(pady=20, padx=30)

        # Done button
        ctk.CTkButton(
            container,
            text="Continue ✓",
            command=self.complete_enhanced_quest,
            width=250,
            height=60,
            font=("Arial", 18, "bold"),
            fg_color="#00AA00",
            hover_color="#00CC00"
        ).grid(row=5, column=0, pady=30)

        # Play celebration audio
        if self.audio.is_enabled():
            message = f"Amazing work, champion. You earned {total_xp} experience points total. You just leveled up your {skill['skill_name']} skill. You're not the same person who started this quest. The champion is waking up."
            self.audio.speak(message)

    def complete_enhanced_quest(self):
        """Complete the enhanced quest and return to home"""
        self.audio.stop()
        # In real app, would record completion to database
        # For demo, just go back
        self.on_complete(self.quest['id'], self.quest['xp_value'] + 50, was_primary=True)
