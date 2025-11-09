"""
Reflection Tab - Daily Check-in and Mood Tracking
"""
import customtkinter as ctk
from datetime import datetime


class ReflectionTab(ctk.CTkFrame):
    """
    Daily reflection with:
    - Mood check-in
    - Energy level tracking
    - Gratitude journaling
    - Pattern recognition
    - Reflection history
    """

    def __init__(self, parent, db, audio):
        super().__init__(parent, fg_color="transparent")

        self.db = db
        self.audio = audio

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.setup_ui()

    def setup_ui(self):
        """Build reflection UI"""
        # Header
        header = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=15)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header,
            text="📝 Daily Reflection",
            font=("Arial", 28, "bold"),
            text_color="#00AAFF"
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            header,
            text="Check in with yourself",
            font=("Arial", 14),
            text_color="#888888"
        ).pack(pady=(0, 20))

        # Main content
        self.content_scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        self.content_scroll.grid(row=1, column=0, sticky="nsew")
        self.content_scroll.grid_columnconfigure(0, weight=1)

        # Check if already reflected today
        today_reflection = self.db.get_reflection_by_date(datetime.now().strftime("%Y-%m-%d"))

        if today_reflection:
            self.show_completed_reflection(today_reflection)
        else:
            self.show_reflection_form()

    def show_reflection_form(self):
        """Show daily reflection form"""
        # Mood check-in
        mood_section = ctk.CTkFrame(self.content_scroll, fg_color="#1a1a1a", corner_radius=12)
        mood_section.grid(row=0, column=0, sticky="ew", pady=(0, 15))

        ctk.CTkLabel(
            mood_section,
            text="How are you feeling today?",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15))

        # Mood selector
        mood_frame = ctk.CTkFrame(mood_section, fg_color="transparent")
        mood_frame.pack(pady=(0, 20))

        self.selected_mood = ctk.StringVar(value="")
        moods = [
            ("😁", "Great", "#00FF00"),
            ("🙂", "Good", "#00AAFF"),
            ("😐", "Okay", "#FFAA00"),
            ("😔", "Not Great", "#FF6600"),
            ("😢", "Struggling", "#CC0000")
        ]

        for i, (emoji, label, color) in enumerate(moods):
            mood_btn = ctk.CTkRadioButton(
                mood_frame,
                text=f"{emoji} {label}",
                variable=self.selected_mood,
                value=label.lower(),
                font=("Arial", 15)
            )
            mood_btn.grid(row=i // 3, column=i % 3, padx=15, pady=8, sticky="w")

        # Energy level
        energy_section = ctk.CTkFrame(self.content_scroll, fg_color="#1a1a1a", corner_radius=12)
        energy_section.grid(row=1, column=0, sticky="ew", pady=(0, 15))

        ctk.CTkLabel(
            energy_section,
            text="What's your energy level?",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15))

        self.energy_slider = ctk.CTkSlider(
            energy_section,
            from_=0,
            to=10,
            number_of_steps=10,
            width=400
        )
        self.energy_slider.set(5)
        self.energy_slider.pack(pady=10)

        self.energy_label = ctk.CTkLabel(
            energy_section,
            text="5/10",
            font=("Arial", 14)
        )
        self.energy_label.pack(pady=(0, 20))

        self.energy_slider.configure(command=lambda v: self.energy_label.configure(text=f"{int(v)}/10"))

        # Sleep quality
        sleep_section = ctk.CTkFrame(self.content_scroll, fg_color="#1a1a1a", corner_radius=12)
        sleep_section.grid(row=2, column=0, sticky="ew", pady=(0, 15))

        ctk.CTkLabel(
            sleep_section,
            text="How did you sleep last night?",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15))

        self.sleep_quality = ctk.StringVar(value="")
        sleep_options = [
            ("😴 Great", "great"),
            ("🙂 Okay", "okay"),
            ("😕 Poor", "poor"),
            ("😵 Terrible", "terrible")
        ]

        for text, value in sleep_options:
            ctk.CTkRadioButton(
                sleep_section,
                text=text,
                variable=self.sleep_quality,
                value=value,
                font=("Arial", 14)
            ).pack(pady=5, padx=40, anchor="w")

        sleep_section.pack(pady=(0, 20), padx=40)

        # Gratitude
        gratitude_section = ctk.CTkFrame(self.content_scroll, fg_color="#1a1a1a", corner_radius=12)
        gratitude_section.grid(row=3, column=0, sticky="ew", pady=(0, 15))

        ctk.CTkLabel(
            gratitude_section,
            text="One thing you're grateful for today:",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            gratitude_section,
            text="Even something tiny counts",
            font=("Arial", 12),
            text_color="#888888"
        ).pack(pady=(0, 10))

        self.gratitude_text = ctk.CTkTextbox(
            gratitude_section,
            height=80,
            font=("Arial", 14)
        )
        self.gratitude_text.pack(fill="x", padx=40, pady=(0, 20))

        # Free reflection
        reflection_section = ctk.CTkFrame(self.content_scroll, fg_color="#1a1a1a", corner_radius=12)
        reflection_section.grid(row=4, column=0, sticky="ew", pady=(0, 15))

        ctk.CTkLabel(
            reflection_section,
            text="Anything else on your mind? (Optional)",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 10))

        self.reflection_text = ctk.CTkTextbox(
            reflection_section,
            height=120,
            font=("Arial", 14)
        )
        self.reflection_text.pack(fill="x", padx=40, pady=(0, 20))

        # Submit button
        ctk.CTkButton(
            self.content_scroll,
            text="Save Reflection",
            command=self.save_reflection,
            width=200,
            height=50,
            font=("Arial", 16),
            fg_color="#0066CC",
            hover_color="#0088EE"
        ).grid(row=5, column=0, pady=20)

    def show_completed_reflection(self, reflection):
        """Show already completed reflection"""
        completed_card = ctk.CTkFrame(self.content_scroll, fg_color="#1a1a1a", corner_radius=15)
        completed_card.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            completed_card,
            text="✅ You've already reflected today!",
            font=("Arial", 22, "bold"),
            text_color="#00AA00"
        ).pack(pady=(30, 10))

        ctk.CTkLabel(
            completed_card,
            text="Here's what you shared:",
            font=("Arial", 14),
            text_color="#888888"
        ).pack(pady=(0, 20))

        # Display reflection data
        data_frame = ctk.CTkFrame(completed_card, fg_color="#2a2a2a", corner_radius=10)
        data_frame.pack(fill="x", padx=40, pady=(0, 30))

        items = [
            ("Mood", reflection['mood'].title()),
            ("Energy", f"{reflection['energy_level']}/10"),
            ("Sleep", reflection['sleep_quality'].title()),
            ("Grateful For", reflection['gratitude']),
        ]

        if reflection.get('notes'):
            items.append(("Notes", reflection['notes']))

        for label, value in items:
            item_frame = ctk.CTkFrame(data_frame, fg_color="transparent")
            item_frame.pack(fill="x", padx=20, pady=10)

            ctk.CTkLabel(
                item_frame,
                text=f"{label}:",
                font=("Arial", 13, "bold"),
                text_color="#00AAFF"
            ).pack(anchor="w")

            ctk.CTkLabel(
                item_frame,
                text=value,
                font=("Arial", 13),
                text_color="#CCCCCC",
                wraplength=500,
                justify="left"
            ).pack(anchor="w", pady=(5, 0))

        # Show reflection history
        self.show_reflection_history()

    def show_reflection_history(self):
        """Show past reflections"""
        history_section = ctk.CTkFrame(self.content_scroll, fg_color="#1a1a1a", corner_radius=15)
        history_section.grid(row=1, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            history_section,
            text="📖 Reflection History",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 15))

        # Get past reflections
        history = self.db.get_reflection_history(limit=7)

        if len(history) > 1:  # More than just today
            for reflection in history[1:]:  # Skip today's (already shown)
                history_card = ctk.CTkFrame(history_section, fg_color="#2a2a2a", corner_radius=8)
                history_card.pack(fill="x", padx=20, pady=5)

                header = ctk.CTkFrame(history_card, fg_color="transparent")
                header.pack(fill="x", padx=15, pady=10)

                # Date
                date_str = reflection['date']
                ctk.CTkLabel(
                    header,
                    text=date_str,
                    font=("Arial", 13, "bold")
                ).pack(side="left")

                # Mood indicator
                mood_emoji = self.get_mood_emoji(reflection['mood'])
                ctk.CTkLabel(
                    header,
                    text=mood_emoji,
                    font=("Arial", 16)
                ).pack(side="right")

                # Quick summary
                summary = f"Energy: {reflection['energy_level']}/10 • Sleep: {reflection['sleep_quality']}"
                ctk.CTkLabel(
                    history_card,
                    text=summary,
                    font=("Arial", 11),
                    text_color="#888888"
                ).pack(padx=15, pady=(0, 10), anchor="w")
        else:
            ctk.CTkLabel(
                history_section,
                text="Keep reflecting to see patterns over time!",
                font=("Arial", 13),
                text_color="#888888"
            ).pack(pady=(0, 20))

    def save_reflection(self):
        """Save daily reflection"""
        mood = self.selected_mood.get()
        energy = int(self.energy_slider.get())
        sleep = self.sleep_quality.get()
        gratitude = self.gratitude_text.get("1.0", "end-1c").strip()
        notes = self.reflection_text.get("1.0", "end-1c").strip()

        if not mood:
            if self.audio.is_enabled():
                self.audio.speak("Please select how you're feeling.")
            return

        if not sleep:
            if self.audio.is_enabled():
                self.audio.speak("Please select your sleep quality.")
            return

        if not gratitude:
            if self.audio.is_enabled():
                self.audio.speak("Please share one thing you're grateful for.")
            return

        # Save to database
        self.db.save_reflection(
            date=datetime.now().strftime("%Y-%m-%d"),
            mood=mood,
            energy_level=energy,
            sleep_quality=sleep,
            gratitude=gratitude,
            notes=notes if notes else None
        )

        # Audio feedback
        if self.audio.is_enabled():
            self.audio.speak("Reflection saved. Thank you for checking in with yourself, champion.")

        # Refresh to show completed state
        for widget in self.content_scroll.winfo_children():
            widget.destroy()

        today_reflection = self.db.get_reflection_by_date(datetime.now().strftime("%Y-%m-%d"))
        self.show_completed_reflection(today_reflection)

    def get_mood_emoji(self, mood):
        """Get emoji for mood"""
        emojis = {
            "great": "😁",
            "good": "🙂",
            "okay": "😐",
            "not great": "😔",
            "struggling": "😢"
        }
        return emojis.get(mood.lower(), "😐")
