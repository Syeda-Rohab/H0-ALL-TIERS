@echo off
cls
echo ========================================
echo   H0 ALL TIERS - Complete Upload
echo ========================================
echo.
echo Uploading: Bronze, Silver, Gold, Platinum + Dashboard
echo.

cd /d "%~dp0"

echo [1/6] Initializing Git...
git init

echo.
echo [2/6] Creating .gitignore...
(
echo node_modules/
echo .next/
echo .git/
echo *.log
echo .DS_Store
echo __pycache__/
echo *.pyc
echo .env
echo dist/
echo build/
) > .gitignore

echo.
echo [3/6] Adding ALL files...
git add .

echo.
echo [4/6] Committing...
git commit -m "H0 Complete Project - All 4 Tiers + Dashboard"

echo.
echo [5/6] Setting branch...
git branch -M main

echo.
echo [6/6] Pushing to GitHub...
git remote set-url origin https://github.com/Syeda-Rohab/H0-ALL-TIERS.git
git push -u origin main --force

echo.
echo ========================================
echo   Upload Complete!
echo ========================================
echo.
echo Uploaded:
echo   - Bronze Tier
echo   - Silver Tier  
echo   - Gold Tier
echo   - Platinum Tier
echo   - AI Employee Pro Dashboard
echo.
echo Go to: https://github.com/Syeda-Rohab/H0-ALL-TIERS
echo Then deploy on Vercel!
echo.
pause
