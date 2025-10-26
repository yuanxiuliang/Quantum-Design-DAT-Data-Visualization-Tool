#!/bin/bash
# 创建macOS .dmg安装包

echo "开始创建macOS .dmg安装包..."

# 检查必要工具
if ! command -v hdiutil &> /dev/null; then
    echo "错误: hdiutil未找到，请确保在macOS系统上运行"
    exit 1
fi

# 创建临时目录
TEMP_DIR="temp_dmg"
APP_NAME="Quantum Design DAT Data Visualization Tool"
DMG_NAME="Quantum_Design_DAT_Data_Visualization_Tool_macOS"

# 清理旧文件
rm -rf "$TEMP_DIR"
rm -f "${DMG_NAME}.dmg"

# 创建目录结构
mkdir -p "$TEMP_DIR"
mkdir -p "$TEMP_DIR/.background"

# 复制可执行文件
if [ -f "Quantum Design DAT Data Visualization Tool" ]; then
    cp "Quantum Design DAT Data Visualization Tool" "$TEMP_DIR/"
    chmod +x "$TEMP_DIR/Quantum Design DAT Data Visualization Tool"
else
    echo "错误: 可执行文件未找到，请先运行 build_mac.sh"
    exit 1
fi

# 复制README
cp "README.md" "$TEMP_DIR/"

# 创建应用程序包结构
mkdir -p "$TEMP_DIR/${APP_NAME}.app/Contents/MacOS"
mkdir -p "$TEMP_DIR/${APP_NAME}.app/Contents/Resources"

# 移动可执行文件到应用程序包
mv "$TEMP_DIR/Quantum Design DAT Data Visualization Tool" "$TEMP_DIR/${APP_NAME}.app/Contents/MacOS/"

# 创建Info.plist
cat > "$TEMP_DIR/${APP_NAME}.app/Contents/Info.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>Quantum Design DAT Data Visualization Tool</string>
    <key>CFBundleIdentifier</key>
    <string>com.yuanxiuliang.quantum-design-dat-tool</string>
    <key>CFBundleName</key>
    <string>Quantum Design DAT Data Visualization Tool</string>
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

# 创建启动脚本
cat > "$TEMP_DIR/${APP_NAME}.app/Contents/MacOS/start.sh" << EOF
#!/bin/bash
cd "\$(dirname "\$0")"
./"Quantum Design DAT Data Visualization Tool"
EOF

chmod +x "$TEMP_DIR/${APP_NAME}.app/Contents/MacOS/start.sh"

# 创建DMG
echo "创建DMG文件..."
hdiutil create -volname "$APP_NAME" -srcfolder "$TEMP_DIR" -ov -format UDZO "${DMG_NAME}.dmg"

# 清理临时文件
rm -rf "$TEMP_DIR"

if [ -f "${DMG_NAME}.dmg" ]; then
    echo "✅ macOS .dmg安装包创建成功！"
    echo "文件位置: ${DMG_NAME}.dmg"
    echo "用户可以直接双击安装包进行安装"
else
    echo "❌ DMG创建失败"
    exit 1
fi
