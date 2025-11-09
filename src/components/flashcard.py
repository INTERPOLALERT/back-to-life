"""
Flashcard Component - Spaced Repetition Learning
Shows learning moments after quests
"""
import customtkinter as ctk
from src.services.audio_service import get_audio_service


class FlashcardWidget(ctk.CTkFrame):
    """
    Flashcard widget for learning moments

    Shows front, user clicks to reveal back, reinforces learning
    """

    def __init__(self, parent, flashcard_data, on_complete):
        super().__init__(parent, fg_color="#1a1a1a", corner_radius=15)

        self.flashcard = flashcard_data
        self.on_complete = on_complete
        self.audio = get_audio_service()
        self.showing_back = False

        self.grid_columnconfigure(0, weight=1)
        self.setup_ui()

    def setup_ui(self):
        """Build flashcard UI"""
        # Header
        ctk.CTkLabel(
            self,
            text="💡 LEARNING MOMENT",
            font=("Arial", 24, "bold"),
            text_color="#FFD700"
        ).grid(row=0, column=0, pady=(30, 10))

        ctk.CTkLabel(
            self,
            text="Understanding this will help you succeed",
            font=("Arial", 14),
            text_color="#888888"
        ).grid(row=1, column=0, pady=(0, 20))

        # Card container
        self.card_frame = ctk.CTkFrame(
            self,
            fg_color="#2a2a2a",
            corner_radius=10
        )
        self.card_frame.grid(row=2, column=0, sticky="ew", padx=30, pady=20)

        # Card content (will be updated on flip)
        self.card_label = ctk.CTkLabel(
            self.card_frame,
            text=self.flashcard['front'],
            font=("Arial", 20, "bold"),
            wraplength=500,
            justify="center"
        )
        self.card_label.pack(pady=60, padx=40)

        # Flip button
        self.flip_button = ctk.CTkButton(
            self,
            text="🔄 Show Answer",
            command=self.flip_card,
            width=200,
            height=50,
            font=("Arial", 16),
            fg_color="#0066CC",
            hover_color="#0088EE"
        )
        self.flip_button.grid(row=3, column=0, pady=20)

        # Audio button
        audio_btn = ctk.CTkButton(
            self,
            text="🔊 Hear It",
            command=self.play_audio,
            width=150,
            height=40,
            font=("Arial", 14),
            fg_color="#444444",
            hover_color="#666666"
        )
        audio_btn.grid(row=4, column=0, pady=(0, 10))

        # Complete button (hidden until back shown)
        self.complete_button = ctk.CTkButton(
            self,
            text="Got It! ✓",
            command=self.mark_complete,
            width=200,
            height=50,
            font=("Arial", 16),
            fg_color="#00AA00",
            hover_color="#00CC00"
        )
        # Don't show initially

        # Auto-play audio for front
        if self.audio.is_enabled():
            self.audio.speak(self.flashcard.get('audio_front', self.flashcard['front']))

    def flip_card(self):
        """Flip card to show back"""
        if not self.showing_back:
            # Show back
            self.card_label.configure(
                text=self.flashcard['back'],
                font=("Arial", 16)
            )
            self.flip_button.configure(text="🔄 Show Question Again")
            self.showing_back = True

            # Show complete button
            self.complete_button.grid(row=5, column=0, pady=20)

            # Play audio for back
            if self.audio.is_enabled():
                self.audio.speak(self.flashcard.get('audio_back', self.flashcard['back']))

        else:
            # Show front again
            self.card_label.configure(
                text=self.flashcard['front'],
                font=("Arial", 20, "bold")
            )
            self.flip_button.configure(text="🔄 Show Answer")
            self.showing_back = False

            # Hide complete button
            self.complete_button.grid_forget()

    def play_audio(self):
        """Play audio for current side"""
        if self.showing_back:
            text = self.flashcard.get('audio_back', self.flashcard['back'])
        else:
            text = self.flashcard.get('audio_front', self.flashcard['front'])

        self.audio.speak(text)

    def mark_complete(self):
        """Mark flashcard as learned"""
        self.audio.stop()
        self.on_complete(self.flashcard['id'])


class FlashcardManager:
    """
    Manages flashcard database and spaced repetition
    """

    def __init__(self, db):
        self.db = db
        self._init_flashcard_table()

    def _init_flashcard_table(self):
        """Initialize flashcard tracking table"""
        self.db.cursor.execute('''
            CREATE TABLE IF NOT EXISTS flashcard_reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                flashcard_id TEXT,
                review_date TEXT,
                correct BOOLEAN,
                next_review_date TEXT
            )
        ''')
        self.db.conn.commit()

    def record_review(self, flashcard_id, correct=True):
        """Record that user reviewed a flashcard"""
        from datetime import datetime, timedelta

        # Simple spaced repetition: show again tomorrow, then in 3 days, then in 7 days
        self.db.cursor.execute('''
            SELECT COUNT(*) FROM flashcard_reviews
            WHERE flashcard_id = ?
        ''', (flashcard_id,))

        review_count = self.db.cursor.fetchone()[0]

        # Calculate next review date
        if review_count == 0:
            days_until_next = 1  # Tomorrow
        elif review_count == 1:
            days_until_next = 3  # 3 days
        else:
            days_until_next = 7  # Weekly

        next_review = (datetime.now() + timedelta(days=days_until_next)).isoformat()

        self.db.cursor.execute('''
            INSERT INTO flashcard_reviews (flashcard_id, review_date, correct, next_review_date)
            VALUES (?, ?, ?, ?)
        ''', (flashcard_id, datetime.now().isoformat(), correct, next_review))

        self.db.conn.commit()

    def get_due_flashcards(self):
        """Get flashcards that are due for review"""
        from datetime import datetime

        self.db.cursor.execute('''
            SELECT flashcard_id, next_review_date
            FROM flashcard_reviews
            WHERE next_review_date <= ?
            ORDER BY next_review_date
        ''', (datetime.now().isoformat(),))

        return self.db.cursor.fetchall()
