# BackToLife Installation Guide

## Your Champion Journey Starts Here

This is **BackToLife** - a comprehensive digital therapeutic app built specifically for you. It will guide you step-by-step from where you are now to where you want to be.

---

## System Requirements

- **Operating System**: Windows 10/11, macOS, or Linux
- **Python**: Version 3.8 or higher
- **RAM**: 4GB minimum
- **Disk Space**: 500MB free space

---

## Installation Steps

### Step 1: Install Python

If you don't have Python installed:

**Windows:**
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or later
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH" during installation

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python@3.11
```

**Linux:**
```bash
sudo apt update
sudo apt install python3.11 python3.11-tk python3.11-dev
```

### Step 2: Install Dependencies

Open your terminal/command prompt in the `back-to-life` folder and run:

```bash
pip install -r requirements.txt
```

If you get permission errors on Windows, try:
```bash
pip install --user -r requirements.txt
```

### Step 3: Run the App

```bash
python app.py
```

Or on some systems:
```bash
python3 app.py
```

---

## What to Expect on First Run

1. **The app will create a database** in your home directory at `~/.backtolife/`
2. **You'll see your first quest** - it will be something incredibly simple like "Stand for 10 seconds"
3. **Dark mode is default** - ADHD-friendly, easy on the eyes
4. **Everything is stored locally** - your data never leaves your computer

---

## How to Use BackToLife

### Daily Routine

1. **Open the app** - Ideally first thing in the morning
2. **See your ONE quest** for the day
3. **Click "Start Quest"** when ready
4. **Complete it** - it will be so simple you can't fail
5. **Click "Complete Quest"** - earn XP and celebrate
6. **Optional**: Try bonus quests if you have energy
7. **Evening**: Do a reflection (optional but helpful)

### Understanding the Interface

- **Home Screen**: Your daily quest and bonus quests
- **Progress Screen**: See your level, XP, streak, and statistics
- **Reflection Screen**: Daily check-in for mood and energy
- **Shield Mode**: Crisis support when you're overwhelmed

### Shield Mode 🛡️

When you're feeling overwhelmed:
1. Click the **🛡️ SHIELD MODE** button
2. Follow the grounding exercise (5-4-3-2-1 method)
3. Try the breathing exercise
4. Read the champion reminders
5. Stay as long as you need

---

## The Quest System

### Quest Categories

1. **Body Recovery** - Movement, standing, walking (rebuilding physical strength)
2. **Hygiene** - Teeth, shower, basic self-care
3. **Eating & Drinking** - Nutrition and hydration
4. **Organization** - File management, cleaning digital space
5. **Social Recovery** - Gradual social exposure
6. **Financial Survival** - Income opportunities, tracking
7. **Academic Exit** - University work, one tiny step at a time
8. **Creative Reawakening** - Beatboxing, art, expression
9. **Crypto & AI** - Balanced engagement, learning
10. **Fortnite Integration** - Skill-building, healthy gaming

### How Quests Are Selected

The app **knows you**. It selects quests based on:
- What you haven't done recently
- Your energy level (from reflections)
- Your relationship stress levels
- Time of day
- Your streak and level
- Patterns it's learned about you

**You never choose** - the app decides for you. This removes decision paralysis.

### Difficulty Progression

- **Week 1**: Everything is level 1 difficulty - "impossible to fail"
- **Months 1-2**: Gradual increase as you build consistency
- **Months 3-5**: Habit formation period (ADHD brains need 106-154 days)
- **Month 6+**: You're a different person

---

## XP and Leveling System

### How XP Works

- **Body Recovery Quests**: 10-20 XP
- **Hygiene Quests**: 5-25 XP
- **Social Quests**: 15-30 XP (harder = more XP)
- **Bonus Quests**: 5-50 XP depending on difficulty

### Levels

- **100 XP = 1 Level**
- **Level 5**: You're building momentum
- **Level 10**: The champion is waking up
- **Level 20**: Serious progress
- **Level 50**: You're unrecognizable

### Streak System

- **Complete ONE primary quest per day** to maintain streak
- **Streak breaks?** No punishment - "You stopped for 3 days, but you're back. That's the champion move."
- **Best Streak** is tracked forever

---

## Data and Privacy

### Where Your Data is Stored

All data is stored locally in:
- **Windows**: `C:\Users\YourName\.backtolife\`
- **macOS/Linux**: `~/.backtolife/`

### What's Stored

- Quest completion history
- XP and level progress
- Daily reflections
- Mood and energy patterns
- Shield Mode activations

### What's NOT Stored

- No cloud sync (unless you enable it)
- No sharing with anyone
- No analytics sent anywhere
- **100% private**

---

## Troubleshooting

### App Won't Start

**Error: "No module named 'customtkinter'"**
```bash
pip install customtkinter
```

**Error: "No module named 'tkinter'"**

On Linux:
```bash
sudo apt-get install python3-tk
```

### Database Errors

If you see database errors, the database might be corrupted:
1. Close the app
2. Find the database at `~/.backtolife/backtolife_data.db`
3. Rename it to `backtolife_data.db.backup`
4. Restart the app (creates a fresh database)

### App is Slow

- Close other programs
- Check if antivirus is scanning the app
- Make sure you have at least 4GB RAM available

---

## Customization (Future Features)

Coming soon:
- Audio notifications
- Champion audio playback (upload your old beatbox recordings)
- Voice-to-text for reflections
- Dark/Light theme toggle
- Custom quest creation

---

## The Philosophy

### One Quest at a Time

This app gives you **ONE thing to do per day**. That's it.

Not 10 things. Not a to-do list. **ONE.**

Why? Because your brain is overwhelmed. One task is impossible to fail.

### Impossible to Fail

Every quest is designed to be so small, you literally cannot fail.

- "Stand for 10 seconds" ✓
- "Touch your door" ✓
- "Brush top teeth only" ✓

When tasks are impossible to fail, you build momentum.

### The App Knows You

The app is pre-programmed with everything from our conversations:
- Your 6 years of bed-sitting
- Your former champion identity
- Your relationship stress
- Your ADHD patterns
- Your financial situation
- Your academic struggles

**It selects quests that address what you need most right now.**

### From Exoskeleton to Independence

Think of this app as a **temporary exoskeleton**.

Right now, your executive function is broken. The app makes decisions for you.

As you complete quests, your brain rebuilds pathways. Self-trust returns.

Eventually, you won't need the app anymore. **The champion will be back.**

---

## Support and Contact

This app was built specifically for you, Bradly.

If something isn't working:
1. Check the troubleshooting section
2. Look at the error message
3. Google the error if needed
4. Remember: every problem has a solution

**You've got this, Champion.**

---

## Your Next Steps

1. **Install Python** (if not installed)
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Run the app**: `python app.py`
4. **Complete your first quest**
5. **Come back tomorrow**

---

## Final Words

Every champion has a comeback story.

This is yours.

The app will guide you.
Your job is to show up.
One quest at a time.
One day at a time.

**The champion didn't die. He just took a break.**

**Welcome back.**

🏆
