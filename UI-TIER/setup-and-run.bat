@echo off
echo ========================================
echo AI Employee UI - Setup and Run Script
echo ========================================
echo.

echo [1/3] Installing Node.js dependencies...
cd /d "%~dp0"
call npm install
if %errorlevel% neq 0 (
    echo ERROR: npm install failed!
    pause
    exit /b 1
)

echo.
echo [2/3] Installing Python dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo WARNING: pip install failed! Make sure Python is installed.
)

echo.
echo [3/3] Setup complete!
echo.
echo ========================================
echo Starting AI Employee UI...
echo ========================================
echo.
echo The UI will open at: http://localhost:3000
echo Press Ctrl+C to stop the server.
echo.

start http://localhost:3000
npm run dev

pause
