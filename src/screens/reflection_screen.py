"""
BackToLife Reflection Screen
Daily evening reflection and mood tracking
"""
import customtkinter as ctk
from tkinter import messagebox


class ReflectionScreen(ctk.CTkFrame):
    def __init__(self, parent, db, on_back):
        super().__init__(parent, corner_radius=0)

        self.db = db
        self.on_back = on_back

        # Reflection data
        self.mood_rating = 5
        self.energy_level = 5
        self.relationship_stress = 5

        self.grid_columnconfigure(0, weight=1)
        self.setup_ui()

    def setup_ui(self):
        """Build reflection screen UI"""
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
            text="📝 Daily Reflection",
            font=("Arial", 32, "bold")
        ).grid(row=0, column=1, padx=20)

        # Main reflection card
        reflection_card = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=15)
        reflection_card.grid(row=1, column=0, sticky="ew", pady=20)
        reflection_card.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            reflection_card,
            text="How are you feeling right now?",
            font=("Arial", 18, "bold")
        ).grid(row=0, column=0, pady=(20, 10), padx=20)

        # Mood rating
        mood_frame = self.create_rating_section(
            reflection_card,
            "Overall Mood (0-10)",
            lambda val: setattr(self, 'mood_rating', int(float(val)))
        )
        mood_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

        # Energy level
        energy_frame = self.create_rating_section(
            reflection_card,
            "Energy Level (0-10)",
            lambda val: setattr(self, 'energy_level', int(float(val)))
        )
        energy_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=10)

        # Relationship stress
        stress_frame = self.create_rating_section(
            reflection_card,
            "Relationship Stress (0-10)",
            lambda val: setattr(self, 'relationship_stress', int(float(val)))
        )
        stress_frame.grid(row=3, column=0, sticky="ew", padx=20, pady=10)

        # Text questions
        ctk.CTkLabel(
            reflection_card,
            text="What worked well today?",
            font=("Arial", 16, "bold"),
            anchor="w"
        ).grid(row=4, column=0, pady=(20, 5), padx=20, sticky="w")

        self.what_worked_entry = ctk.CTkTextbox(
            reflection_card,
            height=80,
            font=("Arial", 14)
        )
        self.what_worked_entry.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(
            reflection_card,
            text="What was difficult today?",
            font=("Arial", 16, "bold"),
            anchor="w"
        ).grid(row=6, column=0, pady=(10, 5), padx=20, sticky="w")

        self.what_was_hard_entry = ctk.CTkTextbox(
            reflection_card,
            height=80,
            font=("Arial", 14)
        )
        self.what_was_hard_entry.grid(row=7, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(
            reflection_card,
            text="One thing you're grateful for? (Optional)",
            font=("Arial", 16, "bold"),
            anchor="w"
        ).grid(row=8, column=0, pady=(10, 5), padx=20, sticky="w")

        self.grateful_entry = ctk.CTkTextbox(
            reflection_card,
            height=60,
            font=("Arial", 14)
        )
        self.grateful_entry.grid(row=9, column=0, padx=20, pady=(0, 10), sticky="ew")

        # Save button
        ctk.CTkButton(
            reflection_card,
            text="Save Reflection",
            command=self.save_reflection,
            width=250,
            height=50,
            font=("Arial", 18, "bold")
        ).grid(row=10, column=0, pady=30)

    def create_rating_section(self, parent, label_text, on_change):
        """Create a rating slider section"""
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            frame,
            text=label_text,
            font=("Arial", 14),
            anchor="w"
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))

        slider = ctk.CTkSlider(
            frame,
            from_=0,
            to=10,
            number_of_steps=10,
            command=on_change,
            width=400
        )
        slider.set(5)
        slider.grid(row=1, column=0, sticky="ew")

        # Labels for scale
        scale_frame = ctk.CTkFrame(frame, fg_color="transparent")
        scale_frame.grid(row=2, column=0, sticky="ew")
        scale_frame.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(
            scale_frame,
            text="Low",
            font=("Arial", 11),
            text_color="#888888",
            anchor="w"
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(
            scale_frame,
            text="High",
            font=("Arial", 11),
            text_color="#888888",
            anchor="e"
        ).grid(row=0, column=1, sticky="e")

        return frame

    def save_reflection(self):
        """Save reflection to database"""
        what_worked = self.what_worked_entry.get("1.0", "end-1c").strip()
        what_was_hard = self.what_was_hard_entry.get("1.0", "end-1c").strip()
        grateful_for = self.grateful_entry.get("1.0", "end-1c").strip()

        # Save to database
        self.db.save_reflection(
            mood_rating=self.mood_rating,
            what_worked=what_worked,
            what_was_hard=what_was_hard,
            grateful_for=grateful_for,
            energy_level=self.energy_level,
            relationship_stress=self.relationship_stress
        )

        # Show confirmation
        messagebox.showinfo(
            "Reflection Saved",
            "Your reflection has been saved. Thank you for taking time to reflect."
        )

        # Go back
        self.on_back()
