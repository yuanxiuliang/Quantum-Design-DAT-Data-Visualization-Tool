@echo off
REM Windows版本构建脚本

echo 🪟 开始构建Windows版本的Quantum Design DAT Data Visualization Tool...
echo ==================================================

REM 设置构建目录
set SCRIPT_DIR=%~dp0
set RELEASES_DIR=%SCRIPT_DIR%..
set PROJECT_ROOT=%RELEASES_DIR%..

REM 清理旧的安装包和临时文件
echo 🧹 清理旧的安装包...
cd /d "%RELEASES_DIR%"
if exist "Quantum_Design_DAT_Tool_Windows.exe" del "Quantum_Design_DAT_Tool_Windows.exe"
for /d %%i in (temp_*) do rmdir /s /q "%%i"
if exist "Quantum Design DAT Data Visualization Tool.spec" del "Quantum Design DAT Data Visualization Tool.spec"

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

REM 安装依赖
echo 📦 安装Python依赖...
python -m pip install --upgrade pip
python -m pip install pyinstaller pandas numpy matplotlib

REM 创建临时构建目录
set TEMP_BUILD_DIR=%RELEASES_DIR%\temp_windows_build
if exist "%TEMP_BUILD_DIR%" rmdir /s /q "%TEMP_BUILD_DIR%"
mkdir "%TEMP_BUILD_DIR%"

REM 复制源代码
echo 📋 复制源代码...
copy "%PROJECT_ROOT%\Quantum Design DAT Data Visualization Tool.py" "%TEMP_BUILD_DIR%\"

REM 构建可执行文件
echo 🔨 构建可执行文件...
cd /d "%TEMP_BUILD_DIR%"
python -m PyInstaller --onefile --windowed --name "Quantum Design DAT Data Visualization Tool" "Quantum Design DAT Data Visualization Tool.py"

if errorlevel 1 (
    echo ❌ 可执行文件构建失败
    pause
    exit /b 1
)

echo ✅ 可执行文件构建成功！

REM 重命名可执行文件
echo 📦 重命名可执行文件...
if exist "dist\Quantum Design DAT Data Visualization Tool.exe" (
    copy "dist\Quantum Design DAT Data Visualization Tool.exe" "%RELEASES_DIR%\Quantum_Design_DAT_Tool_Windows.exe"
    echo ✅ Windows版本构建成功！
    echo 📁 文件: %RELEASES_DIR%\Quantum_Design_DAT_Tool_Windows.exe
    for %%F in ("%RELEASES_DIR%\Quantum_Design_DAT_Tool_Windows.exe") do echo 📏 大小: %%~zF bytes
) else (
    echo ❌ 可执行文件未找到
    pause
    exit /b 1
)

REM 清理临时文件
echo 🧹 清理临时文件...
if exist "%TEMP_BUILD_DIR%" rmdir /s /q "%TEMP_BUILD_DIR%"
if exist "%PROJECT_ROOT%\Quantum Design DAT Data Visualization Tool.spec" del "%PROJECT_ROOT%\Quantum Design DAT Data Visualization Tool.spec"

echo 🎉 Windows版本构建完成！
echo 📦 安装包位置: %RELEASES_DIR%\Quantum_Design_DAT_Tool_Windows.exe
pause
