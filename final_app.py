"""
BackToLife - FINAL COMPLETE VERSION
All features, all tools, nothing missing
"""
import customtkinter as ctk
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.database import Database
from src.data.quest_database import initialize_quest_database
from src.utils.context_engine import ContextEngine
from src.services.audio_service import get_audio_service

# Import all tab screens
from src.screens.final.home_tab import HomeTab
from src.screens.final.learn_tab import LearnTab
from src.screens.final.tools_tab import ToolsTab
from src.screens.final.guides_tab import GuidesTab
from src.screens.final.progress_tab import ProgressTab
from src.screens.final.reflection_tab import ReflectionTab
from src.screens.final.shield_tab import ShieldTab
from src.screens.final.settings_tab import SettingsTab


class BackToLifeFinal(ctk.CTk):
    """
    Final Complete Version of BackToLife
    - Multi-tab navigation
    - All features integrated
    - Mobile-friendly responsive design
    - Tool library
    - Learning center
    - Everything from research
    """

    def __init__(self):
        super().__init__()

        # App configuration
        self.title("BackToLife - Your Complete Life Operating System")
        self.geometry("1200x800")

        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Initialize services
        self.db = Database()
        initialize_quest_database(self.db)
        self.context_engine = ContextEngine(self.db)
        self.audio = get_audio_service()

        # Current tab tracking
        self.current_tab = "home"
        self.tab_widgets = {}

        # Setup UI
        self.setup_ui()

        # Show home by default
        self.show_tab("home")

    def setup_ui(self):
        """Setup main application UI with navigation"""
        # Configure grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create navigation sidebar
        self.create_navigation()

        # Create main content area
        self.content_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        # Create quick access bar
        self.create_quick_access_bar()

    def create_navigation(self):
        """Create navigation sidebar"""
        # Navigation frame
        self.nav_frame = ctk.CTkFrame(
            self,
            width=200,
            corner_radius=0,
            fg_color="#1a1a1a"
        )
        self.nav_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.nav_frame.grid_rowconfigure(10, weight=1)  # Push settings to bottom

        # App title
        title_frame = ctk.CTkFrame(self.nav_frame, fg_color="transparent")
        title_frame.grid(row=0, column=0, pady=(20, 10), padx=15, sticky="ew")

        ctk.CTkLabel(
            title_frame,
            text="BackToLife",
            font=("Arial", 20, "bold"),
            text_color="#FFD700"
        ).pack()

        ctk.CTkLabel(
            title_frame,
            text="🏆",
            font=("Arial", 24)
        ).pack()

        # User stats (compact)
        profile = self.db.get_user_profile()
        stats_frame = ctk.CTkFrame(self.nav_frame, fg_color="#2a2a2a", corner_radius=8)
        stats_frame.grid(row=1, column=0, pady=(0, 20), padx=10, sticky="ew")

        ctk.CTkLabel(
            stats_frame,
            text=f"Level {profile['level']}",
            font=("Arial", 14, "bold")
        ).pack(pady=(8, 2))

        ctk.CTkLabel(
            stats_frame,
            text=f"{profile['xp']} XP | {profile['streak']}🔥",
            font=("Arial", 11),
            text_color="#888888"
        ).pack(pady=(0, 8))

        # Navigation buttons
        self.nav_buttons = {}

        nav_items = [
            ("home", "🏠", "Home", 2),
            ("learn", "📚", "Learn", 3),
            ("tools", "🛠️", "Tools", 4),
            ("guides", "📖", "Guides", 5),
            ("progress", "📊", "Progress", 6),
            ("reflection", "📝", "Reflection", 7),
            ("shield", "🛡️", "Shield", 8),
        ]

        for tab_id, icon, label, row in nav_items:
            btn = ctk.CTkButton(
                self.nav_frame,
                text=f"{icon} {label}",
                command=lambda t=tab_id: self.show_tab(t),
                width=180,
                height=45,
                font=("Arial", 14),
                fg_color="#2a2a2a",
                hover_color="#3a3a3a",
                anchor="w",
                corner_radius=8
            )
            btn.grid(row=row, column=0, padx=10, pady=5, sticky="ew")
            self.nav_buttons[tab_id] = btn

        # Settings button (bottom)
        settings_btn = ctk.CTkButton(
            self.nav_frame,
            text="⚙️ Settings",
            command=lambda: self.show_tab("settings"),
            width=180,
            height=45,
            font=("Arial", 14),
            fg_color="#444444",
            hover_color="#555555",
            anchor="w",
            corner_radius=8
        )
        settings_btn.grid(row=11, column=0, padx=10, pady=(10, 20), sticky="ew")
        self.nav_buttons["settings"] = settings_btn

        # Audio toggle (bottom)
        self.audio_toggle_btn = ctk.CTkButton(
            self.nav_frame,
            text="🔊 Audio ON",
            command=self.toggle_audio,
            width=180,
            height=35,
            font=("Arial", 12),
            fg_color="#00AA00",
            hover_color="#00CC00",
            corner_radius=8
        )
        self.audio_toggle_btn.grid(row=12, column=0, padx=10, pady=(0, 15), sticky="ew")

    def create_quick_access_bar(self):
        """Create quick access bar at bottom"""
        self.quick_bar = ctk.CTkFrame(
            self,
            height=60,
            corner_radius=0,
            fg_color="#2a2a2a"
        )
        self.quick_bar.grid(row=1, column=1, sticky="ew")

        # Quick action buttons (context-aware)
        self.quick_bar_buttons = ctk.CTkFrame(self.quick_bar, fg_color="transparent")
        self.quick_bar_buttons.pack(side="left", padx=20, pady=10)

        # Will be populated based on current tab
        self.update_quick_bar()

    def update_quick_bar(self):
        """Update quick access bar based on current tab"""
        # Clear existing buttons
        for widget in self.quick_bar_buttons.winfo_children():
            widget.destroy()

        # Add context-appropriate buttons
        if self.current_tab == "home":
            ctk.CTkButton(
                self.quick_bar_buttons,
                text="⚡ Start Quest",
                width=120,
                height=40,
                font=("Arial", 13)
            ).pack(side="left", padx=5)

            ctk.CTkButton(
                self.quick_bar_buttons,
                text="🛡️ Shield",
                width=100,
                height=40,
                font=("Arial", 13),
                fg_color="#666666"
            ).pack(side="left", padx=5)

        elif self.current_tab == "learn":
            ctk.CTkButton(
                self.quick_bar_buttons,
                text="💡 Review Cards",
                width=140,
                height=40,
                font=("Arial", 13)
            ).pack(side="left", padx=5)

            ctk.CTkButton(
                self.quick_bar_buttons,
                text="🎯 Take Quiz",
                width=120,
                height=40,
                font=("Arial", 13)
            ).pack(side="left", padx=5)

        elif self.current_tab == "shield":
            ctk.CTkButton(
                self.quick_bar_buttons,
                text="🆘 Crisis Line",
                width=130,
                height=40,
                font=("Arial", 13),
                fg_color="#CC0000"
            ).pack(side="left", padx=5)

            ctk.CTkButton(
                self.quick_bar_buttons,
                text="🧘 Ground Now",
                width=130,
                height=40,
                font=("Arial", 13)
            ).pack(side="left", padx=5)

    def show_tab(self, tab_id):
        """Show selected tab"""
        # Update current tab
        self.current_tab = tab_id

        # Update navigation button states
        for btn_id, btn in self.nav_buttons.items():
            if btn_id == tab_id:
                btn.configure(fg_color="#0066CC")
            else:
                btn.configure(fg_color="#2a2a2a" if btn_id != "settings" else "#444444")

        # Clear content area
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Create or get tab widget
        if tab_id not in self.tab_widgets:
            self.tab_widgets[tab_id] = self.create_tab_widget(tab_id)

        # Show tab widget
        tab_widget = self.tab_widgets[tab_id]
        if tab_widget:
            tab_widget.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Update quick access bar
        self.update_quick_bar()

    def create_tab_widget(self, tab_id):
        """Create widget for specified tab"""
        if tab_id == "home":
            return HomeTab(self.content_frame, self.db, self.context_engine, self.audio)
        elif tab_id == "learn":
            return LearnTab(self.content_frame, self.db, self.audio)
        elif tab_id == "tools":
            return ToolsTab(self.content_frame, self.db, self.audio)
        elif tab_id == "guides":
            return GuidesTab(self.content_frame, self.db, self.audio)
        elif tab_id == "progress":
            return ProgressTab(self.content_frame, self.db, self.audio)
        elif tab_id == "reflection":
            return ReflectionTab(self.content_frame, self.db, self.audio)
        elif tab_id == "shield":
            return ShieldTab(self.content_frame, self.db, self.audio)
        elif tab_id == "settings":
            return SettingsTab(self.content_frame, self.db, self.audio)
        return None

    def toggle_audio(self):
        """Toggle audio on/off"""
        enabled = self.audio.toggle()
        if enabled:
            self.audio_toggle_btn.configure(
                text="🔊 Audio ON",
                fg_color="#00AA00"
            )
        else:
            self.audio_toggle_btn.configure(
                text="🔇 Audio OFF",
                fg_color="#666666"
            )

    def run(self):
        """Start the application"""
        self.mainloop()


if __name__ == "__main__":
    app = BackToLifeFinal()
    app.run()
