@echo off
echo ========================================
echo   AI Employee Dashboard
echo   Vercel Deployment Script
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] Installing dependencies...
call npm install
if %errorlevel% neq 0 (
    echo ERROR: npm install failed!
    pause
    exit /b 1
)

echo.
echo [2/3] Building application...
call npm run build
if %errorlevel% neq 0 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo [3/3] Ready to deploy!
echo.
echo ========================================
echo To deploy to Vercel, run:
echo   vercel --prod
echo.
echo Or double-click deploy.bat
echo ========================================
echo.
pause
