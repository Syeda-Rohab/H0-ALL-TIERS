@echo off
echo ========================================
echo   AI Employee - Web Application
echo   Unified Dashboard (All Tiers)
echo ========================================
echo.
echo Installing dependencies...
pip install flask flask-cors -q
echo.
echo Starting web server...
echo.
echo Open your browser to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.
cd /d "%~dp0"
python app.py
pause
