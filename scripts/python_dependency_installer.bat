@echo off
:: set voor betere for-loops en if-statements
setlocal EnableDelayedExpansion 


REM === Configuratie ===
:: set variabele als parameter/default
set "DEFAULT_INPUT_VALUE=requirements.txt"
if "%1"=="" (
    echo [INFO] NO PARAMETER 'INPUT_PATH' GIVEN. USING DEFAULT VALUE '%DEFAULT_INPUT_VALUE%'
    set "USER_INPUT_PATH=%DEFAULT_INPUT_VALUE%"
) else (
    set "USER_INPUT_PATH=%1"
)



REM === installeren van python dependencies ===
echo [INFO] Installeren van Python dependencies...
python -m pip install -r "%USER_INPUT_PATH%" -q


if %errorlevel% neq 0 (
    echo [FOUT] Installatie van dependencies mislukt.
    echo Controleer of Python en pip correct zijn geconfigureerd en in je PATH staan.
) else (
    echo [SUCCES] Dependencies zijn succesvol geinstalleerd.
)

:einde
echo [INFO] Python Dependency Installer script is done.