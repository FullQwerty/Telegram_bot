@echo off 

call %~dp0dev/Telegramm_Bot_Regestartion/venv/bin/activate 

cd %~dp0dev/Telegramm_Bot_Regestartion

set TOKEN=5147116107:AAGL2Pdi6iK9chJFmd4VSZfqAJfQuvSL9_c

python3 bot_telegram.py

pause 