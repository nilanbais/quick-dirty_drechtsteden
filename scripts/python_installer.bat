@echo off
setlocal

REM === Configuratie ===
set "DOWNLOADS_FOLDER=%USERPROFILE%\Downloads"
set "PYTHON_VERSION=3.12.2"
set "PYTHON_EXEC=python.exe"
set "PYTHON_EXE_FILE_NAME=python-%PYTHON_VERSION%-amd64.exe"
set "INSTALLER_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_EXE_FILE_NAME%"
set "PYTHON_INSTALLER_EXE_FILE_PATH=%DOWNLOADS_FOLDER%\%PYTHON_EXE_FILE_NAME%"


REM === Stap 1: Download installer als die nog niet lokaal staat ===
if not exist %PYTHON_INSTALLER_EXE_FILE_PATH% (
    echo [INFO] Python installer wordt gedownload...
    powershell -Command "Invoke-WebRequest -Uri '%INSTALLER_URL%' -OutFile '%PYTHON_INSTALLER_EXE_FILE_PATH%'"
    if %errorlevel% neq 0 (
        echo [ERROR] Download mislukt. Controleer internetverbinding of URL.
        exit /b 1
    )
)

REM === Stap 2: Voer de installer uit in stille modus ===
echo [INFO] Python wordt geïnstalleerd...
start /wait "" %PYTHON_EXE_FILE_NAME% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
if %errorlevel% neq 0 (
    echo [ERROR] Python-installatie is mislukt.
    exit /b 1
)

REM === Stap 3: Controleer installatie ===
where %PYTHON_EXEC% >nul 2>nul
if %errorlevel% equ 0 (
    echo [SUCCES] Python %PYTHON_VERSION% is succesvol geïnstalleerd.
) else (
    echo [FOUT] Python is niet correct toegevoegd aan PATH. Herstart pc of voeg handmatig toe.
)

:einde
echo.
echo [INFO] Python Installer script voltooid.
pause