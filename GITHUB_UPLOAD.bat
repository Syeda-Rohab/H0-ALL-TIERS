@echo off
cls
echo ========================================
echo   GitHub Upload - Complete Project
echo ========================================
echo.

cd /d "%~dp0"

REM Initialize
git init

REM Add remote
git remote remove origin 2>nul
git remote add origin https://github.com/Syeda-Rohab/H0-ALL-TIERS.git

REM Create .gitignore
(
echo node_modules/
echo .next/
echo .git/
echo *.log
echo .DS_Store
echo __pycache__/
echo *.pyc
echo .env
) > .gitignore

REM Add all files
echo Adding files...
git add .

REM Commit
echo Committing...
git commit -m "Complete project with beautiful README"

REM Set branch
git branch -M main

REM Force push
echo Pushing to GitHub...
git push -u origin main --force

echo.
echo ========================================
echo   Upload Complete!
echo ========================================
echo.
echo Check: https://github.com/Syeda-Rohab/H0-ALL-TIERS
echo.
pause
