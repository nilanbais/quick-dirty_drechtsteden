@echo off
setlocal EnableDelayedExpansion

set "ENV_FILE_PATH=%CD%\.env"
set "INPUT_FOLDER_PATH=%CD%\input"
set "OUTPUT_FOLDER_PATH=%CD%\rapportage_dataset"

echo INPUT_FOLDER_PATH=%INPUT_FOLDER_PATH% > %ENV_FILE_PATH%
echo OUTPUT_FOLDER_PATH=%OUTPUT_FOLDER_PATH% >> %ENV_FILE_PATH%
