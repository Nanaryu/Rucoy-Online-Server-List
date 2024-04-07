@echo off
py -m pip install -r requirements.txt
cls
py -m rucoyserverlist
exit /b %errorlevel%