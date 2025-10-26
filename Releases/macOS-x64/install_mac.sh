#!/bin/bash
# macOS自动安装脚本

echo "Quantum Design DAT Data Visualization Tool - macOS 安装程序"
echo "=================================================="

# 检查系统
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "错误: 此脚本只能在macOS系统上运行"
    exit 1
fi

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "正在安装Python3..."
    if command -v brew &> /dev/null; then
        brew install python3
    else
        echo "请先安装Homebrew: https://brew.sh/"
        exit 1
    fi
fi

# 安装依赖
echo "安装Python依赖..."
pip3 install pandas numpy matplotlib pyinstaller

# 创建应用程序包
echo "创建应用程序包..."
APP_NAME="Quantum Design DAT Data Visualization Tool"
APP_DIR="/Applications/${APP_NAME}.app"

# 创建应用程序结构
mkdir -p "${APP_DIR}/Contents/MacOS"
mkdir -p "${APP_DIR}/Contents/Resources"

# 复制源代码
cp "../../Quantum Design DAT Data Visualization Tool.py" "${APP_DIR}/Contents/MacOS/"

# 创建启动脚本
cat > "${APP_DIR}/Contents/MacOS/start.sh" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
python3 "Quantum Design DAT Data Visualization Tool.py"
EOF

chmod +x "${APP_DIR}/Contents/MacOS/start.sh"

# 创建Info.plist
cat > "${APP_DIR}/Contents/Info.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>start.sh</string>
    <key>CFBundleIdentifier</key>
    <string>com.yuanxiuliang.quantum-design-dat-tool</string>
    <key>CFBundleName</key>
    <string>${APP_NAME}</string>
    <key>CFBundleVersion</key>
    <string>1.0.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.14</string>
</dict>
</plist>
EOF

echo "✅ 安装完成！"
echo "应用程序已安装到: ${APP_DIR}"
echo "您可以在Applications文件夹中找到并运行应用程序"
