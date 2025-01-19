@echo off

REM Setze den Pfad zur Python-Installation
set PATH=C:\Users\%USERNAME%\PycharmProjects\peharge-chatpp-pro\.venv\Scripts;%PATH%

REM Wechsle in das Verzeichnis deines Python-Projekts
cd "C:\Users\%USERNAME%\PycharmProjects\Chatpp\main"

REM Führe das Python-Skript aus
python "sec-check.py"
