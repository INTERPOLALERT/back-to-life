"""
Tools Tab - Mood-Based Tool Library
Different tools for different feelings and situations
"""
import customtkinter as ctk


class ToolsTab(ctk.CTkFrame):
    """
    Tool library with:
    - Mood-based selector ("I feel...")
    - Situation-based tools
    - Quick access tools
    - Tool categories
    """

    def __init__(self, parent, db, audio):
        super().__init__(parent, fg_color="transparent")

        self.db = db
        self.audio = audio
        self.current_filter = "all"

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.setup_ui()

    def setup_ui(self):
        """Build tools UI"""
        # Header
        header = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=15)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header,
            text="🛠️ Tool Library",
            font=("Arial", 28, "bold"),
            text_color="#00AAFF"
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            header,
            text="Different tools for different moments",
            font=("Arial", 14),
            text_color="#888888"
        ).pack(pady=(0, 20))

        # Mood selector
        mood_frame = ctk.CTkFrame(header, fg_color="#2a2a2a", corner_radius=10)
        mood_frame.pack(fill="x", padx=20, pady=(0, 20))

        ctk.CTkLabel(
            mood_frame,
            text="How are you feeling right now?",
            font=("Arial", 16, "bold")
        ).pack(pady=(15, 10))

        # Mood buttons
        mood_buttons = ctk.CTkFrame(mood_frame, fg_color="transparent")
        mood_buttons.pack(pady=(0, 15))

        moods = [
            ("😰 Overwhelmed", "overwhelmed", "#FF6600"),
            ("😔 Low Energy", "low_energy", "#666666"),
            ("😤 Frustrated", "frustrated", "#CC0000"),
            ("😕 Stuck", "stuck", "#AA6600"),
            ("🤔 Confused", "confused", "#0066CC"),
            ("✨ Good", "good", "#00AA00")
        ]

        for i, (label, mood_id, color) in enumerate(moods):
            btn = ctk.CTkButton(
                mood_buttons,
                text=label,
                command=lambda m=mood_id: self.filter_by_mood(m),
                width=140,
                height=40,
                font=("Arial", 13),
                fg_color=color,
                hover_color=self.lighten_color(color)
            )
            btn.grid(row=i // 3, column=i % 3, padx=8, pady=5)

        # Show all button
        ctk.CTkButton(
            mood_frame,
            text="Show All Tools",
            command=lambda: self.filter_by_mood("all"),
            width=200,
            height=35,
            font=("Arial", 12),
            fg_color="#444444",
            hover_color="#666666"
        ).pack(pady=(10, 15))

        # Scrollable tools area
        self.tools_scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        self.tools_scroll.grid(row=1, column=0, sticky="nsew")
        self.tools_scroll.grid_columnconfigure(0, weight=1)

        # Show all tools by default
        self.display_tools("all")

    def filter_by_mood(self, mood_id):
        """Filter tools by mood"""
        self.current_filter = mood_id
        self.display_tools(mood_id)

        # Audio feedback
        mood_messages = {
            "overwhelmed": "Here are tools to help when you're feeling overwhelmed.",
            "low_energy": "These tools work even when your energy is low.",
            "frustrated": "Tools to help manage frustration.",
            "stuck": "Tools to help you get unstuck.",
            "confused": "Tools to help clarify and simplify.",
            "good": "Great! Here are tools to maintain momentum.",
            "all": "Showing all available tools."
        }
        if self.audio.is_enabled():
            self.audio.speak(mood_messages.get(mood_id, ""))

    def display_tools(self, filter_mood):
        """Display filtered tools"""
        # Clear existing
        for widget in self.tools_scroll.winfo_children():
            widget.destroy()

        # Tool database with mood mapping
        all_tools = self.get_all_tools()

        # Filter tools
        if filter_mood == "all":
            tools = all_tools
        else:
            tools = [t for t in all_tools if filter_mood in t['moods']]

        if not tools:
            ctk.CTkLabel(
                self.tools_scroll,
                text="No tools found for this mood.",
                font=("Arial", 14),
                text_color="#888888"
            ).pack(pady=40)
            return

        # Display tools by category
        categories = {}
        for tool in tools:
            cat = tool['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(tool)

        row = 0
        for category, cat_tools in categories.items():
            # Category header
            cat_header = ctk.CTkFrame(
                self.tools_scroll,
                fg_color="#1a1a1a",
                corner_radius=10
            )
            cat_header.grid(row=row, column=0, sticky="ew", pady=(0, 10))

            ctk.CTkLabel(
                cat_header,
                text=f"{self.get_category_icon(category)} {category}",
                font=("Arial", 18, "bold"),
                text_color="#FFD700"
            ).pack(pady=15, padx=20, anchor="w")

            row += 1

            # Tools grid
            tools_grid = ctk.CTkFrame(self.tools_scroll, fg_color="transparent")
            tools_grid.grid(row=row, column=0, sticky="ew", pady=(0, 20))
            tools_grid.grid_columnconfigure((0, 1), weight=1)

            for i, tool in enumerate(cat_tools):
                self.create_tool_card(tools_grid, tool, i // 2, i % 2)

            row += 1

    def create_tool_card(self, parent, tool, row, col):
        """Create individual tool card"""
        card = ctk.CTkFrame(
            parent,
            fg_color="#2a2a2a",
            corner_radius=12
        )
        card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Tool icon and title
        ctk.CTkLabel(
            card,
            text=tool['icon'],
            font=("Arial", 32)
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            card,
            text=tool['name'],
            font=("Arial", 16, "bold")
        ).pack(pady=(0, 5))

        # Description
        ctk.CTkLabel(
            card,
            text=tool['description'],
            font=("Arial", 12),
            text_color="#AAAAAA",
            wraplength=220,
            justify="center"
        ).pack(pady=(0, 15), padx=15)

        # Use button
        ctk.CTkButton(
            card,
            text=f"Use {tool['name']}",
            command=lambda t=tool: self.use_tool(t),
            width=180,
            height=40,
            font=("Arial", 13),
            fg_color="#0066CC",
            hover_color="#0088EE"
        ).pack(pady=(0, 20))

    def get_all_tools(self):
        """Get complete tool database"""
        return [
            # Task Management Tools
            {
                'id': 'magic_todo',
                'name': 'Magic To-Do',
                'icon': '✨',
                'description': 'Breaks big tasks into tiny steps (like Goblin Tools)',
                'category': 'Task Management',
                'moods': ['overwhelmed', 'stuck', 'all'],
                'action': 'magic_todo'
            },
            {
                'id': 'task_estimator',
                'name': 'Time Estimator',
                'icon': '⏱️',
                'description': 'Helps estimate how long tasks really take',
                'category': 'Task Management',
                'moods': ['overwhelmed', 'confused', 'all'],
                'action': 'time_estimator'
            },
            {
                'id': 'priority_matrix',
                'name': 'Priority Decider',
                'icon': '🎯',
                'description': 'Figures out what to do first when everything feels urgent',
                'category': 'Task Management',
                'moods': ['overwhelmed', 'confused', 'all'],
                'action': 'priority_matrix'
            },

            # Emotion & Energy Tools
            {
                'id': 'mood_logger',
                'name': 'Mood Logger',
                'icon': '📊',
                'description': 'Track patterns in how you feel',
                'category': 'Emotional Support',
                'moods': ['low_energy', 'frustrated', 'all'],
                'action': 'mood_logger'
            },
            {
                'id': 'energy_optimizer',
                'name': 'Energy Optimizer',
                'icon': '⚡',
                'description': 'Matches tasks to your energy level',
                'category': 'Emotional Support',
                'moods': ['low_energy', 'all'],
                'action': 'energy_optimizer'
            },
            {
                'id': 'emotion_namer',
                'name': 'Emotion Namer',
                'icon': '🎭',
                'description': 'Helps identify what you\'re actually feeling',
                'category': 'Emotional Support',
                'moods': ['confused', 'frustrated', 'all'],
                'action': 'emotion_namer'
            },

            # Focus & Attention Tools
            {
                'id': 'focus_timer',
                'name': 'Focus Timer',
                'icon': '⏲️',
                'description': 'Pomodoro timer with ADHD-friendly breaks',
                'category': 'Focus Tools',
                'moods': ['good', 'all'],
                'action': 'focus_timer'
            },
            {
                'id': 'distraction_blocker',
                'name': 'Distraction Blocker',
                'icon': '🚫',
                'description': 'Gentle reminders when you drift',
                'category': 'Focus Tools',
                'moods': ['frustrated', 'stuck', 'all'],
                'action': 'distraction_blocker'
            },
            {
                'id': 'body_doubling',
                'name': 'Virtual Body Double',
                'icon': '👥',
                'description': 'Simulated presence to help you start',
                'category': 'Focus Tools',
                'moods': ['stuck', 'low_energy', 'all'],
                'action': 'body_doubling'
            },

            # Communication Tools
            {
                'id': 'text_formatter',
                'name': 'Text Formatter',
                'icon': '💬',
                'description': 'Makes your messages clearer and more professional',
                'category': 'Communication',
                'moods': ['confused', 'frustrated', 'all'],
                'action': 'text_formatter'
            },
            {
                'id': 'conversation_helper',
                'name': 'Conversation Helper',
                'icon': '🗣️',
                'description': 'Helps plan difficult conversations',
                'category': 'Communication',
                'moods': ['overwhelmed', 'confused', 'all'],
                'action': 'conversation_helper'
            },

            # Crisis & Grounding Tools
            {
                'id': 'grounding_exercise',
                'name': '5-4-3-2-1 Grounding',
                'icon': '🌊',
                'description': 'Quick sensory grounding when overwhelmed',
                'category': 'Crisis Support',
                'moods': ['overwhelmed', 'frustrated', 'all'],
                'action': 'grounding_exercise'
            },
            {
                'id': 'breathing_guide',
                'name': 'Breathing Guide',
                'icon': '🫁',
                'description': 'Guided breathing with audio',
                'category': 'Crisis Support',
                'moods': ['overwhelmed', 'frustrated', 'low_energy', 'all'],
                'action': 'breathing_guide'
            },
            {
                'id': 'crisis_plan',
                'name': 'Crisis Plan',
                'icon': '🆘',
                'description': 'Your personalized crisis support plan',
                'category': 'Crisis Support',
                'moods': ['overwhelmed', 'all'],
                'action': 'crisis_plan'
            },

            # Organization Tools
            {
                'id': 'decision_helper',
                'name': 'Decision Helper',
                'icon': '🤔',
                'description': 'Makes decisions when you\'re stuck choosing',
                'category': 'Organization',
                'moods': ['stuck', 'overwhelmed', 'all'],
                'action': 'decision_helper'
            },
            {
                'id': 'routine_builder',
                'name': 'Routine Builder',
                'icon': '📅',
                'description': 'Creates sustainable routines',
                'category': 'Organization',
                'moods': ['good', 'all'],
                'action': 'routine_builder'
            }
        ]

    def use_tool(self, tool):
        """Launch selected tool"""
        # Audio feedback
        if self.audio.is_enabled():
            self.audio.speak(f"Opening {tool['name']}. {tool['description']}")

        # Launch tool based on action
        action = tool['action']

        if action == 'magic_todo':
            self.launch_magic_todo()
        elif action == 'time_estimator':
            self.launch_time_estimator()
        elif action == 'priority_matrix':
            self.launch_priority_matrix()
        elif action == 'mood_logger':
            self.launch_mood_logger()
        elif action == 'grounding_exercise':
            self.launch_grounding()
        elif action == 'breathing_guide':
            self.launch_breathing()
        # Add more tool launches...
        else:
            # Placeholder for unimplemented tools
            self.show_tool_placeholder(tool)

    def launch_magic_todo(self):
        """Launch Magic To-Do tool"""
        # Create tool window
        tool_window = ctk.CTkToplevel(self)
        tool_window.title("Magic To-Do")
        tool_window.geometry("600x500")

        ctk.CTkLabel(
            tool_window,
            text="✨ Magic To-Do",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            tool_window,
            text="Enter a big overwhelming task, and I'll break it into tiny steps:",
            font=("Arial", 14),
            wraplength=500
        ).pack(pady=10)

        # Input
        task_input = ctk.CTkTextbox(
            tool_window,
            height=100,
            font=("Arial", 13)
        )
        task_input.pack(pady=10, padx=40, fill="x")

        # Break down button
        def break_down():
            task = task_input.get("1.0", "end-1c")
            if task.strip():
                # Simple breakdown algorithm
                steps = self.break_down_task(task)
                result_text.delete("1.0", "end")
                result_text.insert("1.0", "\n".join(f"{i+1}. {step}" for i, step in enumerate(steps)))

        ctk.CTkButton(
            tool_window,
            text="✨ Break It Down",
            command=break_down,
            width=200,
            height=40,
            font=("Arial", 14)
        ).pack(pady=10)

        # Result area
        ctk.CTkLabel(
            tool_window,
            text="Broken down steps:",
            font=("Arial", 13, "bold")
        ).pack(pady=(20, 5))

        result_text = ctk.CTkTextbox(
            tool_window,
            height=200,
            font=("Arial", 12)
        )
        result_text.pack(pady=10, padx=40, fill="both", expand=True)

    def launch_grounding(self):
        """Launch 5-4-3-2-1 grounding exercise"""
        tool_window = ctk.CTkToplevel(self)
        tool_window.title("Grounding Exercise")
        tool_window.geometry("600x500")

        ctk.CTkLabel(
            tool_window,
            text="🌊 5-4-3-2-1 Grounding",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            tool_window,
            text="Let's ground you in the present moment.\nGo at your own pace.",
            font=("Arial", 14),
            wraplength=500
        ).pack(pady=10)

        # Grounding steps
        steps = [
            ("5 things you can SEE", "Look around. Name 5 things you can see right now."),
            ("4 things you can TOUCH", "Notice 4 things you can physically feel touching your body."),
            ("3 things you can HEAR", "Listen. What 3 sounds can you hear?"),
            ("2 things you can SMELL", "Notice 2 things you can smell (or like to smell)."),
            ("1 thing you can TASTE", "Notice 1 thing you can taste, or imagine a taste you enjoy.")
        ]

        step_frame = ctk.CTkScrollableFrame(tool_window)
        step_frame.pack(pady=20, padx=40, fill="both", expand=True)

        for title, instruction in steps:
            card = ctk.CTkFrame(step_frame, fg_color="#2a2a2a", corner_radius=10)
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
                wraplength=450,
                justify="left"
            ).pack(pady=(0, 15), padx=20, anchor="w")

        if self.audio.is_enabled():
            self.audio.speak("Let's ground you with the 5-4-3-2-1 exercise. Go at your own pace. Start by noticing 5 things you can see.")

    def launch_breathing(self):
        """Launch breathing guide"""
        tool_window = ctk.CTkToplevel(self)
        tool_window.title("Breathing Guide")
        tool_window.geometry("500x400")

        ctk.CTkLabel(
            tool_window,
            text="🫁 Breathing Guide",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        # Breathing circle (visual guide)
        canvas_frame = ctk.CTkFrame(tool_window, fg_color="#1a1a1a")
        canvas_frame.pack(pady=20, padx=40, fill="both", expand=True)

        instruction_label = ctk.CTkLabel(
            canvas_frame,
            text="Click Start to begin",
            font=("Arial", 18, "bold")
        )
        instruction_label.pack(pady=80)

        # TODO: Add animated breathing circle
        # For now, simple text instructions

        ctk.CTkButton(
            tool_window,
            text="▶ Start Breathing Exercise",
            width=200,
            height=50,
            font=("Arial", 14)
        ).pack(pady=20)

    def show_tool_placeholder(self, tool):
        """Show placeholder for unimplemented tools"""
        placeholder = ctk.CTkToplevel(self)
        placeholder.title(tool['name'])
        placeholder.geometry("500x300")

        ctk.CTkLabel(
            placeholder,
            text=f"{tool['icon']} {tool['name']}",
            font=("Arial", 24, "bold")
        ).pack(pady=40)

        ctk.CTkLabel(
            placeholder,
            text=tool['description'],
            font=("Arial", 14),
            wraplength=400
        ).pack(pady=20)

        ctk.CTkLabel(
            placeholder,
            text="This tool is coming soon!",
            font=("Arial", 12),
            text_color="#888888"
        ).pack(pady=20)

    def break_down_task(self, task):
        """Simple task breakdown algorithm"""
        # This is a simplified version - could be enhanced with AI/templates
        task_lower = task.lower()

        if "clean" in task_lower:
            return [
                "Look at the area you need to clean (just look, don't touch)",
                "Pick ONE small section to focus on",
                "Set a timer for 5 minutes",
                "Clean just that one section",
                "Stop when timer goes off (even if not done)",
                "Celebrate completing this step"
            ]
        elif "email" in task_lower or "message" in task_lower:
            return [
                "Open your email/messaging app",
                "Read the message you need to respond to",
                "Write just ONE sentence as a response",
                "Add one more sentence if you can",
                "Click send (don't over-edit)",
                "Mark as done"
            ]
        elif "organize" in task_lower:
            return [
                "Look at what needs organizing (don't touch yet)",
                "Pick the EASIEST item to organize",
                "Organize just that ONE item",
                "Take a breath",
                "Organize one more item if you want",
                "Stop and celebrate what you did"
            ]
        else:
            # Generic breakdown
            return [
                "Identify the very first tiny step",
                "Do just that one step",
                "Pause and assess",
                "Identify the next tiny step",
                "Do that step",
                "Continue one micro-step at a time"
            ]

    def get_category_icon(self, category):
        """Get icon for category"""
        icons = {
            'Task Management': '✅',
            'Emotional Support': '❤️',
            'Focus Tools': '🎯',
            'Communication': '💬',
            'Crisis Support': '🛡️',
            'Organization': '📋'
        }
        return icons.get(category, '🔧')

    def lighten_color(self, color):
        """Lighten color for hover"""
        lighter = {
            "#FF6600": "#FF8833",
            "#666666": "#888888",
            "#CC0000": "#EE0000",
            "#AA6600": "#CC8800",
            "#0066CC": "#0088EE",
            "#00AA00": "#00CC00"
        }
        return lighter.get(color, color)
