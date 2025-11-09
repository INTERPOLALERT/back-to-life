"""
BackToLife - Command Line Interface Version
For testing and environments without GUI support
"""
import sys
import os
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.database import Database
from src.data.quest_database import initialize_quest_database
from src.utils.context_engine import ContextEngine


class BackToLifeCLI:
    def __init__(self):
        self.db = Database()
        initialize_quest_database(self.db)
        self.context_engine = ContextEngine(self.db)
        self.running = True

    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        """Print app header"""
        print("=" * 60)
        print("🏆  BACKTOLIFE - Your Champion Journey  🏆")
        print("=" * 60)
        print()

    def show_profile(self):
        """Display user profile"""
        profile = self.db.get_user_profile()
        print(f"Level: {profile['level']}  |  XP: {profile['xp']}  |  Streak: {profile['streak']} days")
        print(f"Best Streak: {profile['best_streak']} days")
        print()
        champion_msg = self.context_engine.get_champion_message(profile)
        print(f"💭 {champion_msg}")
        print()

    def show_main_menu(self):
        """Display main menu"""
        self.clear_screen()
        self.print_header()
        self.show_profile()

        print("=" * 60)
        print("MAIN MENU")
        print("=" * 60)
        print()
        print("1. View Today's Quest")
        print("2. View Progress")
        print("3. Daily Reflection")
        print("4. Shield Mode (Crisis Support)")
        print("5. Exit")
        print()

        choice = input("Choose an option (1-5): ").strip()
        return choice

    def show_daily_quest(self):
        """Display today's quest"""
        self.clear_screen()
        self.print_header()

        # Check if completed today
        completed_today = self.db.get_today_completed_quests()

        if completed_today:
            print("✨ TODAY'S QUEST COMPLETE ✨")
            print()
            print("You did it, Champion.")
            print("Rest now, or come back tomorrow for your next quest.")
            print()
            input("Press Enter to continue...")
            return

        # Get today's quest
        quest = self.context_engine.select_daily_quest()

        if not quest:
            print("No quest available. This shouldn't happen!")
            input("Press Enter to continue...")
            return

        print("🎯 TODAY'S QUEST")
        print("=" * 60)
        print()

        category = quest[1].replace('_', ' ').title()
        print(f"Category: {category}")
        print()

        print(f"📋 {quest[2]}")  # title
        print()
        print(f"Description: {quest[3]}")  # description
        print()

        time_of_day = self.context_engine.get_time_of_day()
        why_text = self.context_engine.get_context_aware_why_message(quest, time_of_day)
        print(f"💡 Why: {why_text}")
        print()

        print(f"Instructions:")
        print(f"  {quest[9]}")  # instructions (index 9)
        print()

        print(f"XP Reward: {quest[5]} XP")
        print()

        print("-" * 60)
        print()
        print("Ready to complete this quest?")
        print("1. Mark as Complete")
        print("2. Back to Menu")
        print()

        choice = input("Choose (1-2): ").strip()

        if choice == '1':
            self.complete_quest(quest)

    def complete_quest(self, quest):
        """Mark quest as complete"""
        quest_id = quest[0]
        xp_earned = quest[5]

        leveled_up = self.db.complete_quest(quest_id, xp_earned, was_primary=True)

        self.clear_screen()
        self.print_header()

        print("✨" * 30)
        print()
        print("        🏆 QUEST COMPLETE! 🏆")
        print()
        print(f"           +{xp_earned} XP")
        print()
        print("✨" * 30)
        print()

        if leveled_up:
            profile = self.db.get_user_profile()
            print("🎉" * 30)
            print()
            print(f"       ⭐ LEVEL UP! LEVEL {profile['level']} ⭐")
            print()
            print("      You're becoming unstoppable.")
            print()
            print("🎉" * 30)
            print()

        print("The champion is waking up.")
        print()
        input("Press Enter to continue...")

    def show_progress(self):
        """Display progress statistics"""
        self.clear_screen()
        self.print_header()

        stats = self.db.get_stats()
        profile = stats['profile']

        print("📊 YOUR PROGRESS")
        print("=" * 60)
        print()

        print(f"Level: {profile['level']}")
        print(f"Total XP: {profile['xp']}")
        print(f"XP to Next Level: {self.db.xp_for_next_level(profile['xp'])}")
        print()

        print(f"Current Streak: {profile['streak']} days")
        print(f"Best Streak: {profile['best_streak']} days")
        print()

        print(f"Total Quests Completed: {stats['total_quests']}")
        print(f"Quests This Week: {stats['quests_this_week']}")
        print()

        if stats['quests_by_category']:
            print("Quests by Category:")
            print("-" * 60)
            for category, count in stats['quests_by_category'][:8]:
                category_name = category.replace('_', ' ').title()
                print(f"  {category_name}: {count}")
            print()

        input("Press Enter to continue...")

    def show_reflection(self):
        """Daily reflection"""
        self.clear_screen()
        self.print_header()

        print("📝 DAILY REFLECTION")
        print("=" * 60)
        print()

        print("How are you feeling right now?")
        print()

        # Mood rating
        while True:
            try:
                mood = int(input("Overall Mood (0-10): ").strip())
                if 0 <= mood <= 10:
                    break
                print("Please enter a number between 0 and 10")
            except ValueError:
                print("Please enter a valid number")

        # Energy level
        while True:
            try:
                energy = int(input("Energy Level (0-10): ").strip())
                if 0 <= energy <= 10:
                    break
                print("Please enter a number between 0 and 10")
            except ValueError:
                print("Please enter a valid number")

        # Relationship stress
        while True:
            try:
                stress = int(input("Relationship Stress (0-10): ").strip())
                if 0 <= stress <= 10:
                    break
                print("Please enter a number between 0 and 10")
            except ValueError:
                print("Please enter a valid number")

        print()
        what_worked = input("What worked well today? ").strip()
        what_hard = input("What was difficult today? ").strip()
        grateful = input("One thing you're grateful for (optional)? ").strip()

        # Save reflection
        self.db.save_reflection(
            mood_rating=mood,
            what_worked=what_worked,
            what_was_hard=what_hard,
            grateful_for=grateful,
            energy_level=energy,
            relationship_stress=stress
        )

        print()
        print("✅ Reflection saved. Thank you for taking time to reflect.")
        print()
        input("Press Enter to continue...")

    def show_shield_mode(self):
        """Shield Mode - crisis support"""
        self.clear_screen()
        print()
        print("🛡️" * 30)
        print()
        print("          SHIELD MODE ACTIVATED")
        print()
        print("🛡️" * 30)
        print()

        activation_id = self.db.record_shield_activation("CLI initiated")

        print("You're safe here. Take your time.")
        print()
        print("=" * 60)
        print("🧘 GROUNDING EXERCISE - 5-4-3-2-1 Method")
        print("=" * 60)
        print()
        print("Name out loud (or in your head):")
        print()
        print("  • 5 things you can see")
        print("  • 4 things you can touch")
        print("  • 3 things you can hear")
        print("  • 2 things you can smell")
        print("  • 1 thing you can taste")
        print()
        print("There's no rush. Take as long as you need.")
        print()
        print("=" * 60)
        print()

        input("Press Enter when you're ready to continue...")
        print()

        print("REMEMBER, CHAMPION:")
        print("-" * 60)
        print("  • This feeling will pass")
        print("  • You've survived every hard day before this")
        print("  • You don't have to do anything right now")
        print("  • Just breathe. Just exist. That's enough.")
        print("  • The champion inside you is still there")
        print()

        input("Press Enter when you're feeling better...")
        print()
        print("✨ Shield Mode deactivated. You did great.")
        print()
        input("Press Enter to continue...")

    def run(self):
        """Main application loop"""
        while self.running:
            choice = self.show_main_menu()

            if choice == '1':
                self.show_daily_quest()
            elif choice == '2':
                self.show_progress()
            elif choice == '3':
                self.show_reflection()
            elif choice == '4':
                self.show_shield_mode()
            elif choice == '5':
                self.clear_screen()
                print()
                print("Thank you for using BackToLife.")
                print("See you tomorrow, Champion.")
                print()
                self.running = False
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")


if __name__ == "__main__":
    app = BackToLifeCLI()
    app.run()
