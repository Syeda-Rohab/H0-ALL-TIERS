@echo off
echo ========================================
echo   Deploying to Vercel...
echo ========================================
echo.

cd /d "%~dp0"

REM Check if Vercel CLI is installed
where vercel >nul 2>nul
if %errorlevel% neq 0 (
    echo Vercel CLI not found. Installing...
    npm install -g vercel
)

echo Deploying to production...
vercel --prod

echo.
echo ========================================
echo Deployment complete!
echo ========================================
pause
