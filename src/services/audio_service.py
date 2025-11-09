"""
Audio Service - Text-to-Speech for Accessibility
Provides audio guidance for all content
"""
import pyttsx3
import threading
from typing import Optional


class AudioService:
    def __init__(self):
        """Initialize TTS engine"""
        self.engine = None
        self.is_speaking = False
        self.enabled = True
        self._init_engine()

    def _init_engine(self):
        """Initialize pyttsx3 engine"""
        try:
            self.engine = pyttsx3.init()

            # Configure voice properties
            self.engine.setProperty('rate', 150)  # Speed (words per minute)
            self.engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

            # Try to set a better voice if available
            voices = self.engine.getProperty('voices')
            if len(voices) > 0:
                # Prefer first voice (usually better quality)
                self.engine.setProperty('voice', voices[0].id)

        except Exception as e:
            print(f"TTS initialization warning: {e}")
            print("Audio features will be disabled.")
            self.enabled = False

    def speak(self, text: str, wait: bool = False):
        """
        Speak text aloud

        Args:
            text: Text to speak
            wait: If True, blocks until speech is complete
        """
        if not self.enabled or not self.engine:
            return

        if self.is_speaking:
            self.stop()

        try:
            if wait:
                # Blocking mode - wait until done
                self.is_speaking = True
                self.engine.say(text)
                self.engine.runAndWait()
                self.is_speaking = False
            else:
                # Non-blocking mode - speak in background
                def speak_background():
                    self.is_speaking = True
                    self.engine.say(text)
                    self.engine.runAndWait()
                    self.is_speaking = False

                thread = threading.Thread(target=speak_background, daemon=True)
                thread.start()

        except Exception as e:
            print(f"TTS error: {e}")
            self.is_speaking = False

    def stop(self):
        """Stop current speech"""
        if self.enabled and self.engine:
            try:
                self.engine.stop()
                self.is_speaking = False
            except:
                pass

    def set_rate(self, rate: int):
        """
        Set speech rate

        Args:
            rate: Words per minute (50-300, default 150)
        """
        if self.enabled and self.engine:
            self.engine.setProperty('rate', max(50, min(300, rate)))

    def set_volume(self, volume: float):
        """
        Set speech volume

        Args:
            volume: Volume level (0.0 to 1.0)
        """
        if self.enabled and self.engine:
            self.engine.setProperty('volume', max(0.0, min(1.0, volume)))

    def toggle(self):
        """Toggle audio on/off"""
        self.enabled = not self.enabled
        return self.enabled

    def is_enabled(self):
        """Check if audio is enabled"""
        return self.enabled


# Global audio service instance
_audio_service: Optional[AudioService] = None


def get_audio_service() -> AudioService:
    """Get or create global audio service instance"""
    global _audio_service
    if _audio_service is None:
        _audio_service = AudioService()
    return _audio_service


def speak(text: str, wait: bool = False):
    """Convenience function to speak text"""
    service = get_audio_service()
    service.speak(text, wait=wait)


def stop_audio():
    """Convenience function to stop audio"""
    service = get_audio_service()
    service.stop()
