@echo off
chcp 65001 >nul 2>&1
setlocal enabledelayedexpansion
REM Windows版本构建脚本 - 只输出最终安装包，清理所有过程文件

echo 🪟 开始构建Windows版本的Quantum Design DAT Data Visualization Tool...
echo ==================================================

REM 设置构建目录
set "SCRIPT_DIR=%~dp0"
REM 规范化路径：先切换到Releases目录，再切换到项目根目录
pushd "%SCRIPT_DIR%.."
set "RELEASES_DIR=%CD%"
popd
pushd "%SCRIPT_DIR%..\.."
set "PROJECT_ROOT=%CD%"
popd

REM 清理旧的安装包和临时文件
echo 🧹 清理旧的安装包和临时文件...
cd /d "%RELEASES_DIR%"
if exist "Quantum_Design_DAT_Tool_Windows.exe" del /q "Quantum_Design_DAT_Tool_Windows.exe"
for /d %%i in (temp_*) do rmdir /s /q "%%i" 2>nul
if exist "Quantum Design DAT Data Visualization Tool.spec" del /q "Quantum Design DAT Data Visualization Tool.spec"

REM 检查Python环境
echo 🐍 检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未找到Python，请先安装Python 3.12.0
    echo 下载地址: https://www.python.org/downloads/release/python-3120/
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ 使用Python: %PYTHON_VERSION%

REM 安装依赖（静默安装，只显示错误）
echo 📦 安装Python依赖...
python -m pip install --upgrade pip --quiet >nul 2>&1
python -m pip install pyinstaller pandas numpy matplotlib --quiet >nul 2>&1
if errorlevel 1 (
    echo ❌ 依赖安装失败，尝试非静默模式...
    python -m pip install --upgrade pip
    python -m pip install pyinstaller pandas numpy matplotlib
    if errorlevel 1 (
        echo ❌ 依赖安装失败
        pause
        exit /b 1
    )
)

REM 创建临时构建目录
set TEMP_BUILD_DIR=%RELEASES_DIR%\temp_windows_build
if exist "%TEMP_BUILD_DIR%" rmdir /s /q "%TEMP_BUILD_DIR%" 2>nul
mkdir "%TEMP_BUILD_DIR%" 2>nul

REM 复制源代码
echo [INFO] Copying source code...
if not exist "%PROJECT_ROOT%\Quantum Design DAT Data Visualization Tool.py" (
    echo ❌ 错误: 找不到源文件: "%PROJECT_ROOT%\Quantum Design DAT Data Visualization Tool.py"
    pause
    exit /b 1
)
copy "%PROJECT_ROOT%\Quantum Design DAT Data Visualization Tool.py" "%TEMP_BUILD_DIR%\" >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 复制源文件失败
    pause
    exit /b 1
)
if not exist "%TEMP_BUILD_DIR%\Quantum Design DAT Data Visualization Tool.py" (
    echo ❌ 错误: 源文件复制后未找到
    pause
    exit /b 1
)

REM 构建可执行文件（将输出重定向，只显示关键信息）
echo 🔨 构建可执行文件（这可能需要几分钟）...
cd /d "%TEMP_BUILD_DIR%"
python -m PyInstaller --onefile --windowed --name "Quantum Design DAT Data Visualization Tool" --clean --noconfirm "Quantum Design DAT Data Visualization Tool.py" >nul 2>&1

if errorlevel 1 (
    echo ❌ 静默构建失败，使用详细模式重新构建...
    python -m PyInstaller --onefile --windowed --name "Quantum Design DAT Data Visualization Tool" --clean --noconfirm "Quantum Design DAT Data Visualization Tool.py"
    if errorlevel 1 (
        echo ❌ 可执行文件构建失败
        cd /d "%RELEASES_DIR%"
        if exist "%TEMP_BUILD_DIR%" rmdir /s /q "%TEMP_BUILD_DIR%" 2>nul
        pause
        exit /b 1
    )
    echo ✅ 详细模式构建成功，继续后续步骤...
)

REM 复制最终安装包
if exist "dist\Quantum Design DAT Data Visualization Tool.exe" (
    echo 📦 生成最终安装包...
    copy "dist\Quantum Design DAT Data Visualization Tool.exe" "%RELEASES_DIR%\Quantum_Design_DAT_Tool_Windows.exe" >nul 2>&1
    
    REM 验证文件是否存在
    if exist "%RELEASES_DIR%\Quantum_Design_DAT_Tool_Windows.exe" (
        echo ✅ Windows版本构建成功！
        echo 📁 文件: %RELEASES_DIR%\Quantum_Design_DAT_Tool_Windows.exe
        for %%F in ("%RELEASES_DIR%\Quantum_Design_DAT_Tool_Windows.exe") do (
            set /a SIZE_MB=%%~zF/1048576
            echo 📏 大小: %%~zF bytes (约 !SIZE_MB! MB)
        )
    ) else (
        echo ❌ 安装包复制失败
        cd /d "%RELEASES_DIR%"
        if exist "%TEMP_BUILD_DIR%" rmdir /s /q "%TEMP_BUILD_DIR%" 2>nul
        pause
        exit /b 1
    )
) else (
    echo ❌ 可执行文件未找到
    cd /d "%RELEASES_DIR%"
    if exist "%TEMP_BUILD_DIR%" rmdir /s /q "%TEMP_BUILD_DIR%" 2>nul
    pause
    exit /b 1
)

REM 清理所有临时文件和过程文件
echo 🧹 清理所有过程文件...
cd /d "%TEMP_BUILD_DIR%"

REM 清理PyInstaller生成的所有文件
if exist "build" rmdir /s /q "build" 2>nul
if exist "dist" rmdir /s /q "dist" 2>nul
if exist "Quantum Design DAT Data Visualization Tool.spec" del /q "Quantum Design DAT Data Visualization Tool.spec" 2>nul
if exist "__pycache__" rmdir /s /q "__pycache__" 2>nul

REM 清理临时构建目录
cd /d "%RELEASES_DIR%"
if exist "%TEMP_BUILD_DIR%" rmdir /s /q "%TEMP_BUILD_DIR%" 2>nul

REM 清理项目根目录中可能生成的.spec文件
if exist "%PROJECT_ROOT%\Quantum Design DAT Data Visualization Tool.spec" del /q "%PROJECT_ROOT%\Quantum Design DAT Data Visualization Tool.spec" 2>nul

REM 清理Releases目录中可能残留的文件
if exist "%RELEASES_DIR%\Quantum Design DAT Data Visualization Tool.spec" del /q "%RELEASES_DIR%\Quantum Design DAT Data Visualization Tool.spec" 2>nul

echo.
echo 🎉 Windows版本构建完成！
echo 📦 安装包位置: %RELEASES_DIR%\Quantum_Design_DAT_Tool_Windows.exe
echo ✅ 所有过程文件已清理，只保留最终安装包
exit /b 0
