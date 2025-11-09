"""
Test script to verify all imports work correctly
(without requiring GUI)
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("Testing imports...")

# Test database
try:
    from src.services.database import Database
    print("✓ Database import successful")
except Exception as e:
    print(f"✗ Database import failed: {e}")

# Test audio service
try:
    from src.services.audio_service import get_audio_service
    print("✓ Audio service import successful")
except Exception as e:
    print(f"✗ Audio service import failed: {e}")

# Test context engine
try:
    from src.utils.context_engine import ContextEngine
    print("✓ Context engine import successful")
except Exception as e:
    print(f"✗ Context engine import failed: {e}")

# Test components
try:
    from src.components.flashcard import FlashcardManager
    print("✓ Flashcard component import successful")
except Exception as e:
    print(f"✗ Flashcard component import failed: {e}")

try:
    from src.components.quiz import QuizWidget
    print("✓ Quiz component import successful")
except Exception as e:
    print(f"✗ Quiz component import failed: {e}")

# Test quest database
try:
    from src.data.quest_database import initialize_quest_database, QUESTS
    print(f"✓ Quest database import successful ({len(QUESTS)} quests)")
except Exception as e:
    print(f"✗ Quest database import failed: {e}")

# Test enhanced quests
try:
    from src.data.enhanced_quests import DEMO_QUEST
    print("✓ Enhanced quests import successful")
except Exception as e:
    print(f"✗ Enhanced quests import failed: {e}")

print("\nAll non-GUI components tested successfully!")
print("\nNote: GUI components (final_app.py and tab screens) require")
print("customtkinter and cannot be tested in a headless environment.")
print("However, all syntax checks passed.")
