#!/bin/bash
# macOS版本构建脚本

echo "🍎 开始构建macOS版本的Quantum Design DAT Data Visualization Tool..."
echo "=================================================="

# 设置构建目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RELEASES_DIR="$(dirname "$SCRIPT_DIR")"
PROJECT_ROOT="$(dirname "$RELEASES_DIR")"

# 清理旧的安装包
echo "🧹 清理旧的安装包..."
cd "$RELEASES_DIR"
rm -f "Quantum_Design_DAT_Tool_macOS.dmg"
rm -f "Quantum Design DAT Data Visualization Tool.spec"

# 设置Python路径
PYTHON_PATH="$HOME/.pyenv/versions/3.12.0/bin/python3"
PIP_PATH="$HOME/.pyenv/versions/3.12.0/bin/pip3"

# 检查Python环境
if [ ! -f "$PYTHON_PATH" ]; then
    echo "❌ 错误: 未找到Python 3.12.0，请先配置环境"
    echo "请运行: brew install python@3.12 pyenv && pyenv install 3.12.0 && pyenv global 3.12.0"
    exit 1
fi

echo "✅ 使用Python: $($PYTHON_PATH --version)"

# 安装依赖
echo "📦 安装Python依赖..."
$PIP_PATH install pyinstaller pandas numpy matplotlib

# 检查create-dmg
if ! command -v create-dmg &> /dev/null; then
    echo "❌ 错误: create-dmg未找到，请先安装: brew install create-dmg"
    exit 1
fi

# 创建临时构建目录
TEMP_BUILD_DIR="$RELEASES_DIR/temp_macos_build"
rm -rf "$TEMP_BUILD_DIR"
mkdir -p "$TEMP_BUILD_DIR"

# 复制源代码
echo "📋 复制源代码..."
cp "$PROJECT_ROOT/Quantum Design DAT Data Visualization Tool.py" "$TEMP_BUILD_DIR/"

# 构建可执行文件
echo "🔨 构建可执行文件..."
cd "$TEMP_BUILD_DIR"
$PYTHON_PATH -m PyInstaller --onefile --windowed --name "Quantum Design DAT Data Visualization Tool" "Quantum Design DAT Data Visualization Tool.py"

if [ $? -eq 0 ]; then
    echo "✅ 可执行文件构建成功！"
else
    echo "❌ 可执行文件构建失败"
    exit 1
fi

# 创建DMG安装包
echo "📀 开始创建DMG安装包..."

# 创建DMG目录
DMG_DIR="$TEMP_BUILD_DIR/dmg"
rm -rf "$DMG_DIR"
mkdir -p "$DMG_DIR"

# 复制应用程序到DMG目录
cp -r "$TEMP_BUILD_DIR/dist/Quantum Design DAT Data Visualization Tool.app" "$DMG_DIR/"

# 创建DMG
DMG_NAME="Quantum_Design_DAT_Tool_macOS"
DMG_PATH="$RELEASES_DIR/${DMG_NAME}.dmg"

echo "📀 创建DMG文件..."
# 使用hdiutil创建简单的DMG
hdiutil create -volname "Quantum Design DAT Tool" -srcfolder "$DMG_DIR" -ov -format UDZO "$DMG_PATH"

if [ $? -eq 0 ]; then
    echo "✅ macOS版本构建成功！"
    echo "📁 文件: $DMG_PATH"
    echo "📏 大小: $(du -sh "$DMG_PATH" | cut -f1)"
else
    echo "❌ macOS DMG创建失败"
    exit 1
fi

# 清理临时文件
echo "🧹 清理临时文件..."
rm -rf "$TEMP_BUILD_DIR"

echo "🎉 macOS版本构建完成！"
echo "📦 安装包位置: $DMG_PATH"
