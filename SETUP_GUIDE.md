# BackToLife Setup Guide

Complete installation guide for the BackToLife digital therapeutic app.

## 🚀 Quick Start (Windows)

### Option 1: Automatic Setup (Easiest)

1. **Double-click `setup.bat`**
2. Wait for installation to complete
3. Double-click `run_app.bat` to launch the app

That's it! The setup script will:
- Check your Python installation
- Install all required packages
- Initialize the database
- Create a launcher for easy access

### Option 2: Manual Setup

If you prefer to install manually or the automatic setup doesn't work:

```bash
# 1. Install Python packages
pip install -r requirements.txt

# 2. Initialize the quest database
python -c "from src.data.quest_database import initialize_quest_database; initialize_quest_database()"

# 3. Run the app
python final_app.py
```

## 📋 Requirements

### System Requirements
- **OS**: Windows 10/11, macOS 10.14+, or Linux
- **Python**: 3.11 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Storage**: 50MB for app + database

### Python Packages
All installed automatically by `setup.bat`:
- `customtkinter` - Modern UI framework
- `pyttsx3` - Text-to-speech for audio guidance
- `Pillow` - Image support

## 🔧 Installation Steps (Detailed)

### Step 1: Install Python

If you don't have Python installed:

**Windows:**
1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. ✅ **IMPORTANT**: Check "Add Python to PATH"
4. Click "Install Now"

**macOS:**
```bash
# Install using Homebrew
brew install python@3.11
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3-pip python3-tk
```

### Step 2: Verify Python Installation

Open Command Prompt (Windows) or Terminal (Mac/Linux) and run:
```bash
python --version
```

You should see: `Python 3.11.x` or higher

### Step 3: Install BackToLife

**Windows:**
```cmd
# Navigate to the BackToLife folder
cd path\to\back-to-life

# Run setup
setup.bat
```

**macOS/Linux:**
```bash
# Navigate to the BackToLife folder
cd path/to/back-to-life

# Install packages
pip install -r requirements.txt

# Initialize database
python -c "from src.data.quest_database import initialize_quest_database; initialize_quest_database()"
```

### Step 4: Launch the App

**Windows:**
- Double-click `run_app.bat`
- Or run: `python final_app.py`

**macOS/Linux:**
```bash
python final_app.py
```

## 🎯 What to Expect

When you first launch BackToLife, you'll see:

1. **8 Navigation Tabs** on the left sidebar
2. **Home Tab** with your daily quest
3. **Audio Toggle** button at the bottom
4. **User Stats** (Level 1, 0 XP, 0 Streak)

### First Steps:
1. Click on different tabs to explore all features
2. Try the **Tools** tab and select a mood to see filtered tools
3. Complete your first quest on the **Home** tab
4. Check out the **Shield** tab if you ever need crisis support
5. Visit **Settings** to customize audio and appearance

## 🛠️ Troubleshooting

### "Python is not recognized"
**Problem**: Python not in PATH
**Solution**: Reinstall Python and check "Add Python to PATH"

### "No module named 'customtkinter'"
**Problem**: Packages not installed
**Solution**: Run `pip install -r requirements.txt`

### "ModuleNotFoundError: No module named 'tkinter'"
**Problem**: tkinter not installed (Linux only)
**Solution**: `sudo apt-get install python3-tk`

### Audio not working
**Problem**: pyttsx3 or system audio issues
**Solution**:
- Windows: Make sure speakers are enabled
- macOS: Grant microphone/accessibility permissions
- Linux: Install espeak: `sudo apt-get install espeak`

### App window is too large/small
**Solution**:
- The app is designed to be resizable
- Drag window corners to adjust size
- Settings → Appearance (coming soon) will add scaling options

### Database errors
**Problem**: Corrupt database
**Solution**: Delete `~/.backtolife/backtolife_data.db` and restart app

## 📂 Where Your Data is Stored

BackToLife stores all data locally on your computer:

**Windows:**
```
C:\Users\YourName\.backtolife\backtolife_data.db
```

**macOS/Linux:**
```
~/.backtolife/backtolife_data.db
```

All data stays on your device - nothing is sent to the cloud.

## 🎮 Demo Mode

Want to see what an enhanced quest looks like before diving in?

```bash
python demo_app.py
```

This shows a complete quest with:
- Psychoeducation (before/after)
- Step-by-step audio guidance
- Interactive flashcard
- ADHD-friendly quiz

## 🔄 Updating

To update BackToLife to a new version:

1. Download the latest version
2. Copy your database file (`.backtolife/backtolife_data.db`) to a safe location
3. Replace all files with the new version
4. Run `setup.bat` again
5. Your data will be preserved!

## ⚙️ Advanced Options

### Running in Virtual Environment

For developers or if you want isolated packages:

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Run app
python final_app.py
```

### Command-Line Interface

The original CLI version is still available:

```bash
python cli_app.py
```

### Portable Installation

To make BackToLife portable (run from USB drive):

1. Install Python Embedded: https://www.python.org/downloads/windows/
2. Extract to BackToLife folder
3. Install packages to the embedded Python
4. Create batch file pointing to embedded python.exe

## 🆘 Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Make sure you're running Python 3.11+
3. Try deleting and recreating the database
4. Check the BUILD_SUMMARY.md for feature documentation

## 📚 Additional Resources

- **BUILD_SUMMARY.md** - Complete feature list
- **COMPLETE_ARCHITECTURE.md** - Full app design
- **backtolife.md** - Original planning document
- **RESEARCH_ANALYSIS.md** - App research findings

## 🎉 You're All Set!

Once setup is complete, you're ready to start your BackToLife journey.

**Remember:**
- Start small - complete just one quest
- Use the mood-based tool selector when you need help
- The Shield tab is always there if you need it
- Your progress is tracked automatically

Welcome to BackToLife! 🌟
