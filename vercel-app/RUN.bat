@echo off
echo ========================================
echo   AI Employee Dashboard
echo   Vercel App - Local Development
echo ========================================
echo.
echo [1/2] Installing dependencies...
call npm install
if %errorlevel% neq 0 (
    echo ERROR: Installation failed!
    echo Make sure Node.js is installed from nodejs.org
    pause
    exit /b 1
)

echo.
echo [2/2] Starting development server...
echo.
echo Dashboard will open at: http://localhost:3000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

start http://localhost:3000
npm run dev

pause
