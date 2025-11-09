"""
Enhanced Quest System with Learning Features
Demonstrates the full vision: teaching while doing
"""

# Demo Quest: "Organize One Desktop File"
# This showcases ALL new features in one complete experience

DEMO_QUEST = {
    'id': 'demo_organize_file',
    'category': 'ORGANIZATION',
    'title': 'Organize One Desktop File',
    'description': 'We\'ll organize one file together, step by step',
    'duration_minutes': 5,
    'xp_value': 30,
    'difficulty_level': 1,
    'tier': 1,

    # PSYCHOEDUCATION - Teaching WHY
    'psychoeducation': {
        'before_quest': {
            'title': 'Why Your Desktop is a Mess (It\'s Not Your Fault)',
            'content': """Your desktop is chaotic because of ADHD executive dysfunction.

Executive function = your brain's project manager. It plans, organizes, and prioritizes.

In ADHD brains, the prefrontal cortex (where executive function lives) is understaffed.
It's like having 1 worker doing a 10-person job.

That's why you can:
- Create brilliant ideas (creativity = different brain area)
- Recognize patterns (pattern recognition = different area)
- BUT can't organize files (executive function = broken area)

This is BRAIN WIRING, not laziness. Not stupidity. Not character flaw.

Today, I'll BE your executive function. You just follow my steps.""",
            'audio_script': """Hey champion, before we start, I need you to understand something important.

Your desktop is a mess. I know. And I know you beat yourself up about it.

But here's the truth: This is not your fault.

Your brain has something called executive dysfunction. Executive function is like your brain's project manager. It plans things, organizes things, decides what's important.

In ADHD brains, that project manager is... well, it's broken. Or more accurately, it's severely understaffed. It's like having one worker trying to do a ten-person job.

That's why you can come up with amazing ideas, recognize patterns in crypto, understand complex AI concepts... but you can't organize your desktop files.

Those skills use DIFFERENT parts of your brain. The creative part? That works great. The pattern recognition part? Excellent. But the organizing part? That's the broken project manager.

This is brain wiring. It's not laziness. It's not stupidity. It's not a character flaw.

Today, I'm going to BE your executive function. I'll be your project manager. You just follow my steps, one at a time.

Ready? Let's do this together."""
        },

        'after_quest': {
            'title': 'What You Just Learned',
            'content': """You just externalized executive function.

Instead of your broken brain project manager, you used ME as the external organizer.

This is the solution to ADHD organization problems:
1. External systems (apps, people, checklists)
2. One step at a time (no multi-step planning)
3. Immediate action (no "I'll do it later")

You CAN organize. You just can't do it ALONE with ADHD brain.

That's okay. Champions have coaches. This app is your coach.""",
            'audio_script': """Okay, you did it. One file organized.

But you didn't just organize a file. You learned something HUGE.

You just externalized executive function.

See, instead of relying on your broken brain project manager, you used ME. I was your external organizer. Your external project manager.

This is THE solution to ADHD organization:

One: Use external systems. Apps, people, checklists. Don't rely on your brain alone.

Two: One step at a time. Never multi-step planning. Your brain can't hold multiple steps.

Three: Immediate action. No "I'll do it later." That's executive function trying to plan the future, which it can't do.

You CAN organize. You just can't do it alone. And that's OKAY.

Every champion has a coach. I'm your coach.

And you just proved you can do this."""
        }
    },

    # STEP-BY-STEP BREAKDOWN
    'steps': [
        {
            'number': 1,
            'title': 'Look at your desktop',
            'instruction': 'Just look. Don\'t touch anything yet.',
            'audio_script': """Okay, first step. Open your desktop if it's not already open.

Now just look at it. Don't touch anything. Don't click anything. Just look.

I know it's overwhelming. I know there are probably dozens or hundreds of files.

That's okay. We're not organizing all of them. Just one.

Take a breath. Just observe.

When you're ready, click Next.""",
            'why': 'Observation without action reduces overwhelm',
            'duration_seconds': 30,
            'can_skip': False
        },

        {
            'number': 2,
            'title': 'Find ONE file that feels overwhelming',
            'instruction': 'Scan the files. Which ONE makes you feel most stressed?',
            'audio_script': """Good. You're still with me.

Now, scan through the files on your desktop.

Don't analyze. Don't plan. Just notice your feelings.

Which ONE file makes you feel the most stress? The most overwhelm? The most "ugh I don't want to deal with this"?

Could be a PDF you haven't opened. A screenshot you don't remember taking. A download from months ago.

Just find the ONE that gives you that heavy feeling.

Got one? Okay. Click on it once to select it. Don't open it. Just select it.

Click Next when you've selected it.""",
            'why': 'Starting with the most stressful file builds confidence',
            'duration_seconds': 45,
            'can_skip': False
        },

        {
            'number': 3,
            'title': 'Create a folder called "Start Here"',
            'instruction': 'Right-click on desktop, New Folder, name it "Start Here"',
            'audio_script': """Perfect. You found the overwhelming file. Good.

Now we need somewhere to put it.

Right-click on an empty space on your desktop.

You should see "New Folder" or "Create Folder" or something similar.

Click that.

A new folder should appear. It might say "New Folder" or "Untitled Folder."

Now type: Start Here

That's it. S-T-A-R-T space H-E-R-E.

This is your organization folder. Your "I don't know where this goes yet" folder.

Press Enter to confirm the name.

Done? Click Next.""",
            'why': 'One folder is the beginning of structure',
            'duration_seconds': 60,
            'can_skip': False
        },

        {
            'number': 4,
            'title': 'Move the file into the folder',
            'instruction': 'Drag the selected file into "Start Here" folder',
            'audio_script': """Okay, champion. Final step.

See that file you selected? The overwhelming one?

And see your new "Start Here" folder?

Click and HOLD on the file. Keep holding.

Now drag your mouse over to the "Start Here" folder.

Drop it. Let go of the mouse button.

The file should disappear into the folder.

That's it. You just organized.

One file. One folder. One action.

Click Complete Quest.""",
            'why': 'Action completes the learning loop',
            'duration_seconds': 30,
            'can_skip': False
        }
    ],

    # FLASHCARD - Spaced Repetition Learning
    'flashcard': {
        'id': 'adhd_organization_001',
        'front': 'Why can\'t I organize my desktop files?',
        'back': """Executive dysfunction from ADHD.

Your prefrontal cortex (brain's project manager) is understaffed.

You CAN organize with external help (apps, people, step-by-step).

Not laziness. Not stupidity. Brain wiring.""",
        'audio_front': 'Why can\'t I organize my desktop files?',
        'audio_back': """Executive dysfunction from ADHD.

Your prefrontal cortex, that's your brain's project manager, is understaffed. It can't handle planning and organizing like typical brains.

But here's the good news: You CAN organize when you have external help. Like this app. Like people. Like step-by-step instructions.

This isn't laziness. This isn't stupidity. This is brain wiring. And it's manageable.""",
        'category': 'ADHD',
        'difficulty': 'beginner',
        'review_interval_days': 1  # Show again tomorrow
    },

    # INTERACTIVE QUIZ - Reinforcement
    'quiz': {
        'question': 'Your girlfriend asks you to organize all your files by tonight. What do you do?',
        'options': [
            {
                'text': 'A) Promise to do it, then feel overwhelmed and freeze',
                'correct': False,
                'feedback': """That's the ADHD trap.

You promise with good intentions. But your executive dysfunction can't handle "all files" + "by tonight."

Result: Paralysis, shame, broken promise.

Try another answer.""",
                'audio_feedback': """I get it. That's what your brain wants to do. Promise with good intentions.

But here's what happens: Your executive dysfunction looks at "all files by tonight" and just... freezes.

It can't break that down. It can't plan. It can't prioritize.

So you end up paralyzed, feeling shame, breaking your promise.

Let's try another answer."""
            },
            {
                'text': 'B) Say "I can\'t do it all, but I can organize 3 files today"',
                'correct': True,
                'feedback': """YES! Perfect boundary + realistic goal.

You acknowledged the request (validation).
You set a limit (boundary).
You offered what you CAN do (realistic).

This is external executive function: YOU decide the scope, not your broken brain project manager.

+50 XP bonus for correct answer!""",
                'audio_feedback': """Yes! That's exactly right.

You acknowledged her request. That's validation. She feels heard.

You set a limit. That's a boundary. You protected yourself from overwhelm.

And you offered what you CAN do. That's realistic. Three files is doable.

This is you using external executive function. YOU decided the scope. You didn't let your broken brain project manager promise the impossible.

This is mastery. Plus fifty X P bonus!"""
            },
            {
                'text': 'C) Ignore the message because you can\'t handle it',
                'correct': False,
                'feedback': """Avoidance creates more problems.

She feels ignored (relationship damage).
Files stay messy (problem unsolved).
You feel guilt (emotional damage).

Better option: Set a boundary.

Try another answer.""",
                'audio_feedback': """I understand the impulse. When you're overwhelmed, you want to hide.

But avoidance creates three new problems:

One: She feels ignored. That damages the relationship.

Two: The files stay messy. Problem unsolved.

Three: You feel guilt. That's emotional damage to yourself.

There's a better option. Try another answer."""
            }
        ],
        'audio_question': 'Your girlfriend asks you to organize all your files by tonight. What do you do?'
    },

    # PATTERN RECOGNITION - Show what user can't see
    'pattern_insights': {
        'triggers': [
            'Mondays (low energy)',
            'When parent is home (avoidance)',
            'After girlfriend money requests (stress)'
        ],
        'completion_rate': '40% (you avoid organization quests)',
        'best_time': 'Tuesday afternoons (highest completion)',
        'correlation': 'After movement quests, organization success increases 60%',
        'insight': """You avoid organization when stressed about money.

Pattern detected: Girlfriend money request → crypto checking spike → organization quest avoided.

Recommendation: Do organization quests BEFORE checking messages, when your brain is less activated."""
    },

    # SKILL BEING BUILT
    'skill_chain': {
        'skill_name': 'Organization Systems',
        'current_level': 1,
        'next_quest_in_chain': 'Organize 3 files into categories',
        'progression': [
            '✓ Level 1: Organize 1 file (today)',
            '→ Level 2: Organize 3 files',
            '→ Level 3: Create folder structure',
            '→ Level 4: Organize 10 files',
            '→ Level 5: Daily file management habit'
        ]
    }
}


# Quest Flow with ALL features integrated
QUEST_FLOW = {
    'stages': [
        {
            'stage': 'pre_quest',
            'components': [
                'psychoeducation_before',
                'pattern_insight',
                'skill_progress_check'
            ]
        },
        {
            'stage': 'during_quest',
            'components': [
                'step_by_step_guidance',
                'audio_coaching',
                'real_time_support'
            ]
        },
        {
            'stage': 'post_quest',
            'components': [
                'psychoeducation_after',
                'flashcard_learning',
                'interactive_quiz',
                'skill_level_up',
                'xp_reward',
                'celebration'
            ]
        }
    ]
}
