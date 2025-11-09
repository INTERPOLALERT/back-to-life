"""
Guides Tab - How-To Library
Practical guides for common challenges
"""
import customtkinter as ctk


class GuidesTab(ctk.CTkFrame):
    """
    Guides library with:
    - How-to guides for common situations
    - Step-by-step walkthroughs
    - Searchable library
    - Audio support for all guides
    """

    def __init__(self, parent, db, audio):
        super().__init__(parent, fg_color="transparent")

        self.db = db
        self.audio = audio
        self.current_category = "all"

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.setup_ui()

    def setup_ui(self):
        """Build guides UI"""
        # Header
        header = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=15)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header,
            text="📖 How-To Guides",
            font=("Arial", 28, "bold"),
            text_color="#00AAFF"
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            header,
            text="Practical step-by-step help for real situations",
            font=("Arial", 14),
            text_color="#888888"
        ).pack(pady=(0, 15))

        # Search bar
        search_frame = ctk.CTkFrame(header, fg_color="transparent")
        search_frame.pack(pady=(0, 15))

        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Search guides...",
            width=400,
            height=40,
            font=("Arial", 14)
        )
        self.search_entry.pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            search_frame,
            text="🔍 Search",
            command=self.search_guides,
            width=100,
            height=40,
            font=("Arial", 13)
        ).pack(side="left")

        # Category filter
        cat_frame = ctk.CTkFrame(header, fg_color="transparent")
        cat_frame.pack(pady=(5, 20))

        categories = [
            ("All", "all"),
            ("Tasks", "tasks"),
            ("Social", "social"),
            ("Self-Care", "selfcare"),
            ("Crisis", "crisis")
        ]

        self.cat_buttons = {}
        for i, (label, cat_id) in enumerate(categories):
            btn = ctk.CTkButton(
                cat_frame,
                text=label,
                command=lambda c=cat_id: self.filter_category(c),
                width=100,
                height=35,
                font=("Arial", 12),
                fg_color="#2a2a2a",
                hover_color="#3a3a3a"
            )
            btn.grid(row=0, column=i, padx=5)
            self.cat_buttons[cat_id] = btn

        self.cat_buttons["all"].configure(fg_color="#0066CC")

        # Guides list
        self.guides_scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        self.guides_scroll.grid(row=1, column=0, sticky="nsew")
        self.guides_scroll.grid_columnconfigure(0, weight=1)

        self.display_guides()

    def filter_category(self, category):
        """Filter guides by category"""
        self.current_category = category

        # Update button states
        for cat_id, btn in self.cat_buttons.items():
            if cat_id == category:
                btn.configure(fg_color="#0066CC")
            else:
                btn.configure(fg_color="#2a2a2a")

        self.display_guides()

    def search_guides(self):
        """Search guides"""
        query = self.search_entry.get().lower()
        if query:
            self.display_guides(search_query=query)

    def display_guides(self, search_query=None):
        """Display guides list"""
        # Clear existing
        for widget in self.guides_scroll.winfo_children():
            widget.destroy()

        guides = self.get_all_guides()

        # Filter by category
        if self.current_category != "all":
            guides = [g for g in guides if g['category'] == self.current_category]

        # Filter by search
        if search_query:
            guides = [g for g in guides if
                     search_query in g['title'].lower() or
                     search_query in g['description'].lower()]

        if not guides:
            ctk.CTkLabel(
                self.guides_scroll,
                text="No guides found.",
                font=("Arial", 14),
                text_color="#888888"
            ).pack(pady=40)
            return

        # Display guides
        for i, guide in enumerate(guides):
            self.create_guide_card(guide, i)

    def create_guide_card(self, guide, row):
        """Create guide card"""
        card = ctk.CTkFrame(
            self.guides_scroll,
            fg_color="#1a1a1a",
            corner_radius=12
        )
        card.grid(row=row, column=0, sticky="ew", pady=10)

        # Header
        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=15)

        ctk.CTkLabel(
            header,
            text=guide['icon'],
            font=("Arial", 28)
        ).pack(side="left", padx=(0, 15))

        info_frame = ctk.CTkFrame(header, fg_color="transparent")
        info_frame.pack(side="left", fill="x", expand=True)

        ctk.CTkLabel(
            info_frame,
            text=guide['title'],
            font=("Arial", 17, "bold"),
            anchor="w"
        ).pack(anchor="w")

        ctk.CTkLabel(
            info_frame,
            text=f"{guide['steps']} steps • {guide['time']} min",
            font=("Arial", 12),
            text_color="#888888",
            anchor="w"
        ).pack(anchor="w")

        # Description
        ctk.CTkLabel(
            card,
            text=guide['description'],
            font=("Arial", 13),
            text_color="#CCCCCC",
            wraplength=700,
            justify="left",
            anchor="w"
        ).pack(fill="x", padx=20, pady=(0, 15))

        # Action buttons
        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(pady=(0, 15))

        ctk.CTkButton(
            btn_frame,
            text="📖 Read Guide",
            command=lambda g=guide: self.open_guide(g),
            width=140,
            height=40,
            font=("Arial", 13),
            fg_color="#0066CC",
            hover_color="#0088EE"
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            btn_frame,
            text="🔊 Listen to Guide",
            command=lambda g=guide: self.read_guide_aloud(g),
            width=160,
            height=40,
            font=("Arial", 13),
            fg_color="#00AA00",
            hover_color="#00CC00"
        ).pack(side="left", padx=5)

    def get_all_guides(self):
        """Get all available guides"""
        return [
            # Task Guides
            {
                'id': 'start_overwhelming_task',
                'title': 'How to Start an Overwhelming Task',
                'icon': '🎯',
                'category': 'tasks',
                'description': 'When a task feels impossible to start, use this step-by-step approach to break through the paralysis.',
                'steps': 6,
                'time': 10,
                'content': self.get_guide_content('start_overwhelming_task')
            },
            {
                'id': 'finish_started_task',
                'title': 'How to Finish What You Started',
                'icon': '✅',
                'category': 'tasks',
                'description': 'Strategies for completing tasks when your brain wants to jump to something new.',
                'steps': 5,
                'time': 8,
                'content': self.get_guide_content('finish_started_task')
            },
            {
                'id': 'organize_space',
                'title': 'How to Organize a Messy Space',
                'icon': '🧹',
                'category': 'tasks',
                'description': 'ADHD-friendly approach to cleaning and organizing without getting overwhelmed.',
                'steps': 7,
                'time': 15,
                'content': self.get_guide_content('organize_space')
            },

            # Social Guides
            {
                'id': 'difficult_conversation',
                'title': 'How to Have a Difficult Conversation',
                'icon': '💬',
                'category': 'social',
                'description': 'Prepare for and navigate challenging conversations with confidence.',
                'steps': 8,
                'time': 12,
                'content': self.get_guide_content('difficult_conversation')
            },
            {
                'id': 'set_boundary',
                'title': 'How to Set a Boundary',
                'icon': '🛡️',
                'category': 'social',
                'description': 'Step-by-step guide to setting and maintaining healthy boundaries.',
                'steps': 6,
                'time': 10,
                'content': self.get_guide_content('set_boundary')
            },
            {
                'id': 'apologize_effectively',
                'title': 'How to Apologize Effectively',
                'icon': '🤝',
                'category': 'social',
                'description': 'Making genuine apologies that repair relationships.',
                'steps': 5,
                'time': 7,
                'content': self.get_guide_content('apologize_effectively')
            },

            # Self-Care Guides
            {
                'id': 'morning_routine',
                'title': 'How to Build a Morning Routine',
                'icon': '☀️',
                'category': 'selfcare',
                'description': 'Create a sustainable morning routine that works with your brain.',
                'steps': 6,
                'time': 10,
                'content': self.get_guide_content('morning_routine')
            },
            {
                'id': 'handle_bad_day',
                'title': 'How to Handle a Really Bad Day',
                'icon': '🌧️',
                'category': 'selfcare',
                'description': 'Survival strategies for when everything feels terrible.',
                'steps': 7,
                'time': 12,
                'content': self.get_guide_content('handle_bad_day')
            },
            {
                'id': 'sleep_routine',
                'title': 'How to Fix Your Sleep',
                'icon': '😴',
                'category': 'selfcare',
                'description': 'Science-based approach to improving sleep with ADHD and depression.',
                'steps': 8,
                'time': 15,
                'content': self.get_guide_content('sleep_routine')
            },

            # Crisis Guides
            {
                'id': 'crisis_moment',
                'title': 'What to Do in a Crisis Moment',
                'icon': '🆘',
                'category': 'crisis',
                'description': 'Immediate steps when you\'re in emotional crisis.',
                'steps': 5,
                'time': 5,
                'content': self.get_guide_content('crisis_moment')
            },
            {
                'id': 'panic_attack',
                'title': 'How to Handle a Panic Attack',
                'icon': '😰',
                'category': 'crisis',
                'description': 'Evidence-based techniques to manage panic attacks.',
                'steps': 6,
                'time': 8,
                'content': self.get_guide_content('panic_attack')
            },
            {
                'id': 'shutdown_recovery',
                'title': 'How to Recover from Shutdown',
                'icon': '🔋',
                'category': 'crisis',
                'description': 'Gentle steps to come back online after emotional shutdown.',
                'steps': 5,
                'time': 10,
                'content': self.get_guide_content('shutdown_recovery')
            }
        ]

    def get_guide_content(self, guide_id):
        """Get guide content (placeholder - would be full content)"""
        # This would contain the full step-by-step content
        # For now, return placeholder
        return [
            {"step": 1, "title": "Step 1", "content": "Content here..."},
            {"step": 2, "title": "Step 2", "content": "Content here..."},
        ]

    def open_guide(self, guide):
        """Open guide in reader"""
        if self.audio.is_enabled():
            self.audio.speak(f"Opening guide: {guide['title']}")

        # Create guide window
        guide_window = ctk.CTkToplevel(self)
        guide_window.title(guide['title'])
        guide_window.geometry("800x600")

        # Header
        header = ctk.CTkFrame(guide_window, fg_color="#1a1a1a")
        header.pack(fill="x", pady=(0, 20))

        ctk.CTkLabel(
            header,
            text=f"{guide['icon']} {guide['title']}",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            header,
            text=guide['description'],
            font=("Arial", 14),
            text_color="#AAAAAA",
            wraplength=700
        ).pack(pady=(0, 20), padx=40)

        # Content area
        content_scroll = ctk.CTkScrollableFrame(guide_window)
        content_scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Display steps
        for step_data in guide['content']:
            step_card = ctk.CTkFrame(content_scroll, fg_color="#2a2a2a", corner_radius=10)
            step_card.pack(fill="x", pady=10)

            ctk.CTkLabel(
                step_card,
                text=step_data['title'],
                font=("Arial", 16, "bold"),
                text_color="#00AAFF"
            ).pack(pady=(15, 5), padx=20, anchor="w")

            ctk.CTkLabel(
                step_card,
                text=step_data['content'],
                font=("Arial", 13),
                text_color="#CCCCCC",
                wraplength=700,
                justify="left",
                anchor="w"
            ).pack(pady=(0, 15), padx=20, anchor="w")

    def read_guide_aloud(self, guide):
        """Read guide using text-to-speech"""
        if not self.audio.is_enabled():
            self.audio.toggle()

        # Read title
        self.audio.speak(f"{guide['title']}. {guide['description']}")

        # TODO: Read full guide content
