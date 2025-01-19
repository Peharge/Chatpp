@echo off

rem Setze den Pfad zur Python-Umgebung "peharge_chatpp"
set PATH=C:\Users\%USERNAME%\PycharmProjects\peharge-chatpp-pro\.venv\Scripts;%PATH%

rem Führe das Skript aus, das du benötigst
cd "C:\Users\%USERNAME%\PycharmProjects\Chatpp\main"

rem Verwende den direkten Pfad zur Python-Interpreter-Datei
python "test7-video.py"

rem Führe das nächste Skript aus
python "test7.py"
