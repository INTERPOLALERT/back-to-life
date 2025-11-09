"""
Settings Tab - App Configuration
"""
import customtkinter as ctk


class SettingsTab(ctk.CTkFrame):
    """
    Settings with:
    - Audio preferences
    - Appearance settings
    - Notification preferences
    - Data management
    - About section
    """

    def __init__(self, parent, db, audio):
        super().__init__(parent, fg_color="transparent")

        self.db = db
        self.audio = audio

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.setup_ui()

    def setup_ui(self):
        """Build settings UI"""
        # Scrollable content
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.grid(row=0, column=0, sticky="nsew")
        scroll.grid_columnconfigure(0, weight=1)

        # Header
        header = ctk.CTkFrame(scroll, fg_color="#1a1a1a", corner_radius=15)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header,
            text="⚙️ Settings",
            font=("Arial", 28, "bold"),
            text_color="#00AAFF"
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            header,
            text="Customize your BackToLife experience",
            font=("Arial", 14),
            text_color="#888888"
        ).pack(pady=(0, 20))

        # Audio Settings
        self.show_audio_settings(scroll)

        # Appearance Settings
        self.show_appearance_settings(scroll)

        # Notification Settings
        self.show_notification_settings(scroll)

        # Data Management
        self.show_data_management(scroll)

        # About
        self.show_about(scroll)

    def show_audio_settings(self, parent):
        """Show audio preferences"""
        audio_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=12)
        audio_section.grid(row=1, column=0, sticky="ew", pady=(0, 15))

        ctk.CTkLabel(
            audio_section,
            text="🔊 Audio Settings",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15), padx=20, anchor="w")

        # Enable audio
        audio_toggle_frame = ctk.CTkFrame(audio_section, fg_color="transparent")
        audio_toggle_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            audio_toggle_frame,
            text="Enable Audio Guidance",
            font=("Arial", 14)
        ).pack(side="left")

        self.audio_switch = ctk.CTkSwitch(
            audio_toggle_frame,
            text="",
            command=self.toggle_audio
        )
        self.audio_switch.pack(side="right")

        if self.audio.is_enabled():
            self.audio_switch.select()

        # Audio speed
        speed_frame = ctk.CTkFrame(audio_section, fg_color="transparent")
        speed_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            speed_frame,
            text="Speech Speed",
            font=("Arial", 14)
        ).pack(anchor="w")

        self.speed_slider = ctk.CTkSlider(
            speed_frame,
            from_=100,
            to=200,
            number_of_steps=20,
            width=300,
            command=self.update_audio_speed
        )
        self.speed_slider.set(150)
        self.speed_slider.pack(pady=5, anchor="w")

        self.speed_label = ctk.CTkLabel(
            speed_frame,
            text="150 WPM (Normal)",
            font=("Arial", 12),
            text_color="#888888"
        )
        self.speed_label.pack(anchor="w")

        # Audio volume
        volume_frame = ctk.CTkFrame(audio_section, fg_color="transparent")
        volume_frame.pack(fill="x", padx=20, pady=(10, 20))

        ctk.CTkLabel(
            volume_frame,
            text="Volume",
            font=("Arial", 14)
        ).pack(anchor="w")

        self.volume_slider = ctk.CTkSlider(
            volume_frame,
            from_=0,
            to=100,
            number_of_steps=20,
            width=300,
            command=self.update_volume
        )
        self.volume_slider.set(90)
        self.volume_slider.pack(pady=5, anchor="w")

        self.volume_label = ctk.CTkLabel(
            volume_frame,
            text="90%",
            font=("Arial", 12),
            text_color="#888888"
        )
        self.volume_label.pack(anchor="w")

    def show_appearance_settings(self, parent):
        """Show appearance preferences"""
        appearance_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=12)
        appearance_section.grid(row=2, column=0, sticky="ew", pady=(0, 15))

        ctk.CTkLabel(
            appearance_section,
            text="🎨 Appearance",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15), padx=20, anchor="w")

        # Theme
        theme_frame = ctk.CTkFrame(appearance_section, fg_color="transparent")
        theme_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            theme_frame,
            text="Theme",
            font=("Arial", 14)
        ).pack(anchor="w", pady=(0, 5))

        theme_buttons = ctk.CTkFrame(theme_frame, fg_color="transparent")
        theme_buttons.pack(anchor="w")

        self.theme_var = ctk.StringVar(value="dark")

        ctk.CTkRadioButton(
            theme_buttons,
            text="Dark",
            variable=self.theme_var,
            value="dark",
            command=lambda: self.change_theme("dark")
        ).pack(side="left", padx=(0, 15))

        ctk.CTkRadioButton(
            theme_buttons,
            text="Light",
            variable=self.theme_var,
            value="light",
            command=lambda: self.change_theme("light")
        ).pack(side="left", padx=(0, 15))

        ctk.CTkRadioButton(
            theme_buttons,
            text="System",
            variable=self.theme_var,
            value="system",
            command=lambda: self.change_theme("system")
        ).pack(side="left")

        # Color accent
        color_frame = ctk.CTkFrame(appearance_section, fg_color="transparent")
        color_frame.pack(fill="x", padx=20, pady=(15, 20))

        ctk.CTkLabel(
            color_frame,
            text="Accent Color",
            font=("Arial", 14)
        ).pack(anchor="w", pady=(0, 5))

        colors = [
            ("Blue", "blue"),
            ("Green", "green"),
            ("Dark Blue", "dark-blue")
        ]

        self.color_var = ctk.StringVar(value="blue")

        color_buttons = ctk.CTkFrame(color_frame, fg_color="transparent")
        color_buttons.pack(anchor="w")

        for label, value in colors:
            ctk.CTkRadioButton(
                color_buttons,
                text=label,
                variable=self.color_var,
                value=value,
                command=lambda v=value: self.change_color_theme(v)
            ).pack(side="left", padx=(0, 15))

    def show_notification_settings(self, parent):
        """Show notification preferences"""
        notif_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=12)
        notif_section.grid(row=3, column=0, sticky="ew", pady=(0, 15))

        ctk.CTkLabel(
            notif_section,
            text="🔔 Notifications",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15), padx=20, anchor="w")

        # Notification toggles
        notifications = [
            ("Daily Quest Reminder", "Enable daily reminder for your quest"),
            ("Streak Warning", "Notify when streak is about to break"),
            ("Achievement Unlocked", "Celebrate when you unlock achievements"),
            ("Flashcard Review", "Remind when flashcards are due"),
            ("Reflection Reminder", "Remind to complete daily reflection")
        ]

        for title, description in notifications:
            notif_frame = ctk.CTkFrame(notif_section, fg_color="transparent")
            notif_frame.pack(fill="x", padx=20, pady=8)

            text_frame = ctk.CTkFrame(notif_frame, fg_color="transparent")
            text_frame.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(
                text_frame,
                text=title,
                font=("Arial", 13, "bold"),
                anchor="w"
            ).pack(anchor="w")

            ctk.CTkLabel(
                text_frame,
                text=description,
                font=("Arial", 11),
                text_color="#888888",
                anchor="w"
            ).pack(anchor="w")

            ctk.CTkSwitch(
                notif_frame,
                text=""
            ).pack(side="right")

        notif_section.pack(pady=(0, 20), padx=20)

    def show_data_management(self, parent):
        """Show data management options"""
        data_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=12)
        data_section.grid(row=4, column=0, sticky="ew", pady=(0, 15))

        ctk.CTkLabel(
            data_section,
            text="💾 Data Management",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15), padx=20, anchor="w")

        # Data location
        location_frame = ctk.CTkFrame(data_section, fg_color="#2a2a2a", corner_radius=8)
        location_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            location_frame,
            text="Data Location",
            font=("Arial", 13, "bold")
        ).pack(pady=(12, 5), padx=15, anchor="w")

        ctk.CTkLabel(
            location_frame,
            text=self.db.db_path,
            font=("Arial", 11),
            text_color="#888888"
        ).pack(pady=(0, 12), padx=15, anchor="w")

        # Data actions
        action_buttons = ctk.CTkFrame(data_section, fg_color="transparent")
        action_buttons.pack(padx=20, pady=(10, 20))

        ctk.CTkButton(
            action_buttons,
            text="📤 Export Data",
            command=self.export_data,
            width=150,
            height=40,
            font=("Arial", 13),
            fg_color="#0066CC",
            hover_color="#0088EE"
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            action_buttons,
            text="📥 Import Data",
            command=self.import_data,
            width=150,
            height=40,
            font=("Arial", 13),
            fg_color="#00AA00",
            hover_color="#00CC00"
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            action_buttons,
            text="🗑️ Clear All Data",
            command=self.clear_data_warning,
            width=150,
            height=40,
            font=("Arial", 13),
            fg_color="#CC0000",
            hover_color="#EE0000"
        ).pack(side="left", padx=5)

    def show_about(self, parent):
        """Show about section"""
        about_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=12)
        about_section.grid(row=5, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            about_section,
            text="ℹ️ About BackToLife",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15), padx=20, anchor="w")

        info_frame = ctk.CTkFrame(about_section, fg_color="#2a2a2a", corner_radius=8)
        info_frame.pack(fill="x", padx=20, pady=(0, 20))

        about_text = """BackToLife - Your Complete Life Operating System

Version: 1.0.0

A comprehensive digital therapeutic app designed to support
individuals with ADHD, depression, executive dysfunction, and
related challenges.

Features:
• Evidence-based quest system
• Audio-guided learning
• Flashcard-based education
• Interactive skill-building
• Pattern recognition and insights
• Crisis support tools
• Comprehensive tracking

This app uses local storage to protect your privacy.
Your data never leaves your device.

© 2024 BackToLife. All rights reserved."""

        ctk.CTkLabel(
            info_frame,
            text=about_text,
            font=("Arial", 12),
            justify="left",
            wraplength=650
        ).pack(pady=20, padx=20)

    def toggle_audio(self):
        """Toggle audio on/off"""
        enabled = self.audio.toggle()
        if enabled and self.audio.is_enabled():
            self.audio.speak("Audio guidance enabled.")

    def update_audio_speed(self, value):
        """Update audio speed"""
        speed = int(value)
        self.speed_label.configure(text=f"{speed} WPM {'(Normal)' if speed == 150 else ''}")
        self.audio.set_speed(speed)

    def update_volume(self, value):
        """Update audio volume"""
        volume = int(value)
        self.volume_label.configure(text=f"{volume}%")
        self.audio.set_volume(volume / 100)

    def change_theme(self, theme):
        """Change app theme"""
        ctk.set_appearance_mode(theme)
        if self.audio.is_enabled():
            self.audio.speak(f"{theme.title()} theme applied.")

    def change_color_theme(self, color):
        """Change color theme"""
        try:
            ctk.set_default_color_theme(color)
            if self.audio.is_enabled():
                self.audio.speak(f"{color.title()} color theme applied. Restart the app to see changes.")
        except:
            pass

    def export_data(self):
        """Export user data"""
        if self.audio.is_enabled():
            self.audio.speak("Data export feature coming soon.")
        # TODO: Implement data export

    def import_data(self):
        """Import user data"""
        if self.audio.is_enabled():
            self.audio.speak("Data import feature coming soon.")
        # TODO: Implement data import

    def clear_data_warning(self):
        """Show warning before clearing data"""
        warning = ctk.CTkToplevel(self)
        warning.title("Clear All Data")
        warning.geometry("500x300")

        ctk.CTkLabel(
            warning,
            text="⚠️ WARNING",
            font=("Arial", 28, "bold"),
            text_color="#CC0000"
        ).pack(pady=20)

        ctk.CTkLabel(
            warning,
            text="This will permanently delete all your data:",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        data_list = """• All quest history
• Progress and XP
• Reflections
• Flashcard reviews
• All settings

This action CANNOT be undone!"""

        ctk.CTkLabel(
            warning,
            text=data_list,
            font=("Arial", 13),
            justify="left"
        ).pack(pady=15)

        button_frame = ctk.CTkFrame(warning, fg_color="transparent")
        button_frame.pack(pady=20)

        ctk.CTkButton(
            button_frame,
            text="Cancel",
            command=warning.destroy,
            width=150,
            height=45,
            font=("Arial", 14),
            fg_color="#666666",
            hover_color="#888888"
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            button_frame,
            text="DELETE ALL DATA",
            command=lambda: self.clear_all_data(warning),
            width=200,
            height=45,
            font=("Arial", 14, "bold"),
            fg_color="#CC0000",
            hover_color="#EE0000"
        ).pack(side="left", padx=10)

    def clear_all_data(self, warning_window):
        """Actually clear all data"""
        self.db.clear_all_data()
        warning_window.destroy()

        if self.audio.is_enabled():
            self.audio.speak("All data has been cleared. The app will now restart.")

        # TODO: Restart app or reset to initial state
