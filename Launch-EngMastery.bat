@echo off
title EngMastery AI App Launcher
cd /d "%~dp0"

:: Start background local Python HTTP server on port 5200 if not already running
netstat -ano | findstr :5200 >nul 2>&1
if %errorlevel% neq 0 (
    start /b python server.py >nul 2>&1
    timeout /t 1 /nobreak >nul
)

:: Launch Edge in standalone App mode
start msedge --app="http://localhost:5200/index.html" >nul 2>&1
if %errorlevel% equ 0 exit

:: If msedge fails, try chrome in standalone App mode
start chrome --app="http://localhost:5200/index.html" >nul 2>&1
if %errorlevel% equ 0 exit

:: Fallback to default browser
start http://localhost:5200/index.html
exit
