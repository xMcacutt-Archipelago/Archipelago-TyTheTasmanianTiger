@echo off
setlocal EnableExtensions

set "RUN_TEMPLATE=0"

for %%A in (%*) do (
    if "%%A"=="-t" set RUN_TEMPLATE=1
)

if %RUN_TEMPLATE%==1 (
    py launcher.py "Generate Template Options"
)

copy ".\Players\Templates\Ty_the_Tasmanian_Tiger.yaml" ".\Players\"

if exist ".\output\" (
    del /q ".\output\*"
)

py generate.py

set "LATEST_ZIP="
for /f "delims=" %%F in ('dir ".\output\*.zip" /b /a-d /o-d 2^>nul') do (
    set "LATEST_ZIP=.\output\%%F"
    goto :found
)

:found
if not defined LATEST_ZIP (
    echo ERROR: No zip files found in .\output
    exit /b 1
)

py MultiServer.py "%LATEST_ZIP%"
