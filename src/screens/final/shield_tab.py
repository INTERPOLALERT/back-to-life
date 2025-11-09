"""
Shield Tab - Crisis Support and Emergency Tools
"""
import customtkinter as ctk
from datetime import datetime


class ShieldTab(ctk.CTkFrame):
    """
    Crisis support with:
    - Emergency contacts
    - Crisis hotlines
    - Grounding exercises
    - Safety plan
    - Distress tolerance tools
    """

    def __init__(self, parent, db, audio):
        super().__init__(parent, fg_color="transparent")

        self.db = db
        self.audio = audio

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.setup_ui()

    def setup_ui(self):
        """Build shield UI"""
        # Header
        header = ctk.CTkFrame(self, fg_color="#CC0000", corner_radius=15)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header,
            text="🛡️ Shield Mode",
            font=("Arial", 28, "bold"),
            text_color="#FFFFFF"
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            header,
            text="You're safe here. Take what you need.",
            font=("Arial", 14),
            text_color="#FFCCCC"
        ).pack(pady=(0, 20))

        # Main content
        scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        scroll.grid(row=1, column=0, sticky="nsew")
        scroll.grid_columnconfigure(0, weight=1)

        # Crisis hotlines (always visible at top)
        self.show_crisis_hotlines(scroll)

        # Quick grounding
        self.show_quick_grounding(scroll)

        # Distress tolerance tools
        self.show_distress_tools(scroll)

        # Safety plan
        self.show_safety_plan(scroll)

        # Track shield activation
        self.db.log_shield_activation()

    def show_crisis_hotlines(self, parent):
        """Show emergency contacts and hotlines"""
        crisis_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        crisis_section.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            crisis_section,
            text="🆘 Emergency Support",
            font=("Arial", 22, "bold"),
            text_color="#FF6600"
        ).pack(pady=(20, 15))

        # Crisis hotlines
        hotlines = [
            {
                'name': '988 Suicide & Crisis Lifeline',
                'number': '988',
                'description': 'Call or text 988 • Available 24/7',
                'color': '#CC0000'
            },
            {
                'name': 'Crisis Text Line',
                'number': 'Text HOME to 741741',
                'description': 'Free 24/7 support via text',
                'color': '#0066CC'
            },
            {
                'name': 'SAMHSA Helpline',
                'number': '1-800-662-4357',
                'description': 'Substance abuse and mental health services',
                'color': '#00AA00'
            }
        ]

        for hotline in hotlines:
            hotline_card = ctk.CTkFrame(
                crisis_section,
                fg_color=hotline['color'],
                corner_radius=10
            )
            hotline_card.pack(fill="x", padx=20, pady=8)

            ctk.CTkLabel(
                hotline_card,
                text=hotline['name'],
                font=("Arial", 16, "bold"),
                text_color="#FFFFFF"
            ).pack(pady=(15, 5), padx=20, anchor="w")

            ctk.CTkLabel(
                hotline_card,
                text=hotline['number'],
                font=("Arial", 20, "bold"),
                text_color="#FFFFFF"
            ).pack(pady=5, padx=20, anchor="w")

            ctk.CTkLabel(
                hotline_card,
                text=hotline['description'],
                font=("Arial", 12),
                text_color="#FFFFFF"
            ).pack(pady=(0, 15), padx=20, anchor="w")

        # Important note
        note_frame = ctk.CTkFrame(crisis_section, fg_color="#2a2a2a", corner_radius=8)
        note_frame.pack(fill="x", padx=20, pady=(10, 20))

        ctk.CTkLabel(
            note_frame,
            text="💙 If you're in immediate danger, call 911",
            font=("Arial", 14, "bold"),
            text_color="#FFFFFF"
        ).pack(pady=15)

    def show_quick_grounding(self, parent):
        """Show quick grounding exercises"""
        grounding_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        grounding_section.grid(row=1, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            grounding_section,
            text="🌊 Quick Grounding",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 15))

        ctk.CTkLabel(
            grounding_section,
            text="Bring yourself back to the present moment",
            font=("Arial", 13),
            text_color="#888888"
        ).pack(pady=(0, 15))

        # Grounding buttons
        exercises = [
            {
                'name': '5-4-3-2-1 Grounding',
                'icon': '👁️',
                'description': 'Use your senses to anchor yourself',
                'action': self.start_54321
            },
            {
                'name': 'Box Breathing',
                'icon': '🫁',
                'description': '4-4-4-4 breathing pattern',
                'action': self.start_box_breathing
            },
            {
                'name': 'Ice Water Dive',
                'icon': '🧊',
                'description': 'Activate your dive reflex (quick reset)',
                'action': self.show_ice_water
            },
            {
                'name': 'Progressive Muscle Relaxation',
                'icon': '💪',
                'description': 'Tense and release each muscle group',
                'action': self.start_pmr
            }
        ]

        for exercise in exercises:
            card = ctk.CTkFrame(grounding_section, fg_color="#2a2a2a", corner_radius=10)
            card.pack(fill="x", padx=20, pady=8)

            header = ctk.CTkFrame(card, fg_color="transparent")
            header.pack(fill="x", padx=15, pady=12)

            ctk.CTkLabel(
                header,
                text=exercise['icon'],
                font=("Arial", 24)
            ).pack(side="left", padx=(0, 15))

            info_frame = ctk.CTkFrame(header, fg_color="transparent")
            info_frame.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(
                info_frame,
                text=exercise['name'],
                font=("Arial", 15, "bold"),
                anchor="w"
            ).pack(anchor="w")

            ctk.CTkLabel(
                info_frame,
                text=exercise['description'],
                font=("Arial", 12),
                text_color="#AAAAAA",
                anchor="w"
            ).pack(anchor="w")

            ctk.CTkButton(
                header,
                text="Start",
                command=exercise['action'],
                width=100,
                height=35,
                font=("Arial", 13),
                fg_color="#0066CC",
                hover_color="#0088EE"
            ).pack(side="right")

    def show_distress_tools(self, parent):
        """Show distress tolerance tools"""
        distress_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        distress_section.grid(row=2, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            distress_section,
            text="🛠️ Distress Tolerance Tools",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 15))

        tools = [
            {
                'name': 'TIPP Skills',
                'description': 'Temperature, Intense exercise, Paced breathing, Progressive relaxation',
                'icon': '🧊'
            },
            {
                'name': 'Self-Soothe',
                'description': 'Use your 5 senses to calm yourself',
                'icon': '🌸'
            },
            {
                'name': 'IMPROVE the Moment',
                'description': 'Imagery, Meaning, Prayer, Relaxation, One thing, Vacation, Encouragement',
                'icon': '✨'
            },
            {
                'name': 'Distraction',
                'description': 'Activities, Contributing, Comparisons, Emotions, Push away, Thoughts, Sensations',
                'icon': '🎯'
            }
        ]

        for tool in tools:
            card = ctk.CTkFrame(distress_section, fg_color="#2a2a2a", corner_radius=8)
            card.pack(fill="x", padx=20, pady=6)

            header = ctk.CTkFrame(card, fg_color="transparent")
            header.pack(fill="x", padx=15, pady=12)

            ctk.CTkLabel(
                header,
                text=tool['icon'],
                font=("Arial", 20)
            ).pack(side="left", padx=(0, 12))

            info_frame = ctk.CTkFrame(header, fg_color="transparent")
            info_frame.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(
                info_frame,
                text=tool['name'],
                font=("Arial", 14, "bold"),
                anchor="w"
            ).pack(anchor="w")

            ctk.CTkLabel(
                info_frame,
                text=tool['description'],
                font=("Arial", 11),
                text_color="#AAAAAA",
                wraplength=500,
                justify="left",
                anchor="w"
            ).pack(anchor="w")

    def show_safety_plan(self, parent):
        """Show personalized safety plan"""
        safety_section = ctk.CTkFrame(parent, fg_color="#1a1a1a", corner_radius=15)
        safety_section.grid(row=3, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            safety_section,
            text="📋 Your Safety Plan",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 15))

        # Safety plan steps
        steps = [
            {
                'number': 1,
                'title': 'Recognize warning signs',
                'examples': ['Feeling hopeless', 'Isolating from others', 'Increase in substance use']
            },
            {
                'number': 2,
                'title': 'Use coping strategies',
                'examples': ['Grounding exercises', 'Call a friend', 'Go for a walk']
            },
            {
                'number': 3,
                'title': 'Contact people who help',
                'examples': ['Therapist', 'Trusted friend', 'Family member']
            },
            {
                'number': 4,
                'title': 'Contact crisis services',
                'examples': ['988 Lifeline', 'Crisis Text Line', 'Local emergency room']
            },
            {
                'number': 5,
                'title': 'Make environment safe',
                'examples': ['Remove means of harm', 'Stay with someone', 'Go to safe location']
            }
        ]

        for step in steps:
            step_card = ctk.CTkFrame(safety_section, fg_color="#2a2a2a", corner_radius=8)
            step_card.pack(fill="x", padx=20, pady=6)

            header = ctk.CTkFrame(step_card, fg_color="transparent")
            header.pack(fill="x", padx=15, pady=12)

            # Step number
            num_label = ctk.CTkLabel(
                header,
                text=str(step['number']),
                font=("Arial", 20, "bold"),
                width=40,
                height=40,
                fg_color="#0066CC",
                corner_radius=20
            )
            num_label.pack(side="left", padx=(0, 12))

            # Step content
            content_frame = ctk.CTkFrame(header, fg_color="transparent")
            content_frame.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(
                content_frame,
                text=step['title'].upper(),
                font=("Arial", 13, "bold"),
                text_color="#00AAFF",
                anchor="w"
            ).pack(anchor="w")

            examples_text = " • ".join(step['examples'])
            ctk.CTkLabel(
                content_frame,
                text=examples_text,
                font=("Arial", 11),
                text_color="#AAAAAA",
                wraplength=500,
                justify="left",
                anchor="w"
            ).pack(anchor="w", pady=(3, 0))

        # Customize button
        ctk.CTkButton(
            safety_section,
            text="Customize Safety Plan",
            command=self.customize_safety_plan,
            width=200,
            height=40,
            font=("Arial", 14),
            fg_color="#0066CC",
            hover_color="#0088EE"
        ).pack(pady=20)

    def start_54321(self):
        """Start 5-4-3-2-1 grounding"""
        if self.audio.is_enabled():
            self.audio.speak("Starting 5-4-3-2-1 grounding exercise. Let's bring you back to the present moment.")

        # Create grounding window
        window = ctk.CTkToplevel(self)
        window.title("5-4-3-2-1 Grounding")
        window.geometry("600x500")

        ctk.CTkLabel(
            window,
            text="🌊 5-4-3-2-1 Grounding",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        scroll = ctk.CTkScrollableFrame(window)
        scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        steps = [
            ("5 things you can SEE", "Look around. Name 5 things you can see right now."),
            ("4 things you can TOUCH", "Notice 4 things you can physically feel."),
            ("3 things you can HEAR", "Listen. What 3 sounds can you hear?"),
            ("2 things you can SMELL", "Notice 2 things you can smell."),
            ("1 thing you can TASTE", "Notice 1 thing you can taste.")
        ]

        for title, instruction in steps:
            card = ctk.CTkFrame(scroll, fg_color="#2a2a2a", corner_radius=10)
            card.pack(fill="x", pady=10)

            ctk.CTkLabel(
                card,
                text=title,
                font=("Arial", 16, "bold"),
                text_color="#00AAFF"
            ).pack(pady=(15, 5), padx=20, anchor="w")

            ctk.CTkLabel(
                card,
                text=instruction,
                font=("Arial", 13),
                text_color="#CCCCCC",
                wraplength=500,
                justify="left"
            ).pack(pady=(0, 15), padx=20, anchor="w")

    def start_box_breathing(self):
        """Start box breathing"""
        if self.audio.is_enabled():
            self.audio.speak("Starting box breathing. Follow the pattern: breathe in for 4, hold for 4, out for 4, hold for 4.")

        # Create breathing window
        window = ctk.CTkToplevel(self)
        window.title("Box Breathing")
        window.geometry("500x400")

        ctk.CTkLabel(
            window,
            text="🫁 Box Breathing",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            window,
            text="4-4-4-4 Pattern",
            font=("Arial", 16),
            text_color="#888888"
        ).pack()

        # Instruction display
        instruction_label = ctk.CTkLabel(
            window,
            text="Get Ready...",
            font=("Arial", 28, "bold"),
            text_color="#00AAFF"
        )
        instruction_label.pack(pady=60)

        # Visual indicator (simple text-based for now)
        indicator = ctk.CTkLabel(
            window,
            text="○",
            font=("Arial", 48)
        )
        indicator.pack()

        # TODO: Add animated breathing cycle

    def show_ice_water(self):
        """Show ice water dive instructions"""
        if self.audio.is_enabled():
            self.audio.speak("Ice water dive activates your mammalian dive reflex, which quickly calms your nervous system.")

        window = ctk.CTkToplevel(self)
        window.title("Ice Water Dive")
        window.geometry("500x400")

        ctk.CTkLabel(
            window,
            text="🧊 Ice Water Dive",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        content = ctk.CTkFrame(window, fg_color="#2a2a2a", corner_radius=10)
        content.pack(fill="both", expand=True, padx=30, pady=(0, 30))

        instructions = """This activates your mammalian dive reflex,
which quickly calms your nervous system.

HOW TO DO IT:

1. Fill a bowl with ice water
2. Hold your breath
3. Dunk your face for 15-30 seconds
4. Come up and breathe normally

Alternative:
- Hold an ice pack on your face while holding your breath

This works fast - you should feel calmer within 30 seconds."""

        ctk.CTkLabel(
            content,
            text=instructions,
            font=("Arial", 14),
            justify="left",
            wraplength=400
        ).pack(pady=30, padx=30)

    def start_pmr(self):
        """Start progressive muscle relaxation"""
        if self.audio.is_enabled():
            self.audio.speak("Starting progressive muscle relaxation. We'll tense and release each muscle group.")
        # TODO: Implement guided PMR

    def customize_safety_plan(self):
        """Open safety plan customization"""
        if self.audio.is_enabled():
            self.audio.speak("Opening safety plan customization.")
        # TODO: Implement safety plan editor
