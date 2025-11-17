@echo off
echo Starting Windows build...
echo.

REM Clean old files
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

echo Building package, please wait...
echo This may take a few minutes...

REM Build with conservative parameters - only exclude test modules
pyinstaller --onefile ^
    --windowed ^
    --name "Quantum Design DAT Data Visualization Tool" ^
    --distpath "." ^
    --workpath "build" ^
    --exclude-module matplotlib.tests ^
    --exclude-module pandas.tests ^
    --exclude-module numpy.tests ^
    --exclude-module unittest ^
    --exclude-module pytest ^
    --exclude-module scipy ^
    --exclude-module sklearn ^
    --exclude-module IPython ^
    --exclude-module jupyter ^
    --exclude-module notebook ^
    --exclude-module sphinx ^
    --exclude-module setuptools ^
    --exclude-module pip ^
    --exclude-module wheel ^
    --exclude-module distutils ^
    --exclude-module pydoc ^
    --exclude-module doctest ^
    --exclude-module pdb ^
    --exclude-module profile ^
    --exclude-module pstats ^
    --exclude-module cProfile ^
    --strip ^
    --optimize 2 ^
    "..\..\Quantum Design DAT Data Visualization Tool.py"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Build successful!
    echo.
    
    REM Check file size
    for %%A in ("Quantum Design DAT Data Visualization Tool.exe") do (
        set /a size=%%~zA/1024/1024
        echo File size: !size! MB
    )
    
    echo.
    echo You can now test the optimized exe file!
) else (
    echo.
    echo Build failed, please check error messages
)

pause