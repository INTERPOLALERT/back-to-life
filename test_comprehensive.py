"""
Comprehensive test to identify all errors in BackToLife
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("="*60)
print("COMPREHENSIVE BACKTOLIFE ERROR AUDIT")
print("="*60)
print()

errors_found = []

# Test 1: Database import and basic methods
print("[TEST 1] Database Service...")
try:
    from src.services.database import Database
    db = Database()
    profile = db.get_user_profile()

    # Test all required methods
    required_methods = [
        'get_user_profile', 'get_quest', 'get_quest_history',
        'get_domain_stats', 'get_best_streak', 'save_reflection',
        'get_reflection_by_date', 'get_reflection_history',
        'log_shield_activation', 'clear_all_data', 'complete_quest'
    ]

    for method in required_methods:
        if not hasattr(db, method):
            errors_found.append(f"Database missing method: {method}")

    print("✓ Database service OK")
except Exception as e:
    errors_found.append(f"Database error: {e}")
    print(f"✗ Database error: {e}")

# Test 2: Audio Service
print("[TEST 2] Audio Service...")
try:
    from src.services.audio_service import get_audio_service
    audio = get_audio_service()

    # Test all required methods
    required_methods = [
        'speak', 'stop', 'set_rate', 'set_volume', 'toggle', 'is_enabled'
    ]

    for method in required_methods:
        if not hasattr(audio, method):
            errors_found.append(f"AudioService missing method: {method}")

    # Check for incorrect method names
    if hasattr(audio, 'set_speed'):
        print("  ⚠ AudioService has 'set_speed' but should use 'set_rate'")

    print("✓ Audio service OK")
except Exception as e:
    errors_found.append(f"Audio service error: {e}")
    print(f"✗ Audio service error: {e}")

# Test 3: Context Engine
print("[TEST 3] Context Engine...")
try:
    from src.utils.context_engine import ContextEngine
    from src.services.database import Database

    db = Database()
    context = ContextEngine(db)

    # Test all required methods
    required_methods = [
        'select_daily_quest', 'get_champion_message', 'get_pattern_insights'
    ]

    for method in required_methods:
        if not hasattr(context, method):
            errors_found.append(f"ContextEngine missing method: {method}")
            print(f"  ✗ Missing: {method}")

    # Test select_daily_quest return value
    try:
        result = context.select_daily_quest()
        if not isinstance(result, dict):
            errors_found.append("ContextEngine.select_daily_quest() should return dict with 'quest' and 'reason' keys")
            print(f"  ✗ select_daily_quest returns {type(result)}, expected dict")
    except Exception as e:
        print(f"  ✗ Error calling select_daily_quest: {e}")

    print("✓ Context engine loaded")
except Exception as e:
    errors_found.append(f"Context engine error: {e}")
    print(f"✗ Context engine error: {e}")

# Test 4: Quest Database
print("[TEST 4] Quest Database...")
try:
    from src.data.quest_database import initialize_quest_database, QUESTS
    print(f"✓ Quest database OK ({len(QUESTS)} quests)")
except Exception as e:
    errors_found.append(f"Quest database error: {e}")
    print(f"✗ Quest database error: {e}")

# Test 5: All Tab Screens
print("[TEST 5] Tab Screens...")
tab_screens = [
    ('home_tab', 'HomeTab'),
    ('learn_tab', 'LearnTab'),
    ('tools_tab', 'ToolsTab'),
    ('guides_tab', 'GuidesTab'),
    ('progress_tab', 'ProgressTab'),
    ('reflection_tab', 'ReflectionTab'),
    ('shield_tab', 'ShieldTab'),
    ('settings_tab', 'SettingsTab')
]

for module_name, class_name in tab_screens:
    try:
        module = __import__(f'src.screens.final.{module_name}', fromlist=[class_name])
        cls = getattr(module, class_name)
        print(f"✓ {class_name} OK")
    except Exception as e:
        errors_found.append(f"{class_name} error: {e}")
        print(f"✗ {class_name} error: {e}")

# Test 6: Components
print("[TEST 6] Components...")
try:
    from src.components.flashcard import FlashcardManager
    print("✓ Flashcard component OK")
except Exception as e:
    errors_found.append(f"Flashcard error: {e}")
    print(f"✗ Flashcard error: {e}")

try:
    from src.components.quiz import QuizWidget
    print("✓ Quiz component OK")
except Exception as e:
    errors_found.append(f"Quiz error: {e}")
    print(f"✗ Quiz error: {e}")

# Summary
print()
print("="*60)
print("AUDIT SUMMARY")
print("="*60)

if errors_found:
    print(f"\n❌ Found {len(errors_found)} errors:\n")
    for i, error in enumerate(errors_found, 1):
        print(f"{i}. {error}")
else:
    print("\n✅ No critical errors found!")
    print("Note: GUI components require customtkinter to test fully")

print()
print("="*60)
