@echo off
echo Starting YT Shorts Automation...
timeout /t 2

start cmd /k "cd /d path/to/your/ && python tts_server.py"
echo TTS Server started...
timeout /t 5

start cmd /k "cd /d path/to/your/ && python video_server.py"
echo Video Server started...
timeout /t 5

start cmd /k "cd /d path/to/your/ && python youtube_server.py"
echo YouTube Server started...
timeout /t 3

echo.
echo ================================
echo All servers are running!
echo Automation is active.
echo Remember to open n8n at:
echo http://localhost:5678
echo ================================
pause