@echo off
:: set voor betere for-loops en if-statements
setlocal EnableDelayedExpansion 


REM === Configuratie ===
:: set working dir op pad van dit bestand
cd /d %~dp0

:: set variabelen
set "RELATIVE_PATH_PYTHON_DEPENDENCIES=requirements.txt"
set "RELATIVE_PATH_SCRIPTS_FOLDER=\scripts"
set "PYTHON_INSTALLER_RELATIVE_PATH=%RELATIVE_PATH_SCRIPTS_FOLDER%\python_installer.bat"
set "DEPENDENCY_INSTALLER_RELATIVE_PATH=%RELATIVE_PATH_SCRIPTS_FOLDER%\python_dependency_installer.bat"
set "PYTHON_EXEC=python.exe"
set "PYTHON_SCRIPT_PATH=scripts\execute_transformation.py"

:: python code in folder 'source_code' toevoegen aan PYTHONPATH
set "PYTHONPATH=%CD%\source_code;%PYTHONPATH%"
set "PYTHONWARNINGS=ignore"

:: zoek het pad van python.exe en sla het op in een variabele
for /f "delims=" %%p in ('where python.exe') do (
    set "PYTHON_EXE_PATH=%%p"
)

REM === Controleren of python al geïnstalleerd is op het systeem ===
:python

if not defined PYTHON_EXE_PATH (
    echo [FOUT] Python is niet geïnstalleerd.
    echo.
    echo [INFO] Start installatie van Python.
    pause
    call %CD%\%PYTHON_INSTALLER_RELATIVE_PATH%
) else (
    echo [SUCCES] Python is al geïnstalleerd op het systeem.
    echo.
)

REM === Installeer de benodigde python packages ===
:dependencies 
echo [INFO] Installeer python packages
echo requirements file: %RELATIVE_PATH_PYTHON_DEPENDENCIES%
echo.
call %CD%\%DEPENDENCY_INSTALLER_RELATIVE_PATH% %CD%\%RELATIVE_PATH_PYTHON_DEPENDENCIES%

REM === Voer de python code uit ===
:solution
echo [INFO] Druk op een toets om het script te starten.

pause

echo.
echo [INFO] Bezig met het uitvoeren van het Python-script. Moment gedult a.u.b.
echo.
:: py run argument 
python %PYTHON_SCRIPT_PATH%

echo [INFO] De Python-code is succesvol uitgevoerd.
echo.

:einde
echo [INFO] Script afsluiten. 
echo.
pause