@echo off
chcp 65001 >nul
echo.
echo  ========================================
echo   Coup de pouce - Accès depuis le téléphone
echo  ========================================
echo.
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4"') do (
  set IP=%%a
  goto :found
)
:found
set IP=%IP:~1%
echo  Sur ton PC : le serveur va démarrer.
echo.
echo  Sur ton TELEPHONE (même Wi-Fi) ouvre :
echo.
echo    http://%IP%:8000
echo.
echo  ========================================
echo.
python manage.py runserver 0.0.0.0:8000
pause
