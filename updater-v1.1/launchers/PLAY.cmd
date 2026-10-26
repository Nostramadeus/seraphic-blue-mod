@echo off
cd /d "%~dp0"
if not "%~1"=="" goto play
if not exist ".sb-startup-updates\Startup.ps1" goto play
"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoLogo -NoProfile -STA -WindowStyle Hidden -ExecutionPolicy Bypass -File "%~dp0.sb-startup-updates\Startup.ps1" -GameFolder "%~dp0."
if errorlevel 11 goto play
if errorlevel 10 exit /b 0
:play
if not exist "saves" mkdir "saves"
if not exist "config" mkdir "config"
"%~dp0Player.exe" --project-path "." --save-path "saves" --config-path "config" --encoding 932 --window %*
exit /b %errorlevel%
