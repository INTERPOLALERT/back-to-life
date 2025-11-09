@echo off
SETLOCAL EnableDelayedExpansion

echo ============================================
echo BackToLife - Setup and Installation
echo ============================================
echo.

REM Check if Python is installed
echo [1/5] Checking for Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.11 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation!
    echo.
    pause
    exit /b 1
)

python --version
echo Python found!
echo.

REM Check Python version
echo [2/5] Checking Python version...
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Python version: %PYTHON_VERSION%
echo.

REM Upgrade pip
echo [3/5] Upgrading pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo WARNING: Could not upgrade pip, continuing anyway...
)
echo.

REM Install required packages
echo [4/5] Installing required packages...
echo.
echo Installing CustomTkinter (modern UI framework)...
python -m pip install customtkinter
if %errorlevel% neq 0 (
    echo ERROR: Failed to install customtkinter
    pause
    exit /b 1
)

echo.
echo Installing pyttsx3 (text-to-speech)...
python -m pip install pyttsx3
if %errorlevel% neq 0 (
    echo ERROR: Failed to install pyttsx3
    pause
    exit /b 1
)

echo.
echo Installing Pillow (image support)...
python -m pip install Pillow
if %errorlevel% neq 0 (
    echo WARNING: Failed to install Pillow, some features may not work
)

echo.
echo All packages installed successfully!
echo.

REM Initialize database with quests
echo [5/5] Initializing database...
python -c "from src.data.quest_database import initialize_quest_database; initialize_quest_database()"
if %errorlevel% neq 0 (
    echo WARNING: Could not initialize quest database
    echo The app will create it on first run
)
echo.

REM Create run shortcut
echo Creating run_app.bat launcher...
(
    echo @echo off
    echo cd /d "%%~dp0"
    echo echo Starting BackToLife...
    echo python final_app.py
    echo pause
) > run_app.bat

echo.
echo ============================================
echo Installation Complete!
echo ============================================
echo.
echo BackToLife is now installed and ready to use.
echo.
echo To run the app:
echo   1. Double-click run_app.bat
echo   2. Or run: python final_app.py
echo.
echo To see the enhanced quest demo:
echo   - Run: python demo_app.py
echo.
echo Your data will be stored in:
echo   %USERPROFILE%\.backtolife\
echo.
echo ============================================
echo.
pause
