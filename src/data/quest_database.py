"""
BackToLife Quest Database
All quest definitions organized by category
Tailored specifically for Bradly's needs
"""

QUEST_CATEGORIES = {
    'BODY_RECOVERY': 'Body Recovery',
    'HYGIENE': 'Hygiene',
    'EATING_DRINKING': 'Eating & Drinking',
    'ORGANIZATION': 'Organization',
    'SOCIAL_RECOVERY': 'Social Recovery',
    'FINANCIAL': 'Financial Survival',
    'ACADEMIC': 'Academic Exit',
    'CREATIVE': 'Creative Reawakening',
    'CRYPTO_AI': 'Crypto & AI',
    'FORTNITE': 'Fortnite Integration'
}

# Quest structure: category, title, description, duration_minutes, xp_value, difficulty_level (1-5), tier, why_text, instructions
QUESTS = [
    # === BODY RECOVERY QUESTS ===
    ('BODY_RECOVERY', 'Stand for 10 seconds', 'Stand up beside your bed for 10 seconds', 1, 10, 1, 1,
     'Your body needs to remember it can move', 'Stand up, count to 10 slowly, then sit back down. That\'s it.'),

    ('BODY_RECOVERY', 'Touch your door', 'Stand and walk to touch your door', 2, 10, 1, 1,
     'Walking to the door proves your legs still work', 'Get up, walk to your door, touch it, and come back.'),

    ('BODY_RECOVERY', 'Stand at edge of bed for 1 minute', 'Stand by your bed for a full minute', 2, 15, 1, 2,
     'Standing longer builds endurance', 'Stand up and count to 60. Slow counts are fine.'),

    ('BODY_RECOVERY', 'Walk to bathroom', 'Walk to the bathroom and back', 3, 15, 2, 2,
     'Your body remembers how to move between rooms', 'Walk to bathroom when parents are gone, then return.'),

    ('BODY_RECOVERY', 'Stretch arms up', 'Stand and stretch both arms above your head', 1, 10, 1, 1,
     'Stretching wakes up your muscles', 'Stand up, raise both arms high, hold for 5 seconds.'),

    ('BODY_RECOVERY', 'Take 3 deep breaths', 'Take three slow, deep breaths', 1, 5, 1, 1,
     'Oxygen helps your brain think', 'Breathe in slowly for 4 counts, out for 4 counts. Do this 3 times.'),

    ('BODY_RECOVERY', 'Touch your toes', 'Try to touch your toes (or as close as you can)', 2, 15, 2, 2,
     'Flexibility prevents pain', 'Sit or stand, reach toward your toes. Getting close counts.'),

    ('BODY_RECOVERY', 'Walk to window', 'Walk to your window and look outside', 3, 15, 2, 2,
     'Looking outside reminds you there\'s a world waiting', 'Walk to window, look out for 30 seconds.'),

    ('BODY_RECOVERY', 'Stand by open door for 2 minutes', 'Keep your door open and stand near it', 3, 20, 2, 3,
     'Being near the doorway is practice for going through it', 'Open door, stand inside room near doorway for 2 minutes.'),

    ('BODY_RECOVERY', 'Walk around your room', 'Walk a slow lap around your room', 3, 20, 2, 3,
     'Movement anywhere counts as training', 'Make one complete lap around your room. Slow is fine.'),

    # === HYGIENE QUESTS ===
    ('HYGIENE', 'Brush teeth (top row only)', 'Brush just your top teeth', 2, 5, 1, 1,
     'Even partial cleaning is better than none', 'Wet brush, add toothpaste, brush top teeth for 30 seconds.'),

    ('HYGIENE', 'Brush full teeth', 'Brush both top and bottom teeth', 3, 10, 1, 2,
     'Clean teeth reduce shame and improve health', 'Brush top and bottom teeth for 2 minutes total.'),

    ('HYGIENE', 'Wash face with water', 'Splash water on your face', 2, 5, 1, 1,
     'Water wakes up your skin', 'Use cold or warm water, splash your face 5 times.'),

    ('HYGIENE', 'Wet your hair', 'Run water through your hair', 3, 10, 1, 2,
     'Wet hair feels refreshing', 'In bathroom or sink, wet your hair with water.'),

    ('HYGIENE', 'Apply deodorant', 'Put on deodorant', 1, 5, 1, 1,
     'Small hygiene wins build confidence', 'Apply deodorant to underarms.'),

    ('HYGIENE', 'Change shirt', 'Put on a clean shirt', 2, 10, 1, 2,
     'Fresh clothes change how you feel', 'Pick a clean shirt and put it on.'),

    ('HYGIENE', 'Look in mirror and smile', 'Look at yourself in the mirror', 2, 15, 2, 2,
     'Seeing yourself reminds you that you exist', 'Stand in front of mirror, look at your face, try to smile.'),

    ('HYGIENE', 'Take a 2-minute shower', 'Quick shower, just get wet', 5, 25, 3, 3,
     'Water washes away more than dirt', 'Turn on shower, get in, get wet, get out. 2 minutes max.'),

    ('HYGIENE', 'Wash hands with soap', 'Properly wash your hands', 2, 5, 1, 1,
     'Clean hands prevent sickness', 'Use soap and water, wash for 20 seconds.'),

    ('HYGIENE', 'Change pants/shorts', 'Put on clean pants or shorts', 2, 10, 1, 2,
     'Full outfit change builds momentum', 'Pick clean bottoms and change into them.'),

    # === EATING & DRINKING QUESTS ===
    ('EATING_DRINKING', 'Drink one glass of water', 'Drink a full glass of water', 2, 10, 1, 1,
     'Your body has been without water for hours', 'Fill glass with water and drink it all.'),

    ('EATING_DRINKING', 'Drink two glasses of water', 'Drink two full glasses', 3, 15, 1, 2,
     'Hydration improves mood and focus', 'Drink two glasses of water within 10 minutes.'),

    ('EATING_DRINKING', 'Eat one bite of food', 'Just one bite of anything', 1, 10, 1, 1,
     'One bite breaks the not-eating pattern', 'Pick any food, take one bite, chew, swallow.'),

    ('EATING_DRINKING', 'Eat a full snack', 'Eat something small', 5, 15, 2, 2,
     'Your brain needs fuel to function', 'Eat a piece of fruit, crackers, or any small snack.'),

    ('EATING_DRINKING', 'Make tea or coffee', 'Prepare a hot drink', 5, 15, 2, 2,
     'Making something is an accomplishment', 'Boil water, prepare tea or coffee, drink it.'),

    ('EATING_DRINKING', 'Get a snack from kitchen', 'Go to kitchen and bring back food', 5, 20, 2, 3,
     'Leaving your room to get food is brave', 'When parents are gone, go to kitchen, get snack, return.'),

    ('EATING_DRINKING', 'Eat while sitting (not in bed)', 'Eat somewhere other than bed', 5, 20, 3, 3,
     'Separating bed from eating builds routines', 'Take food to desk or table, eat there.'),

    ('EATING_DRINKING', 'Prepare a simple meal', 'Make something basic to eat', 10, 30, 3, 4,
     'Cooking for yourself is self-care', 'Toast, cereal, sandwich - anything you make counts.'),

    # === ORGANIZATION QUESTS ===
    ('ORGANIZATION', 'Delete one file from desktop', 'Remove one file you don\'t need', 2, 10, 1, 1,
     'Every file deleted reduces overwhelm', 'Find one file on desktop you don\'t need and delete it.'),

    ('ORGANIZATION', 'Create folder "Start Here"', 'Make one new folder', 2, 15, 1, 1,
     'One folder is the beginning of order', 'Right-click desktop, create new folder, name it "Start Here".'),

    ('ORGANIZATION', 'Move one file to a folder', 'Organize one single file', 2, 20, 1, 2,
     'Your future self will thank you', 'Pick one file and move it into any folder.'),

    ('ORGANIZATION', 'Close one browser tab', 'Close a tab you don\'t need', 1, 5, 1, 1,
     'Fewer tabs = less mental clutter', 'Pick one browser tab and close it.'),

    ('ORGANIZATION', 'Close 5 browser tabs', 'Clean up your browser', 3, 15, 2, 2,
     'Digital cleanup reduces anxiety', 'Close 5 tabs you don\'t currently need.'),

    ('ORGANIZATION', 'Write down one task on paper', 'Write one thing you need to do', 2, 10, 1, 1,
     'Getting it out of your head makes it smaller', 'Write one task on paper or in notepad.'),

    ('ORGANIZATION', 'Organize 5 files on desktop', 'Clean up multiple files', 5, 30, 2, 3,
     'Visible progress feels good', 'Move or delete 5 files from your desktop.'),

    ('ORGANIZATION', 'Create folder structure', 'Make folders for different types of files', 10, 40, 3, 4,
     'Structure creates clarity', 'Create 3-5 folders with clear names (Projects, Music, Documents, etc).'),

    # === SOCIAL RECOVERY QUESTS ===
    ('SOCIAL_RECOVERY', 'Stay in room with door open for 5 min', 'Keep door open, stay inside', 5, 15, 2, 1,
     'Being near people (even silently) rebuilds social tolerance', 'Open your door, stay in room for 5 minutes.'),

    ('SOCIAL_RECOVERY', 'Say "morning" to father', 'Greet your father once', 1, 20, 3, 2,
     'One word breaks the silence', 'When you see father, just say "morning" or "hi".'),

    ('SOCIAL_RECOVERY', 'Make eye contact with father\'s wife for 1 second', 'Brief eye contact', 1, 25, 3, 3,
     'Eye contact is practice for the world', 'When you see her, look at her eyes for 1 second.'),

    ('SOCIAL_RECOVERY', 'Text sister one emoji', 'Send one emoji to your sister', 1, 15, 2, 1,
     'Any contact counts as connection', 'Open messages, send sister any emoji.'),

    ('SOCIAL_RECOVERY', 'Send girlfriend one heart emoji', 'Simple message to girlfriend', 1, 15, 2, 1,
     'Simple love gestures maintain connection without draining you', 'Send girlfriend a ❤️ emoji.'),

    ('SOCIAL_RECOVERY', 'Listen to someone talk for 30 seconds', 'Just listen, don\'t respond', 1, 20, 2, 2,
     'Listening is a skill you can rebuild', 'When someone talks, listen for 30 seconds without pressure to reply.'),

    ('SOCIAL_RECOVERY', 'Sit in common area for 10 minutes', 'Be present where family is', 10, 30, 3, 3,
     'Presence builds tolerance', 'Sit in living room or kitchen when parents are home for 10 min.'),

    ('SOCIAL_RECOVERY', 'Ask father one question', 'Initiate conversation', 2, 30, 3, 4,
     'Asking questions shows you\'re coming back', 'Ask father something simple - about his day, weather, anything.'),

    # === FINANCIAL SURVIVAL QUESTS ===
    ('FINANCIAL', 'Open bank app (just look)', 'Check your bank balance', 2, 10, 2, 1,
     'Knowing your situation is better than avoiding it', 'Open banking app, look at balance, close app.'),

    ('FINANCIAL', 'Write down one debt amount', 'Document one thing you owe', 3, 15, 2, 1,
     'Written problems feel more manageable', 'Write down one debt with the amount owed.'),

    ('FINANCIAL', 'Find one item to sell on Vinted', 'Identify something to sell', 5, 20, 2, 2,
     'Small sales add up', 'Look in your room for one item you could sell.'),

    ('FINANCIAL', 'Take photo of one item to sell', 'Photograph something sellable', 5, 25, 2, 3,
     'Photos are preparation for action', 'Take a clear photo of one item you could sell.'),

    ('FINANCIAL', 'Research one way to make £10', 'Find a small money opportunity', 10, 20, 2, 2,
     'Small income breaks the pattern of zero income', 'Search online for quick ways to earn £10.'),

    ('FINANCIAL', 'List one item on Vinted', 'Actually post something for sale', 15, 50, 3, 4,
     'Listed items can sell while you sleep', 'Create listing on Vinted with photo, price, description.'),

    ('FINANCIAL', 'Track spending for one day', 'Write down what you spend', 5, 20, 2, 2,
     'Awareness is the first step to control', 'Write down every pound spent today.'),

    # === ACADEMIC EXIT QUESTS ===
    ('ACADEMIC', 'Find one exam PDF', 'Locate one university exam file', 5, 15, 2, 1,
     'Finding it is the first step', 'Search your computer for one exam PDF file.'),

    ('ACADEMIC', 'Open PDF and read title', 'Just open it and look', 2, 20, 2, 2,
     'Opening the file proves it\'s not scary', 'Open one exam PDF, read the title, close it.'),

    ('ACADEMIC', 'Read one sentence from exam', 'Read just one sentence', 2, 25, 2, 3,
     'One sentence is progress', 'Open exam PDF, read one full sentence, close file.'),

    ('ACADEMIC', 'Highlight one word in exam', 'Mark one word', 3, 30, 2, 4,
     'Interacting with material is studying', 'Open PDF, highlight any one word, save.'),

    ('ACADEMIC', 'Save exam PDF to desktop', 'Organize one exam file', 2, 15, 2, 2,
     'Making files accessible reduces overwhelm', 'Move one exam PDF to your desktop for easy access.'),

    ('ACADEMIC', 'Read one paragraph from exam', 'Read a full paragraph', 5, 35, 3, 5,
     'Paragraphs contain complete thoughts', 'Open exam, read one paragraph, take a break.'),

    ('ACADEMIC', 'Write one sentence about exam content', 'Engage with material', 5, 40, 3, 5,
     'Writing helps process information', 'Read something from exam, write one sentence about it.'),

    # === CREATIVE REAWAKENING QUESTS ===
    ('CREATIVE', 'Beatbox one sound', 'Make one beatbox sound', 1, 10, 1, 1,
     'One sound proves your voice still works', 'Make any beatbox sound once. Just once.'),

    ('CREATIVE', 'Record 5 seconds of beatbox', 'Record yourself', 2, 20, 2, 2,
     'Recording it makes it real', 'Use phone or computer, record 5 seconds of beatboxing.'),

    ('CREATIVE', 'Hum a melody', 'Hum any tune', 1, 10, 1, 1,
     'Music lives inside you still', 'Hum any song or melody for 10 seconds.'),

    ('CREATIVE', 'Draw one line', 'Make one mark on paper', 1, 10, 1, 1,
     'Creativity starts with one mark', 'Get paper and pen, draw one line. Any line.'),

    ('CREATIVE', 'Write one word about how you feel', 'Express yourself', 1, 10, 1, 1,
     'Naming feelings reduces their power', 'Write down one word describing your current emotion.'),

    ('CREATIVE', 'Open AI tool and type "hello"', 'Engage with AI', 2, 15, 1, 1,
     'AI can help you create', 'Open ChatGPT or Claude, type "hello", see response.'),

    ('CREATIVE', 'Beatbox for 30 seconds', 'Extended practice', 3, 30, 2, 3,
     'Longer practice rebuilds skill', 'Beatbox continuously for 30 seconds.'),

    ('CREATIVE', 'Listen to one beatbox video', 'Study others', 5, 15, 2, 2,
     'Watching champions reminds you what\'s possible', 'Watch one professional beatbox video on YouTube.'),

    ('CREATIVE', 'Practice one new beatbox sound', 'Learn something new', 10, 40, 3, 4,
     'New skills prove you\'re growing', 'Pick one new sound and practice it for 10 minutes.'),

    # === CRYPTO & AI QUESTS ===
    ('CRYPTO_AI', 'Check crypto with 5-minute timer', 'Limited crypto checking', 5, 15, 2, 2,
     'Limits prevent obsession', 'Check crypto for 5 minutes max, then close all tabs.'),

    ('CRYPTO_AI', 'Write down one crypto pattern you notice', 'Document observations', 5, 20, 2, 2,
     'Patterns you track teach you more than endless watching', 'Write one thing you notice about crypto movement.'),

    ('CRYPTO_AI', 'Watch one 3-minute AI tutorial', 'Learn something new', 5, 20, 2, 2,
     'Learning AI skills creates real value', 'Watch one short AI tutorial video.'),

    ('CRYPTO_AI', 'Code one line in Python', 'Write actual code', 5, 25, 2, 2,
     'Building creates more wealth than hoping', 'Open Python, write one line of code, run it.'),

    ('CRYPTO_AI', 'Ask ChatGPT one question about apps', 'Learn app development', 3, 15, 2, 1,
     'Questions lead to knowledge', 'Ask ChatGPT anything about making apps.'),

    ('CRYPTO_AI', 'Read one AI article', 'Stay informed', 10, 20, 2, 2,
     'Knowledge is investment in yourself', 'Read one article about AI technology.'),

    ('CRYPTO_AI', 'Close crypto apps for 1 hour', 'Practice control', 60, 35, 3, 3,
     'Discipline builds wealth more than watching', 'Close all crypto apps and don\'t open for 1 hour.'),

    # === FORTNITE INTEGRATION QUESTS ===
    ('FORTNITE', 'Play one match with focus', 'No multitasking during match', 20, 15, 2, 2,
     'Focused practice improves skill', 'Play one match, no phone, no crypto checking.'),

    ('FORTNITE', 'Practice one move in creative for 5 min', 'Skill-building session', 5, 20, 2, 2,
     'Practice makes you better', 'Go to creative mode, practice one building technique.'),

    ('FORTNITE', 'Watch one 2-minute pro tip video', 'Learn from pros', 3, 15, 2, 1,
     'Pros were beginners once too', 'Watch one short Fortnite tips video.'),

    ('FORTNITE', 'Stretch before playing', 'Warm up your body', 2, 15, 2, 1,
     'Your body performs better when warmed up', 'Do 5 quick stretches before playing Fortnite.'),

    ('FORTNITE', 'Take break after each match', 'Rest between matches', 5, 20, 2, 2,
     'Breaks prevent burnout', 'After each match, stand up and walk for 2 minutes.'),

    ('FORTNITE', 'Play only 3 matches today', 'Practice restraint', 60, 30, 3, 3,
     'Quality over quantity', 'Play exactly 3 matches, then close game.'),

    ('FORTNITE', 'Track your eliminations', 'Measure progress', 5, 15, 2, 2,
     'Data shows improvement', 'Write down eliminations from each match today.'),
]


def initialize_quest_database(db):
    """
    Populate database with all quests
    Only run once during setup
    """
    db.connect()

    # Check if quests already exist
    db.cursor.execute('SELECT COUNT(*) FROM quests')
    if db.cursor.fetchone()[0] > 0:
        print("Quests already initialized")
        return

    # Insert all quests
    for quest in QUESTS:
        db.cursor.execute('''
            INSERT INTO quests (
                category, title, description, duration_minutes,
                xp_value, difficulty_level, tier, why_text, instructions
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', quest)

    db.conn.commit()
    print(f"Initialized {len(QUESTS)} quests across {len(QUEST_CATEGORIES)} categories")


def get_quests_by_category(db, category):
    """Get all quests in a specific category"""
    db.cursor.execute('''
        SELECT * FROM quests
        WHERE category = ?
        ORDER BY difficulty_level, tier
    ''', (category,))
    return db.cursor.fetchall()


def get_quest_by_id(db, quest_id):
    """Get specific quest by ID"""
    db.cursor.execute('SELECT * FROM quests WHERE id = ?', (quest_id,))
    return db.cursor.fetchone()


def get_random_quest_by_difficulty(db, category, max_difficulty=3):
    """Get a random quest from category within difficulty range"""
    db.cursor.execute('''
        SELECT * FROM quests
        WHERE category = ? AND difficulty_level <= ?
        ORDER BY RANDOM()
        LIMIT 1
    ''', (category, max_difficulty))
    return db.cursor.fetchone()
