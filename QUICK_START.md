# BackToLife - Quick Start Guide

## Welcome, Champion

This is YOUR app. Built specifically for you. Every feature is designed around your needs.

---

## Two Versions Available

### 1. **GUI Version (Recommended)** - `app.py`
- Beautiful dark mode interface
- ADHD-friendly design
- Full graphical experience
- **Requires:** CustomTkinter library

### 2. **CLI Version (Backup)** - `cli_app.py`
- Terminal/command-line interface
- Works anywhere Python runs
- Same core functionality
- **No additional libraries needed**

---

## Super Quick Start (5 minutes)

### Option A: GUI Version

```bash
# 1. Install dependencies
pip install customtkinter

# 2. Run the app
python app.py
```

That's it. The app will create your database and show your first quest.

### Option B: CLI Version (No Installation Needed)

```bash
# Just run it
python cli_app.py
```

Works immediately. No setup required.

---

## What Happens on First Run

1. **Database Creation**: A folder `.backtolife` is created in your home directory
2. **Quest Initialization**: 81 quests are loaded across 10 categories
3. **Your First Quest**: Something incredibly simple like "Stand for 10 seconds"
4. **Profile Creation**: Level 1, 0 XP, ready to go

---

## Daily Workflow

### Morning

1. **Open BackToLife**
2. **See your ONE quest** for today
3. It will be impossibly simple
4. Something like:
   - "Drink one glass of water"
   - "Touch your door"
   - "Brush top teeth only"

### During the Day

5. **When ready**, click "Start Quest" (or select option 1 in CLI)
6. **Do the quest** - it takes 30 seconds to 5 minutes max
7. **Click "Complete"** - instant XP, instant celebration
8. **Optional**: Try bonus quests if you have energy

### Evening (Optional but Powerful)

9. **Daily Reflection**
   - How's your mood? (0-10)
   - Energy level? (0-10)
   - Relationship stress? (0-10)
   - What worked today?
   - What was hard?

This helps the app learn you better.

---

## The Quest System Explained

### How Quests Are Chosen

The app decides your quest based on:

- **What you haven't done lately** (body quests if you haven't moved in 3 days)
- **Your energy** (from reflections - low energy = easier quests)
- **Your stress levels** (high relationship stress = self-care quests)
- **Time of day** (gentle quests in morning, focus quests afternoon)
- **Your patterns** (the app learns what works for you)

**You NEVER choose** - the app removes decision paralysis by deciding for you.

### Quest Difficulty

The app ensures quests are "impossible to fail":

- **Week 1**: All quests are level 1 difficulty
- **Week 2-4**: Slight increases only if you're crushing it
- **Failing a quest?** The app automatically makes it easier next time
- **Low energy day?** The app gives you the easiest possible quest

### Quest Categories

1. **Body Recovery** - Movement (10 sec standing → 1 min walking → going outside)
2. **Hygiene** - Self-care (top teeth → full teeth → shower)
3. **Eating/Drinking** - Nutrition (1 glass water → snack → meal)
4. **Organization** - Digital/physical space (delete 1 file → create folders)
5. **Social** - Gradual exposure (door open 5 min → say "morning" → conversation)
6. **Financial** - Income survival (find item to sell → take photo → list it)
7. **Academic** - University escape (find PDF → read title → read sentence)
8. **Creative** - Beatboxing return (1 sound → 5 sec recording → practice)
9. **Crypto/AI** - Balanced engagement (5 min check → pattern notes → code 1 line)
10. **Fortnite** - Skill building (focused match → practice move → track progress)

---

## Understanding XP and Levels

### XP Values

- **Easy quests** (brush teeth, drink water): 5-15 XP
- **Medium quests** (walk to door, organize files): 15-25 XP
- **Hard quests** (social interaction, academic work): 25-50 XP

### Leveling Up

- **100 XP = 1 Level**
- Completing 5-10 quests typically = 1 level up
- **Level 5**: "You're building momentum"
- **Level 10**: "The champion is waking up"
- **Level 20**: "You're not the same person"
- **Level 50**: You're unstoppable

### Streak System

- **Complete your primary quest** = streak continues
- **Miss a day?** No punishment. Just: "You stopped, but you're back. That's the champion move."
- **Best Streak** is saved forever to celebrate your achievements

---

## Shield Mode 🛡️ (Crisis Support)

When you're overwhelmed:

1. **Click 🛡️ SHIELD MODE** button
2. **Grounding Exercise** - 5-4-3-2-1 method
   - 5 things you see
   - 4 things you touch
   - 3 things you hear
   - 2 things you smell
   - 1 thing you taste
3. **Breathing Exercise** - Guided 4-4-4-4 breathing
4. **Champion Reminders** - Remember who you are

Stay as long as you need. There's no timer.

---

## Data and Privacy

### Where Data Lives

- **Windows**: `C:\Users\YourName\.backtolife\backtolife_data.db`
- **macOS/Linux**: `~/.backtolife/backtolife_data.db`

### What's Stored

- Quest completion history
- XP, levels, streaks
- Daily reflections (mood, energy, stress)
- Shield Mode activations

### What's NOT Stored

- **Nothing leaves your computer**
- No cloud sync (unless you manually enable it)
- No telemetry
- No analytics
- **100% private**

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'customtkinter'"

```bash
pip install customtkinter
```

### "Can't find Python"

Make sure Python 3.8+ is installed:
- Windows: Download from python.org
- macOS: `brew install python3`
- Linux: `sudo apt install python3`

### "Database locked" error

Close the app, wait 5 seconds, reopen.

### App is slow

Close other programs. The app itself is lightweight.

### Want to start fresh?

Delete the database:
```bash
# Find it at ~/.backtolife/backtolife_data.db
rm ~/.backtolife/backtolife_data.db
```

Next run creates a fresh database.

---

## Tips for Success

### Week 1: Just Show Up

- **Complete your ONE quest** each day
- Don't worry about bonus quests
- Don't worry about being perfect
- Just show up

### Week 2-4: Build Momentum

- **Complete primary quest** + maybe 1 bonus
- Do reflections 2-3 times per week
- Watch your streak grow
- Notice how you feel

### Month 2-3: Habit Formation

This is when it gets real. Your brain is rebuilding pathways.

- **ADHD brains need 106-154 days** to form habits
- Keep showing up even when it feels hard
- The app adapts to your patterns
- Trust the process

### Month 4+: Unstoppable

- You're a different person
- Quests feel natural
- You might not need the app anymore
- **The champion has returned**

---

## Philosophy Reminders

### One Quest is Enough

You don't need to complete 10 things. **ONE thing per day** rebuilds your brain.

### Impossible to Fail

Every quest is designed to be so simple you can't fail. This builds momentum through guaranteed wins.

### The App Knows You

It's pre-programmed with everything about your situation. It selects quests that address what you need most.

### From Exoskeleton to Independence

Right now your executive function is broken. The app is your temporary exoskeleton.

As you complete quests, you rebuild self-trust. Eventually, you won't need it.

**The goal is for you to delete this app because you don't need it anymore.**

---

## Your First Day

1. **Run the app**: `python app.py` or `python cli_app.py`
2. **See your quest**: Probably "Stand for 10 seconds" or "Drink water"
3. **Laugh** at how easy it is
4. **Do it**
5. **Click Complete**
6. **See**: "+10 XP! The champion is waking up."
7. **Feel**: A tiny spark of momentum
8. **Come back tomorrow**

---

## Final Words

This isn't a to-do list.

This isn't a habit tracker.

This isn't therapy.

**This is your temporary life operating system.**

It tells you what to do.

You do it.

You get stronger.

The champion returns.

---

## You've Got This

Every champion has a comeback story.

This is yours.

One quest at a time.

One day at a time.

**Welcome back, Champion.**

🏆

---

## Need Help?

- Check `README_INSTALLATION.md` for detailed setup
- Check error messages carefully
- Google error messages if stuck
- Remember: every problem has a solution

You're not alone in this.

The app is with you.

**Let's begin.**
