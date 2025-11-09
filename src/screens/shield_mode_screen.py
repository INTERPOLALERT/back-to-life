"""
BackToLife Shield Mode Screen
Crisis support and grounding techniques
"""
import customtkinter as ctk
import time


class ShieldModeScreen(ctk.CTkFrame):
    def __init__(self, parent, db, on_back):
        super().__init__(parent, corner_radius=0, fg_color="#0a0a0a")

        self.db = db
        self.on_back = on_back
        self.activation_id = None
        self.start_time = time.time()

        # Record activation
        self.activation_id = self.db.record_shield_activation("User initiated")

        self.grid_columnconfigure(0, weight=1)
        self.setup_ui()

    def setup_ui(self):
        """Build Shield Mode UI"""
        # Header with shield icon
        ctk.CTkLabel(
            self,
            text="🛡️",
            font=("Arial", 80)
        ).grid(row=0, column=0, pady=(40, 10))

        ctk.CTkLabel(
            self,
            text="SHIELD MODE ACTIVATED",
            font=("Arial", 32, "bold"),
            text_color="#00AAFF"
        ).grid(row=1, column=0, pady=(0, 10))

        ctk.CTkLabel(
            self,
            text="You're safe here. Take your time.",
            font=("Arial", 18),
            text_color="#888888"
        ).grid(row=2, column=0, pady=(0, 30))

        # Grounding exercise card
        grounding_card = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=15)
        grounding_card.grid(row=3, column=0, sticky="ew", pady=20, padx=40)

        ctk.CTkLabel(
            grounding_card,
            text="🧘 Grounding Exercise",
            font=("Arial", 24, "bold")
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            grounding_card,
            text="5-4-3-2-1 Method",
            font=("Arial", 16, "bold"),
            text_color="#888888"
        ).pack(pady=(0, 20))

        # Grounding steps
        steps = [
            "5 things you can see",
            "4 things you can touch",
            "3 things you can hear",
            "2 things you can smell",
            "1 thing you can taste"
        ]

        for step in steps:
            step_frame = ctk.CTkFrame(grounding_card, fg_color="#2a2a2a", corner_radius=5)
            step_frame.pack(fill="x", padx=30, pady=5)

            ctk.CTkLabel(
                step_frame,
                text=f"• {step}",
                font=("Arial", 16),
                anchor="w"
            ).pack(side="left", padx=20, pady=15)

        ctk.CTkLabel(
            grounding_card,
            text="Name each one slowly. There's no rush.",
            font=("Arial", 14, "italic"),
            text_color="#888888"
        ).pack(pady=20)

        # Breathing exercise button
        ctk.CTkButton(
            self,
            text="🫁 Breathing Exercise",
            command=self.show_breathing,
            width=300,
            height=50,
            font=("Arial", 18),
            fg_color="#006666",
            hover_color="#008888"
        ).grid(row=4, column=0, pady=10)

        # Champion reminder card
        champion_card = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=15)
        champion_card.grid(row=5, column=0, sticky="ew", pady=20, padx=40)

        ctk.CTkLabel(
            champion_card,
            text="Remember, Champion:",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 10))

        reminders = [
            "This feeling will pass",
            "You've survived every hard day before this",
            "You don't have to do anything right now",
            "Just breathe. Just exist. That's enough.",
            "The champion inside you is still there"
        ]

        for reminder in reminders:
            ctk.CTkLabel(
                champion_card,
                text=f"• {reminder}",
                font=("Arial", 14),
                anchor="w"
            ).pack(anchor="w", padx=40, pady=5)

        ctk.CTkLabel(
            champion_card,
            text="",
            font=("Arial", 1)
        ).pack(pady=10)

        # Exit button
        ctk.CTkButton(
            self,
            text="I'm Feeling Better",
            command=self.exit_shield_mode,
            width=250,
            height=50,
            font=("Arial", 16)
        ).grid(row=6, column=0, pady=30)

    def show_breathing(self):
        """Show breathing exercise in a dialog"""
        breathing_window = ctk.CTkToplevel(self)
        breathing_window.title("Breathing Exercise")
        breathing_window.geometry("500x400")
        breathing_window.transient(self.master)
        breathing_window.grab_set()

        # Center window
        breathing_window.update_idletasks()
        x = (breathing_window.winfo_screenwidth() // 2) - (500 // 2)
        y = (breathing_window.winfo_screenheight() // 2) - (400 // 2)
        breathing_window.geometry(f"500x400+{x}+{y}")

        frame = ctk.CTkFrame(breathing_window, fg_color="#0a0a0a")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        instruction_label = ctk.CTkLabel(
            frame,
            text="Breathe In",
            font=("Arial", 48, "bold"),
            text_color="#00AAFF"
        )
        instruction_label.pack(pady=50)

        count_label = ctk.CTkLabel(
            frame,
            text="4",
            font=("Arial", 72, "bold")
        )
        count_label.pack(pady=30)

        description_label = ctk.CTkLabel(
            frame,
            text="Follow the breathing pattern",
            font=("Arial", 16),
            text_color="#888888"
        )
        description_label.pack(pady=20)

        # Start breathing cycle
        self.run_breathing_cycle(instruction_label, count_label, breathing_window)

    def run_breathing_cycle(self, instruction_label, count_label, window):
        """Animate breathing exercise"""
        cycle = [
            ("Breathe In", 4, "#00AAFF"),
            ("Hold", 4, "#FFAA00"),
            ("Breathe Out", 4, "#00FF00"),
            ("Hold", 4, "#FFAA00")
        ]

        def update_cycle(cycle_index=0, count=4):
            if not window.winfo_exists():
                return

            if count == 0:
                # Move to next phase
                cycle_index = (cycle_index + 1) % len(cycle)
                instruction, duration, color = cycle[cycle_index]
                instruction_label.configure(text=instruction, text_color=color)
                count = duration
            else:
                count -= 1

            count_label.configure(text=str(count) if count > 0 else "")

            # Schedule next update
            window.after(1000, lambda: update_cycle(cycle_index, count))

        # Start the cycle
        update_cycle()

    def exit_shield_mode(self):
        """Exit Shield Mode and save duration"""
        duration = int(time.time() - self.start_time)

        # Update database with duration
        if self.activation_id:
            self.db.update_shield_duration(self.activation_id, duration, helpful_rating=0)

        # Return to home
        self.on_back()
