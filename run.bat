@echo off
TITLE Excel Chat Bot
echo ==========================================
echo       Starting Excel Chat Bot Server
echo ==========================================
echo.
echo Note: Ensure your OPENROUTER_API_KEY is set in the .env file.
echo.
echo [Action] Starting Uvicorn on http://127.0.0.1:8000 (Ctrl+click to open the app)
echo [Action] Press Ctrl+C to stop the server.
echo.

IF EXIST venv\Scripts\activate.bat (
    echo [Info] Activating Virtual Environment...
    call venv\Scripts\activate.bat
)

python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload

if %errorlevel% neq 0 (
    echo.
    echo Server stopped or encountered an error.
    pause
)
