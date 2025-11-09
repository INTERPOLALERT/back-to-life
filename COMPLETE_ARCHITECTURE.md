# BackToLife - Complete App Architecture
## Final Version - Nothing Missing

---

## App Structure Overview

```
BackToLife (Main Window)
├─ Navigation Sidebar (Always Visible)
│  ├─ 🏠 Home (Daily Quest)
│  ├─ 📚 Learn (Learning Center)
│  ├─ 🛠️ Tools (Tool Library)
│  ├─ 📖 Guides (How-To Library)
│  ├─ 📊 Progress (Stats & Growth)
│  ├─ 📝 Reflection (Daily Check-In)
│  ├─ 🛡️ Shield (Crisis Support)
│  └─ ⚙️ Settings
│
├─ Main Content Area (Changes Based on Tab)
└─ Quick Access Bar (Bottom - Context-Aware)
```

---

## 1. HOME TAB - Daily Quest System

### Features:
- **Current Quest Display** (enhanced with all learning)
- **Quest Progress** (steps, completion %)
- **Bonus Quests** (optional extras)
- **Today's Pattern Insight** (mini-report)
- **Quick Stats** (XP, level, streak)
- **Mood Check-In** (quick emoji selector)

### Layout:
```
┌────────────────────────────────────┐
│  🏠 HOME                      Lv 5 │
│  Good Morning, Champion      250 XP│
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                    │
│  💭 "You're building momentum"     │
│                                    │
│  🎯 TODAY'S QUEST                  │
│  ┌────────────────────────────┐  │
│  │ Body Recovery               │  │
│  │ Stand for 10 seconds        │  │
│  │                             │  │
│  │ [▶ START WITH GUIDANCE]     │  │
│  └────────────────────────────┘  │
│                                    │
│  📊 INSIGHT FOR TODAY              │
│  "Tuesdays work best for you"     │
│                                    │
│  ⚡ BONUS QUESTS (Optional)        │
│  • Drink water (+10 XP)           │
│  • Brush teeth (+5 XP)            │
│                                    │
│  🎭 How are you feeling?          │
│  😊 😐 😔 😰 😡                   │
└────────────────────────────────────┘
```

---

## 2. LEARN TAB - Learning Center

### Sections:

#### A. **Courses** (Progressive Learning Paths)
```
Available Courses:
├─ Understanding Your ADHD Brain (12 lessons)
├─ Executive Function Mastery (10 lessons)
├─ Relationship Boundaries 101 (8 lessons)
├─ Organization Systems (15 lessons)
├─ Emotional Regulation (10 lessons)
├─ Social Skills Rebuilt (12 lessons)
├─ Financial Literacy (8 lessons)
├─ Beatboxing Recovery (6 lessons)
└─ Self-Compassion Journey (10 lessons)
```

#### B. **Flashcard Library** (Spaced Repetition)
```
Categories:
├─ ADHD Facts (50 cards)
├─ Depression & Anxiety (40 cards)
├─ Relationship Skills (30 cards)
├─ Organization Tips (25 cards)
├─ Social Scripts (20 cards)
├─ Your Patterns (Dynamic - learns you)
└─ Coping Strategies (35 cards)

Review Status:
• Due Today: 3 cards
• Learning: 12 cards
• Mastered: 45 cards
```

#### C. **Interactive Quizzes**
```
Quiz Topics:
├─ ADHD Executive Function
├─ Boundary Setting
├─ Emotion Recognition
├─ Financial Decision Making
├─ Social Situation Navigation
├─ Organization Strategies
└─ Crisis Management
```

#### D. **Video/Audio Library**
```
Content Types:
├─ Psychoeducation Videos (TTS narrated)
├─ Guided Meditations (Shield Mode)
├─ Beatbox Tutorial Archive
├─ Champion Motivation Audio
└─ Skill Practice Sessions
```

### Layout:
```
┌────────────────────────────────────┐
│  📚 LEARNING CENTER                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                    │
│  🎓 COURSES IN PROGRESS            │
│  ┌─────────────────────┐          │
│  │ Understanding ADHD   │          │
│  │ Lesson 3/12         │          │
│  │ ████████░░░░ 67%    │          │
│  └─────────────────────┘          │
│                                    │
│  💡 FLASHCARDS DUE TODAY (3)       │
│  [Review Now]                      │
│                                    │
│  🎯 RECOMMENDED FOR YOU            │
│  • Relationship Boundaries 101     │
│  • Organization Systems            │
│                                    │
│  📖 BROWSE ALL                     │
│  [Courses] [Flashcards] [Quizzes] │
└────────────────────────────────────┘
```

---

## 3. TOOLS TAB - Comprehensive Tool Library

### Tool Categories:

#### A. **Mood-Based Tools**
```
"I feel..."
├─ Overwhelmed → Grounding exercises, Shield Mode
├─ Anxious → Breathing exercises, Worry worksheet
├─ Depressed → Behavioral activation, Achievement log
├─ Angry → Emotion wheel, Cooling strategies
├─ Lonely → Connection prompts, Social scripts
├─ Stressed → Time management, Priority matrix
├─ Confused → Decision tree, Clarity questions
└─ Stuck → Task breakdown, First step finder
```

#### B. **Situation-Based Tools**
```
"I need help with..."
├─ Money Decision → Budget calculator, Spending tracker
├─ Girlfriend Request → Boundary script generator
├─ File Organization → Desktop scanner, Folder wizard
├─ Social Interaction → Script library, Practice mode
├─ Time Management → Visual timeline, Task estimator
├─ Crypto Checking → Limit setter, Reality anchor
├─ Motivation → Champion audio, Past wins review
└─ Crisis → Emergency protocols, Contact list
```

#### C. **Skill-Building Tools**
```
Tools:
├─ Task Breakdown AI (Goblin Tools style)
├─ Time Estimator (Tiimo style)
├─ Text Tone Adjuster (formal/casual)
├─ Social Script Generator
├─ Boundary Statement Creator
├─ Decision Tree Walker
├─ Habit Tracker
├─ Routine Builder
├─ Goal Decomposer
└─ Pattern Analyzer
```

#### D. **Quick Actions**
```
One-Click Tools:
├─ 🔊 Audio Guidance Toggle
├─ ⏱️ 5-Minute Timer
├─ 🧘 Quick Grounding (60 seconds)
├─ 💬 Text Your Sister (pre-written)
├─ 💰 Check Budget Summary
├─ 📱 Crypto Check Limit Reminder
├─ 🎵 Play Champion Audio
└─ 📝 Quick Note (voice or text)
```

### Layout:
```
┌────────────────────────────────────┐
│  🛠️ TOOLS                          │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                    │
│  🎭 HOW ARE YOU FEELING?           │
│  [Overwhelmed] [Anxious] [Stuck]  │
│  [Depressed] [Angry] [Confused]   │
│                                    │
│  💡 RECOMMENDED FOR YOU            │
│  Based on your patterns:           │
│  • Task Breakdown Tool             │
│  • Boundary Script Generator       │
│  • Time Estimator                  │
│                                    │
│  🔍 BROWSE ALL TOOLS               │
│  [By Feeling] [By Situation]      │
│  [By Skill] [Quick Actions]       │
│                                    │
│  ⭐ FAVORITES                       │
│  • Desktop Organizer               │
│  • Crypto Limit Reminder           │
│  • 5-Minute Grounding              │
└────────────────────────────────────┘
```

---

## 4. GUIDES TAB - How-To Library

### Guide Categories:

#### A. **Daily Living Guides**
```
├─ Morning Routine Builder
├─ Evening Wind-Down Sequence
├─ Hygiene Step-by-Steps
├─ Meal Planning for ADHD
├─ Sleep Hygiene Protocol
├─ Energy Management
└─ Pain Management (Knees)
```

#### B. **Relationship Guides**
```
├─ Setting Boundaries with Girlfriend
├─ Managing Money Requests
├─ Communication Scripts Library
├─ Conflict Resolution Steps
├─ Long-Distance Relationship Tips
├─ Codependency Recovery
└─ Healthy vs Unhealthy Patterns
```

#### C. **Organization Guides**
```
├─ Desktop Organization System
├─ File Naming Conventions
├─ Email Management
├─ Paper Organization
├─ Digital Decluttering
├─ Maintaining Systems
└─ Weekly Reset Routine
```

#### D. **Social Guides**
```
├─ Conversation Starters
├─ Small Talk Survival
├─ Saying No Politely
├─ Asking for Help
├─ Reading Social Cues
├─ Making Eye Contact
└─ Body Language Basics
```

#### E. **Financial Guides**
```
├─ Budget Creation
├─ Debt Tracking
├─ Income Ideas (Non-9-5)
├─ Selling on Vinted
├─ Crypto Check Guidelines
├─ Saving Strategies
└─ Financial Boundaries
```

#### F. **Academic Guides**
```
├─ Finding Exam PDFs
├─ Breaking Down Assignments
├─ Study Techniques for ADHD
├─ Exam Preparation
├─ Submission Checklists
└─ University Communication
```

#### G. **Creative Guides**
```
├─ Beatbox Warm-Ups
├─ Voice Recovery Exercises
├─ Recording Setup
├─ Practice Schedules
├─ Performance Anxiety
└─ Rebuilding Confidence
```

### Layout:
```
┌────────────────────────────────────┐
│  📖 GUIDES                         │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                    │
│  🔍 SEARCH GUIDES                  │
│  [____________________________]    │
│                                    │
│  ⭐ RECOMMENDED FOR YOU            │
│  • Setting Boundaries with GF      │
│  • Desktop Organization System     │
│  • Managing Money Requests         │
│                                    │
│  📚 BROWSE BY CATEGORY             │
│  [Daily Living] [Relationships]   │
│  [Organization] [Social]          │
│  [Financial] [Academic]           │
│  [Creative]                       │
│                                    │
│  📌 RECENTLY VIEWED                │
│  • Morning Routine Builder         │
│  • Saying No Politely              │
└────────────────────────────────────┘
```

---

## 5. PROGRESS TAB - Stats & Growth

### Sections:

#### A. **Overview Dashboard**
```
Key Metrics:
├─ Current Level & XP
├─ Streak (current & best)
├─ Total Quests Completed
├─ Skills Mastered
├─ Courses Completed
├─ Flashcards Mastered
└─ Days Active
```

#### B. **Domain Progress**
```
Life Domains (Visual):
├─ Body Recovery: ████████░░ 80%
├─ Hygiene: ██████░░░░ 60%
├─ Social: ████░░░░░░ 40%
├─ Financial: ███░░░░░░░ 30%
├─ Organization: █████░░░░░ 50%
├─ Academic: ██░░░░░░░░ 20%
├─ Creative: ████░░░░░░ 40%
├─ Crypto/AI: ██████░░░░ 60%
└─ Fortnite: ████████░░ 80%
```

#### C. **Skill Trees**
```
Skills:
├─ Organization Level 3
│  ├─ ✓ Single File
│  ├─ ✓ Multiple Files
│  ├─ ✓ Folder Creation
│  ├─ → Folder Structure
│  └─ → Daily Maintenance
│
├─ Boundaries Level 2
│  ├─ ✓ Recognizing Violations
│  ├─ ✓ Saying "I need to think"
│  ├─ → Saying "No"
│  ├─ → Setting Limits
│  └─ → Enforcing Boundaries
│
└─ (All 20 skill trees)
```

#### D. **Pattern Insights**
```
Weekly Report:
├─ Best Day: Tuesday (80% completion)
├─ Hardest Day: Monday (30% completion)
├─ Best Time: 2-4 PM
├─ Triggers Detected: 3
├─ Correlations Found: 5
└─ Recommendations: 4
```

#### E. **Achievements**
```
Unlocked:
├─ 🏆 First Quest (Day 1)
├─ 🔥 7-Day Streak
├─ 📚 First Course Complete
├─ 💪 10 Body Quests
├─ 🧠 ADHD Expert (50 flashcards)
└─ (50+ achievements)
```

### Layout:
```
┌────────────────────────────────────┐
│  📊 PROGRESS                       │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                    │
│  🏆 LEVEL 5 ━━━━━━━━━━ 250/500 XP│
│  🔥 STREAK: 12 days (Best: 15)    │
│                                    │
│  📈 GROWTH THIS WEEK               │
│  Quests: 5  |  XP: +120  |  📈+15%│
│                                    │
│  🎯 DOMAIN BALANCE                 │
│  [Circular chart visualization]   │
│                                    │
│  🌟 LATEST ACHIEVEMENT             │
│  "Week Warrior" - 7 consecutive   │
│                                    │
│  📊 DETAILED STATS                 │
│  [Domains] [Skills] [Patterns]    │
│  [Achievements] [History]         │
└────────────────────────────────────┘
```

---

## 6. REFLECTION TAB - Daily Check-In

### Features:

#### A. **Mood Tracking**
```
Sliders:
├─ Overall Mood (0-10)
├─ Energy Level (0-10)
├─ Anxiety (0-10)
├─ Depression (0-10)
├─ Relationship Stress (0-10)
├─ Physical Pain (0-10)
└─ Motivation (0-10)
```

#### B. **Journal Prompts**
```
Questions:
├─ What worked today?
├─ What was difficult?
├─ What triggered stress?
├─ What made you proud?
├─ What do you need tomorrow?
├─ Grateful for? (optional)
└─ Any insights? (optional)
```

#### C. **Voice or Text Entry**
```
Options:
├─ 🎤 Voice Record (transcribed)
├─ ⌨️ Type Response
├─ 📝 Guided Prompts
└─ 😊 Emoji-Only Mode
```

#### D. **Pattern Visualization**
```
Charts:
├─ Mood Trends (30 days)
├─ Energy Patterns (weekly)
├─ Trigger Frequency
├─ Correlation Heatmap
└─ Best/Worst Days
```

### Layout:
```
┌────────────────────────────────────┐
│  📝 DAILY REFLECTION               │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                    │
│  How are you feeling right now?    │
│                                    │
│  Overall Mood                      │
│  😔 ●━━━━━━━━━ 😊 (5/10)         │
│                                    │
│  Energy Level                      │
│  💤 ━━━●━━━━━━ ⚡ (3/10)         │
│                                    │
│  Relationship Stress               │
│  😌 ━━━━━━━●━━ 😰 (7/10)         │
│                                    │
│  📝 QUICK JOURNAL                  │
│  [Voice Record] [Type]             │
│                                    │
│  What worked today?                │
│  [________________________]        │
│                                    │
│  [Save Reflection]                 │
│                                    │
│  📊 [View Patterns]                │
└────────────────────────────────────┘
```

---

## 7. SHIELD TAB - Crisis Support

### Features:

#### A. **Emergency Actions**
```
Immediate Help:
├─ 🆘 Crisis Hotline (988)
├─ 💬 Text Crisis Line
├─ 📞 Call Sister
├─ 🏥 Emergency Services
└─ 🛡️ Enter Safe Mode
```

#### B. **Grounding Exercises**
```
Techniques:
├─ 5-4-3-2-1 Grounding
├─ 4-7-8 Breathing
├─ Body Scan Meditation
├─ Progressive Muscle Relaxation
├─ Sensory Grounding
├─ Visualization
└─ Counting Exercises
```

#### C. **Champion Reminders**
```
Affirmations:
├─ Your Past Achievements
├─ Your Strengths List
├─ Champion Audio Playback
├─ Beatbox Recordings
├─ Photos from Good Days
└─ Messages from Sister
```

#### D. **Crisis Plan**
```
Your Safety Plan:
├─ Warning Signs Checklist
├─ Internal Coping Strategies
├─ People/Places for Distraction
├─ Contacts for Help
├─ Professional Resources
└─ Reasons to Live
```

### Layout:
```
┌────────────────────────────────────┐
│  🛡️ SHIELD MODE                    │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                    │
│  You're safe here. Take your time. │
│                                    │
│  🆘 EMERGENCY                       │
│  [Call 988] [Text Crisis Line]    │
│                                    │
│  🧘 GROUNDING                       │
│  [5-4-3-2-1] [Breathing]          │
│  [Body Scan] [Muscle Relaxation]  │
│                                    │
│  💪 CHAMPION REMINDERS             │
│  [Past Wins] [Strengths]          │
│  [Play Audio] [View Photos]       │
│                                    │
│  📋 YOUR SAFETY PLAN               │
│  [View Plan] [Update Plan]        │
│                                    │
│  📞 QUICK CONTACTS                 │
│  [Sister] [Friend] [Therapist]    │
│                                    │
│  [I'm Feeling Better →]            │
└────────────────────────────────────┘
```

---

## 8. SETTINGS TAB

### Options:

#### A. **Audio Settings**
```
├─ Enable/Disable Audio
├─ Voice Speed (50-300 WPM)
├─ Voice Volume (0-100%)
├─ Auto-Play (On/Off)
└─ Voice Selection (if available)
```

#### B. **Notification Settings**
```
├─ Daily Quest Reminder
├─ Flashcard Review Reminder
├─ Reflection Reminder
├─ Streak Maintenance Alert
├─ Pattern Insight Notifications
└─ Achievement Unlocks
```

#### C. **Display Settings**
```
├─ Dark/Light Mode
├─ Font Size (Small/Medium/Large/XL)
├─ Color Scheme
├─ Animation Speed
├─ Compact/Spacious Layout
└─ Mobile/Desktop View
```

#### D. **Privacy Settings**
```
├─ Data Backup (Local/Cloud)
├─ Export Data
├─ Clear History
├─ Anonymous Analytics (On/Off)
└─ Screen Lock
```

#### E. **Profile Settings**
```
├─ Your Name
├─ Your Goals
├─ Crisis Contacts
├─ Therapist Info (optional)
├─ Medication Reminders
└─ Custom Quest Preferences
```

---

## 9. QUICK ACCESS BAR (Bottom) - Context-Aware

### Always Visible:
```
┌─────────────────────────────────────┐
│ 🎯 Quest  📚 Learn  🛡️ Shield  ⚙️  │
└─────────────────────────────────────┘
```

### Changes Based on Context:
```
During Quest:
│ ⏸️ Pause  🔊 Audio  ← Back  Next → │

During Learning:
│ 💡 Card  🎯 Quiz  📖 Guide  ✓ Done │

In Crisis:
│ 🆘 Help  🧘 Ground  💬 Contact  🔙 │
```

---

## Mobile-Friendly Design Principles

### Responsive Breakpoints:
```
├─ Desktop: 1024px+ (Full sidebar, multi-column)
├─ Tablet: 768-1023px (Collapsible sidebar, 2-column)
├─ Mobile: <768px (Bottom nav, single column)
```

### Mobile Adaptations:
```
├─ Bottom navigation instead of sidebar
├─ Swipe gestures between tabs
├─ Larger touch targets (48px minimum)
├─ Collapsible sections
├─ Simplified layouts
├─ Voice input prioritized
└─ One-handed operation optimized
```

---

## Data Architecture

### Databases:
```
Main Database (SQLite):
├─ user_profile
├─ quests (all enhanced quests)
├─ quest_history
├─ flashcard_reviews
├─ quiz_results
├─ courses_progress
├─ reflections (mood/journal)
├─ domain_tracking
├─ skill_progress
├─ achievements
├─ tool_usage
├─ pattern_insights
├─ crisis_log
└─ settings
```

---

## Implementation Priority

### Phase 1 (Core - Week 1):
1. Navigation framework
2. Enhanced quest system (all 81 quests)
3. Audio service (all screens)
4. Flashcard system
5. Quiz system

### Phase 2 (Learning - Week 2):
6. Learning Center (courses)
7. Flashcard library
8. Quiz library
9. Guide system

### Phase 3 (Tools - Week 3):
10. Tool library
11. Mood-based selector
12. Situation-based tools
13. Quick actions

### Phase 4 (Analysis - Week 4):
14. Pattern recognition
15. Progress analytics
16. Reflection system
17. Insights engine

### Phase 5 (Polish - Week 5):
18. Mobile responsiveness
19. All audio narration
20. Settings & customization
21. Testing & refinement

---

This is the COMPLETE architecture. Nothing missing.

Ready to build?
