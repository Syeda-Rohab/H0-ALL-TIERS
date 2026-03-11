@echo off
title AI Employee Dashboard - Installing...
cls

echo ========================================
echo   AI Employee Dashboard
echo   Installing Dependencies...
echo ========================================
echo.

cd /d "%~dp0"

REM Check if Node.js is installed
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed!
    echo.
    echo Please install Node.js from: https://nodejs.org
    echo.
    echo After installation, double-click this file again.
    pause
    exit /b 1
)

echo Node.js found: 
node --version
echo.

echo [1/2] Installing dependencies...
echo This may take 2-3 minutes on first run...
echo.

call npm install

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Installation failed!
    echo Try running as Administrator or check your internet connection.
    pause
    exit /b 1
)

echo.
echo [2/2] Starting development server...
echo.
echo ========================================
echo   Dashboard starting...
echo   Opening in browser...
echo ========================================
echo.
echo Server running at: http://localhost:3000
echo.
echo Press Ctrl+C in the window to stop the server
echo ========================================
echo.

REM Wait a moment for npm to start
timeout /t 2 /nobreak >nul

REM Open browser
start http://localhost:3000

REM Start dev server
call npm run dev

pause
