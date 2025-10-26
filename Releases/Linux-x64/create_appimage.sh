#!/bin/bash
# 创建Linux AppImage便携式应用

echo "开始创建Linux AppImage便携式应用..."

# 检查必要工具
if ! command -v wget &> /dev/null; then
    echo "错误: wget未找到，请安装: sudo apt install wget"
    exit 1
fi

APP_NAME="Quantum Design DAT Data Visualization Tool"
APPIMAGE_NAME="Quantum_Design_DAT_Data_Visualization_Tool_Linux"

# 清理旧文件
rm -f "${APPIMAGE_NAME}.AppImage"
rm -rf "AppDir"

# 创建AppDir结构
mkdir -p "AppDir/usr/bin"
mkdir -p "AppDir/usr/share/applications"
mkdir -p "AppDir/usr/share/icons"

# 复制可执行文件
if [ -f "Quantum Design DAT Data Visualization Tool" ]; then
    cp "Quantum Design DAT Data Visualization Tool" "AppDir/usr/bin/"
    chmod +x "AppDir/usr/bin/Quantum Design DAT Data Visualization Tool"
else
    echo "错误: 可执行文件未找到，请先运行 build_linux.sh"
    exit 1
fi

# 复制README
cp "README.md" "AppDir/"

# 创建.desktop文件
cat > "AppDir/usr/share/applications/quantum-design-dat-tool.desktop" << EOF
[Desktop Entry]
Name=Quantum Design DAT Data Visualization Tool
Comment=Data visualization tool for Quantum Design devices
Exec=Quantum Design DAT Data Visualization Tool
Icon=quantum-design-dat-tool
Terminal=true
Type=Application
Categories=Science;DataVisualization;
Version=1.0
EOF

# 创建AppRun脚本
cat > "AppDir/AppRun" << EOF
#!/bin/bash
HERE="\$(dirname "\$(readlink -f "\${0}")")"
export PATH="\${HERE}/usr/bin:\${PATH}"
export LD_LIBRARY_PATH="\${HERE}/usr/lib:\${LD_LIBRARY_PATH}"
exec "\${HERE}/usr/bin/Quantum Design DAT Data Visualization Tool" "\$@"
EOF

chmod +x "AppDir/AppRun"

# 下载AppImageTool
if [ ! -f "appimagetool-x86_64.AppImage" ]; then
    echo "下载AppImageTool..."
    wget -q "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
    chmod +x "appimagetool-x86_64.AppImage"
fi

# 创建AppImage
echo "创建AppImage文件..."
./appimagetool-x86_64.AppImage "AppDir" "${APPIMAGE_NAME}.AppImage"

# 清理临时文件
rm -rf "AppDir"

if [ -f "${APPIMAGE_NAME}.AppImage" ]; then
    echo "✅ Linux AppImage创建成功！"
    echo "文件位置: ${APPIMAGE_NAME}.AppImage"
    echo "用户可以直接双击运行，无需安装"
    echo "使用方法: chmod +x ${APPIMAGE_NAME}.AppImage && ./${APPIMAGE_NAME}.AppImage"
else
    echo "❌ AppImage创建失败"
    exit 1
fi
