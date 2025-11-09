"""
Learn Tab - Learning Center
Courses, flashcards, quizzes, and psychoeducation library
"""
import customtkinter as ctk
from src.components.flashcard import FlashcardWidget, FlashcardManager
from src.components.quiz import QuizWidget


class LearnTab(ctk.CTkFrame):
    """
    Learning center with:
    - Psychoeducation courses
    - Flashcard library
    - Interactive quizzes
    - Learning progress tracking
    """

    def __init__(self, parent, db, audio):
        super().__init__(parent, fg_color="transparent")

        self.db = db
        self.audio = audio
        self.flashcard_manager = FlashcardManager(db)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.setup_ui()

    def setup_ui(self):
        """Build learning center UI"""
        # Header
        header = ctk.CTkFrame(self, fg_color="#1a1a1a", corner_radius=15)
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            header,
            text="📚 Learning Center",
            font=("Arial", 28, "bold"),
            text_color="#00AAFF"
        ).pack(pady=(20, 5))

        ctk.CTkLabel(
            header,
            text="Understanding yourself is the first step to change",
            font=("Arial", 14),
            text_color="#888888"
        ).pack(pady=(0, 20))

        # Tab selector
        tab_frame = ctk.CTkFrame(header, fg_color="transparent")
        tab_frame.pack(pady=(0, 20))

        self.learning_tabs = {}
        tabs = [
            ("📖 Courses", "courses"),
            ("💡 Flashcards", "flashcards"),
            ("🎓 Quizzes", "quizzes"),
            ("📊 Progress", "learning_progress")
        ]

        for i, (label, tab_id) in enumerate(tabs):
            btn = ctk.CTkButton(
                tab_frame,
                text=label,
                command=lambda t=tab_id: self.show_learning_section(t),
                width=150,
                height=40,
                font=("Arial", 13),
                fg_color="#2a2a2a",
                hover_color="#3a3a3a"
            )
            btn.grid(row=0, column=i, padx=5)
            self.learning_tabs[tab_id] = btn

        # Main content area
        self.content_area = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        self.content_area.grid(row=1, column=0, sticky="nsew")
        self.content_area.grid_columnconfigure(0, weight=1)

        # Show courses by default
        self.show_learning_section("courses")

    def show_learning_section(self, section_id):
        """Switch between learning sections"""
        # Update button states
        for tab_id, btn in self.learning_tabs.items():
            if tab_id == section_id:
                btn.configure(fg_color="#0066CC")
            else:
                btn.configure(fg_color="#2a2a2a")

        # Clear content
        for widget in self.content_area.winfo_children():
            widget.destroy()

        # Show selected section
        if section_id == "courses":
            self.show_courses()
        elif section_id == "flashcards":
            self.show_flashcards()
        elif section_id == "quizzes":
            self.show_quizzes()
        elif section_id == "learning_progress":
            self.show_learning_progress()

    def show_courses(self):
        """Display available courses"""
        courses = self.get_all_courses()

        for i, course in enumerate(courses):
            course_card = ctk.CTkFrame(
                self.content_area,
                fg_color="#1a1a1a",
                corner_radius=15
            )
            course_card.grid(row=i, column=0, sticky="ew", pady=10)

            # Course header
            header_frame = ctk.CTkFrame(course_card, fg_color="transparent")
            header_frame.pack(fill="x", padx=20, pady=15)

            ctk.CTkLabel(
                header_frame,
                text=course['icon'],
                font=("Arial", 32)
            ).pack(side="left", padx=(0, 15))

            info_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
            info_frame.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(
                info_frame,
                text=course['title'],
                font=("Arial", 18, "bold"),
                anchor="w"
            ).pack(anchor="w")

            ctk.CTkLabel(
                info_frame,
                text=f"{course['lessons']} lessons • {course['duration']} min",
                font=("Arial", 12),
                text_color="#888888",
                anchor="w"
            ).pack(anchor="w")

            # Description
            ctk.CTkLabel(
                course_card,
                text=course['description'],
                font=("Arial", 13),
                text_color="#CCCCCC",
                wraplength=700,
                justify="left",
                anchor="w"
            ).pack(fill="x", padx=20, pady=(0, 15))

            # Progress bar
            progress_frame = ctk.CTkFrame(course_card, fg_color="#2a2a2a", corner_radius=8)
            progress_frame.pack(fill="x", padx=20, pady=(0, 15))

            progress_value = course.get('progress', 0)
            ctk.CTkProgressBar(
                progress_frame,
                width=600
            ).pack(side="left", padx=15, pady=12)

            ctk.CTkLabel(
                progress_frame,
                text=f"{progress_value}% Complete",
                font=("Arial", 12)
            ).pack(side="left", padx=(0, 15))

            # Action button
            btn_text = "Continue" if progress_value > 0 else "Start Course"
            ctk.CTkButton(
                course_card,
                text=btn_text,
                command=lambda c=course: self.start_course(c),
                width=150,
                height=40,
                font=("Arial", 14),
                fg_color="#0066CC",
                hover_color="#0088EE"
            ).pack(pady=(0, 20))

    def show_flashcards(self):
        """Display flashcard library"""
        ctk.CTkLabel(
            self.content_area,
            text="💡 Flashcard Library",
            font=("Arial", 22, "bold")
        ).grid(row=0, column=0, pady=(0, 20))

        # Due flashcards
        due_count = len(self.flashcard_manager.get_due_flashcards())

        due_card = ctk.CTkFrame(self.content_area, fg_color="#1a1a1a", corner_radius=12)
        due_card.grid(row=1, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            due_card,
            text=f"📝 {due_count} Cards Due for Review",
            font=("Arial", 18, "bold"),
            text_color="#FFD700"
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            due_card,
            text="Spaced repetition helps you remember what you learn",
            font=("Arial", 13),
            text_color="#888888"
        ).pack(pady=(0, 15))

        if due_count > 0:
            ctk.CTkButton(
                due_card,
                text=f"Review {due_count} Cards Now",
                command=self.start_flashcard_review,
                width=200,
                height=50,
                font=("Arial", 15),
                fg_color="#0066CC",
                hover_color="#0088EE"
            ).pack(pady=(0, 20))
        else:
            ctk.CTkLabel(
                due_card,
                text="No cards due right now. Great job! 🎉",
                font=("Arial", 14),
                text_color="#00AA00"
            ).pack(pady=(0, 20))

        # Flashcard collections
        ctk.CTkLabel(
            self.content_area,
            text="Browse by Topic",
            font=("Arial", 18, "bold")
        ).grid(row=2, column=0, pady=(20, 10), sticky="w")

        collections = [
            {
                'title': 'ADHD Fundamentals',
                'icon': '🧠',
                'cards': 15,
                'description': 'Understanding how ADHD affects your brain'
            },
            {
                'title': 'Executive Function',
                'icon': '⚙️',
                'cards': 12,
                'description': 'Working memory, planning, task initiation'
            },
            {
                'title': 'Depression Basics',
                'icon': '🌧️',
                'cards': 10,
                'description': 'What depression is and how it works'
            },
            {
                'title': 'Relationship Skills',
                'icon': '❤️',
                'cards': 8,
                'description': 'Communication, boundaries, conflict resolution'
            },
            {
                'title': 'Physical Recovery',
                'icon': '💪',
                'cards': 8,
                'description': 'Rebuilding physical health step by step'
            }
        ]

        collections_grid = ctk.CTkFrame(self.content_area, fg_color="transparent")
        collections_grid.grid(row=3, column=0, sticky="ew", pady=10)
        collections_grid.grid_columnconfigure((0, 1), weight=1)

        for i, collection in enumerate(collections):
            card = ctk.CTkFrame(
                collections_grid,
                fg_color="#2a2a2a",
                corner_radius=12
            )
            card.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")

            ctk.CTkLabel(
                card,
                text=collection['icon'],
                font=("Arial", 32)
            ).pack(pady=(20, 5))

            ctk.CTkLabel(
                card,
                text=collection['title'],
                font=("Arial", 16, "bold")
            ).pack(pady=(0, 5))

            ctk.CTkLabel(
                card,
                text=f"{collection['cards']} cards",
                font=("Arial", 12),
                text_color="#888888"
            ).pack()

            ctk.CTkLabel(
                card,
                text=collection['description'],
                font=("Arial", 11),
                text_color="#AAAAAA",
                wraplength=200,
                justify="center"
            ).pack(pady=10, padx=15)

            ctk.CTkButton(
                card,
                text="Study Collection",
                command=lambda c=collection: self.study_collection(c),
                width=150,
                height=35,
                font=("Arial", 12)
            ).pack(pady=(0, 20))

    def show_quizzes(self):
        """Display available quizzes"""
        ctk.CTkLabel(
            self.content_area,
            text="🎓 Knowledge Checks",
            font=("Arial", 22, "bold")
        ).grid(row=0, column=0, pady=(0, 20))

        quizzes = [
            {
                'title': 'ADHD & Executive Function',
                'icon': '🧠',
                'questions': 5,
                'description': 'Test your understanding of ADHD and executive dysfunction',
                'difficulty': 'Beginner'
            },
            {
                'title': 'Depression Recognition',
                'icon': '🌧️',
                'questions': 5,
                'description': 'Understanding depression symptoms and patterns',
                'difficulty': 'Beginner'
            },
            {
                'title': 'Healthy Boundaries',
                'icon': '🛡️',
                'questions': 5,
                'description': 'Practice setting and maintaining boundaries',
                'difficulty': 'Intermediate'
            },
            {
                'title': 'Physical Health Basics',
                'icon': '💪',
                'questions': 5,
                'description': 'Building sustainable physical health habits',
                'difficulty': 'Beginner'
            }
        ]

        for i, quiz in enumerate(quizzes):
            quiz_card = ctk.CTkFrame(
                self.content_area,
                fg_color="#1a1a1a",
                corner_radius=12
            )
            quiz_card.grid(row=i + 1, column=0, sticky="ew", pady=10)

            # Header
            header = ctk.CTkFrame(quiz_card, fg_color="transparent")
            header.pack(fill="x", padx=20, pady=15)

            ctk.CTkLabel(
                header,
                text=quiz['icon'],
                font=("Arial", 32)
            ).pack(side="left", padx=(0, 15))

            info_frame = ctk.CTkFrame(header, fg_color="transparent")
            info_frame.pack(side="left", fill="x", expand=True)

            ctk.CTkLabel(
                info_frame,
                text=quiz['title'],
                font=("Arial", 18, "bold"),
                anchor="w"
            ).pack(anchor="w")

            details_text = f"{quiz['questions']} questions • {quiz['difficulty']} • ~5 min"
            ctk.CTkLabel(
                info_frame,
                text=details_text,
                font=("Arial", 12),
                text_color="#888888",
                anchor="w"
            ).pack(anchor="w")

            # Description
            ctk.CTkLabel(
                quiz_card,
                text=quiz['description'],
                font=("Arial", 13),
                text_color="#CCCCCC",
                wraplength=650,
                justify="left",
                anchor="w"
            ).pack(fill="x", padx=20, pady=(0, 15))

            # Start button
            ctk.CTkButton(
                quiz_card,
                text="Take Quiz",
                command=lambda q=quiz: self.start_quiz(q),
                width=150,
                height=40,
                font=("Arial", 14),
                fg_color="#0066CC",
                hover_color="#0088EE"
            ).pack(pady=(0, 20))

    def show_learning_progress(self):
        """Display learning progress and stats"""
        ctk.CTkLabel(
            self.content_area,
            text="📊 Your Learning Progress",
            font=("Arial", 22, "bold")
        ).grid(row=0, column=0, pady=(0, 20))

        # Overall stats
        stats_card = ctk.CTkFrame(self.content_area, fg_color="#1a1a1a", corner_radius=12)
        stats_card.grid(row=1, column=0, sticky="ew", pady=(0, 20))

        ctk.CTkLabel(
            stats_card,
            text="Learning Statistics",
            font=("Arial", 18, "bold")
        ).pack(pady=(20, 15))

        stats_grid = ctk.CTkFrame(stats_card, fg_color="transparent")
        stats_grid.pack(pady=(0, 20))

        stats = [
            ("Flashcards Reviewed", "245", "💡"),
            ("Quizzes Completed", "12", "🎓"),
            ("Course Lessons", "8/24", "📖"),
            ("Learning Streak", "5 days", "🔥")
        ]

        for i, (label, value, icon) in enumerate(stats):
            stat_box = ctk.CTkFrame(stats_grid, fg_color="#2a2a2a", corner_radius=8)
            stat_box.grid(row=i // 2, column=i % 2, padx=15, pady=10, sticky="nsew")

            ctk.CTkLabel(
                stat_box,
                text=icon,
                font=("Arial", 24)
            ).pack(pady=(15, 5), padx=30)

            ctk.CTkLabel(
                stat_box,
                text=value,
                font=("Arial", 20, "bold"),
                text_color="#00AAFF"
            ).pack(pady=0, padx=30)

            ctk.CTkLabel(
                stat_box,
                text=label,
                font=("Arial", 11),
                text_color="#888888"
            ).pack(pady=(0, 15), padx=30)

        # Recent activity
        ctk.CTkLabel(
            self.content_area,
            text="Recent Activity",
            font=("Arial", 18, "bold")
        ).grid(row=2, column=0, pady=(20, 10), sticky="w")

        activity_card = ctk.CTkFrame(self.content_area, fg_color="#1a1a1a", corner_radius=12)
        activity_card.grid(row=3, column=0, sticky="ew")

        activities = [
            ("Reviewed 'Executive Function' flashcards", "2 hours ago", "💡"),
            ("Completed 'Healthy Boundaries' quiz", "Yesterday", "🎓"),
            ("Finished lesson: Understanding ADHD", "2 days ago", "📖"),
            ("Reviewed 'Depression Basics' flashcards", "3 days ago", "💡")
        ]

        for activity, time, icon in activities:
            activity_row = ctk.CTkFrame(activity_card, fg_color="#2a2a2a", corner_radius=8)
            activity_row.pack(fill="x", padx=15, pady=8)

            ctk.CTkLabel(
                activity_row,
                text=icon,
                font=("Arial", 18)
            ).pack(side="left", padx=(15, 10), pady=10)

            text_frame = ctk.CTkFrame(activity_row, fg_color="transparent")
            text_frame.pack(side="left", fill="x", expand=True, pady=10)

            ctk.CTkLabel(
                text_frame,
                text=activity,
                font=("Arial", 13),
                anchor="w"
            ).pack(anchor="w")

            ctk.CTkLabel(
                text_frame,
                text=time,
                font=("Arial", 11),
                text_color="#888888",
                anchor="w"
            ).pack(anchor="w")

    def get_all_courses(self):
        """Get available courses"""
        return [
            {
                'id': 'adhd_fundamentals',
                'title': 'ADHD Fundamentals',
                'icon': '🧠',
                'description': 'Understanding how ADHD affects your brain, executive function, and daily life. Learn why simple tasks feel impossible and what you can do about it.',
                'lessons': 8,
                'duration': 45,
                'progress': 0
            },
            {
                'id': 'depression_basics',
                'title': 'Understanding Depression',
                'icon': '🌧️',
                'description': 'What depression really is, how it affects motivation and energy, and evidence-based strategies that actually help.',
                'lessons': 6,
                'duration': 35,
                'progress': 0
            },
            {
                'id': 'executive_function',
                'title': 'Executive Function Skills',
                'icon': '⚙️',
                'description': 'Building the skills your brain struggles with: planning, task initiation, working memory, and time management.',
                'lessons': 10,
                'duration': 60,
                'progress': 0
            },
            {
                'id': 'relationship_skills',
                'title': 'Healthy Relationships',
                'icon': '❤️',
                'description': 'Communication, boundaries, conflict resolution, and maintaining relationships when your brain makes it hard.',
                'lessons': 7,
                'duration': 40,
                'progress': 0
            },
            {
                'id': 'physical_recovery',
                'title': 'Physical Recovery Basics',
                'icon': '💪',
                'description': 'Rebuilding physical health from severe deconditioning. Start where you are, not where you think you should be.',
                'lessons': 9,
                'duration': 50,
                'progress': 0
            }
        ]

    def start_course(self, course):
        """Launch course"""
        if self.audio.is_enabled():
            self.audio.speak(f"Opening {course['title']} course.")
        # TODO: Implement course viewer
        pass

    def start_flashcard_review(self):
        """Start reviewing due flashcards"""
        if self.audio.is_enabled():
            self.audio.speak("Starting flashcard review session.")

        # Get due cards
        due_cards = self.flashcard_manager.get_due_flashcards()

        if not due_cards:
            return

        # Create review window
        review_window = ctk.CTkToplevel(self)
        review_window.title("Flashcard Review")
        review_window.geometry("700x500")

        # TODO: Implement flashcard review session
        # For now, show first card as example
        first_card = due_cards[0]

        FlashcardWidget(
            review_window,
            first_card,
            lambda correct: self.on_flashcard_reviewed(first_card['id'], correct)
        ).pack(expand=True, fill="both", padx=20, pady=20)

    def study_collection(self, collection):
        """Study a flashcard collection"""
        if self.audio.is_enabled():
            self.audio.speak(f"Opening {collection['title']} flashcard collection.")
        # TODO: Implement collection study
        pass

    def start_quiz(self, quiz):
        """Launch quiz"""
        if self.audio.is_enabled():
            self.audio.speak(f"Starting {quiz['title']} quiz.")
        # TODO: Implement quiz
        pass

    def on_flashcard_reviewed(self, flashcard_id, correct):
        """Handle flashcard review completion"""
        self.flashcard_manager.record_review(flashcard_id, correct)
