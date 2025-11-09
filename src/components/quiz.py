"""
Interactive Quiz Component - Reinforcement Learning
ADHD-friendly: 3 options max, audio support, no pressure
"""
import customtkinter as ctk
from src.services.audio_service import get_audio_service


class QuizWidget(ctk.CTkFrame):
    """
    Interactive quiz for skill reinforcement

    ADHD-friendly design:
    - Max 3 options
    - No time pressure
    - Immediate feedback
    - Audio support
    - Can retry
    """

    def __init__(self, parent, quiz_data, on_complete):
        super().__init__(parent, fg_color="#1a1a1a", corner_radius=15)

        self.quiz = quiz_data
        self.on_complete = on_complete
        self.audio = get_audio_service()
        self.selected_option = None
        self.answered = False

        self.grid_columnconfigure(0, weight=1)
        self.setup_ui()

    def setup_ui(self):
        """Build quiz UI"""
        # Header
        ctk.CTkLabel(
            self,
            text="🎓 SKILL CHECK",
            font=("Arial", 24, "bold"),
            text_color="#00AAFF"
        ).grid(row=0, column=0, pady=(30, 10))

        ctk.CTkLabel(
            self,
            text="This tests your understanding (no grades, just learning)",
            font=("Arial", 14),
            text_color="#888888"
        ).grid(row=1, column=0, pady=(0, 20))

        # Question
        question_frame = ctk.CTkFrame(self, fg_color="#2a2a2a", corner_radius=10)
        question_frame.grid(row=2, column=0, sticky="ew", padx=30, pady=20)

        ctk.CTkLabel(
            question_frame,
            text=self.quiz['question'],
            font=("Arial", 18, "bold"),
            wraplength=500,
            justify="center"
        ).pack(pady=30, padx=30)

        # Audio question button
        ctk.CTkButton(
            question_frame,
            text="🔊 Hear Question",
            command=lambda: self.audio.speak(self.quiz.get('audio_question', self.quiz['question'])),
            width=150,
            height=35,
            font=("Arial", 12),
            fg_color="#444444",
            hover_color="#666666"
        ).pack(pady=(0, 20))

        # Options (radio buttons)
        self.options_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.options_frame.grid(row=3, column=0, sticky="ew", padx=30, pady=20)

        self.option_var = ctk.StringVar(value="")
        self.option_buttons = []

        for i, option in enumerate(self.quiz['options']):
            option_frame = ctk.CTkFrame(
                self.options_frame,
                fg_color="#0a0a0a",
                corner_radius=8
            )
            option_frame.pack(fill="x", pady=8)

            radio = ctk.CTkRadioButton(
                option_frame,
                text=option['text'],
                variable=self.option_var,
                value=str(i),
                font=("Arial", 15),
                text_color="#FFFFFF"
            )
            radio.pack(side="left", padx=20, pady=15, anchor="w")

            self.option_buttons.append(radio)

        # Submit button
        self.submit_button = ctk.CTkButton(
            self,
            text="Submit Answer",
            command=self.check_answer,
            width=200,
            height=50,
            font=("Arial", 16),
            fg_color="#0066CC",
            hover_color="#0088EE"
        )
        self.submit_button.grid(row=4, column=0, pady=20)

        # Feedback frame (hidden initially)
        self.feedback_frame = ctk.CTkFrame(self, fg_color="#2a2a2a", corner_radius=10)
        # Don't grid yet

        # Auto-play question
        if self.audio.is_enabled():
            self.audio.speak(self.quiz.get('audio_question', self.quiz['question']))

    def check_answer(self):
        """Check selected answer and show feedback"""
        selected = self.option_var.get()

        if not selected:
            # No selection
            self.audio.speak("Please select an answer first.")
            return

        selected_index = int(selected)
        selected_option = self.quiz['options'][selected_index]

        # Show feedback
        self.show_feedback(selected_option)

        if selected_option['correct']:
            # Correct answer - allow completion
            self.answered = True
        else:
            # Wrong answer - can retry
            self.answered = False

    def show_feedback(self, option):
        """Show feedback for selected answer"""
        # Clear previous feedback
        for widget in self.feedback_frame.winfo_children():
            widget.destroy()

        # Grid the feedback frame
        self.feedback_frame.grid(row=5, column=0, sticky="ew", padx=30, pady=20)

        # Feedback header
        if option['correct']:
            header_text = "✅ CORRECT!"
            header_color = "#00FF00"
        else:
            header_text = "❌ Not Quite"
            header_color = "#FF6600"

        ctk.CTkLabel(
            self.feedback_frame,
            text=header_text,
            font=("Arial", 22, "bold"),
            text_color=header_color
        ).pack(pady=(20, 10))

        # Feedback content
        ctk.CTkLabel(
            self.feedback_frame,
            text=option['feedback'],
            font=("Arial", 15),
            wraplength=500,
            justify="left"
        ).pack(pady=10, padx=30)

        # Audio feedback button
        ctk.CTkButton(
            self.feedback_frame,
            text="🔊 Hear Explanation",
            command=lambda: self.audio.speak(option.get('audio_feedback', option['feedback'])),
            width=150,
            height=35,
            font=("Arial", 12),
            fg_color="#444444",
            hover_color="#666666"
        ).pack(pady=10)

        # Action button
        if option['correct']:
            # Complete button
            ctk.CTkButton(
                self.feedback_frame,
                text="Continue ✓",
                command=self.complete_quiz,
                width=200,
                height=50,
                font=("Arial", 16),
                fg_color="#00AA00",
                hover_color="#00CC00"
            ).pack(pady=20)

        else:
            # Try again button
            ctk.CTkButton(
                self.feedback_frame,
                text="Try Another Answer",
                command=self.retry,
                width=200,
                height=50,
                font=("Arial", 16),
                fg_color="#0066CC",
                hover_color="#0088EE"
            ).pack(pady=20)

        # Play audio feedback
        if self.audio.is_enabled():
            self.audio.speak(option.get('audio_feedback', option['feedback']))

    def retry(self):
        """Reset for retry"""
        # Hide feedback
        self.feedback_frame.grid_forget()

        # Clear selection
        self.option_var.set("")

        # Re-enable submit button
        self.submit_button.configure(state="normal")

    def complete_quiz(self):
        """Mark quiz as complete"""
        self.audio.stop()
        self.on_complete(correct=True, xp_bonus=50)
