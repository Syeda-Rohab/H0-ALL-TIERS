@echo off
echo ========================================
echo   AI Employee - Bronze Tier
echo ========================================
echo.
cd /d "%~dp0"
python ai_employee_simple.py
echo.
echo ========================================
echo Process Complete!
echo ========================================
echo.
echo Check the bronze_vault folder for results:
echo - Done folder: Processed emails and plans
echo - Dashboard.md: Updated statistics
echo.
pause
