#!/bin/bash
# Ubuntu/Debian自动安装脚本

echo "Quantum Design DAT Data Visualization Tool - Ubuntu/Debian 安装程序"
echo "=============================================================="

# 检查系统
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if command -v apt &> /dev/null; then
        echo "检测到Ubuntu/Debian系统"
    else
        echo "错误: 此脚本仅支持Ubuntu/Debian系统"
        exit 1
    fi
else
    echo "错误: 此脚本只能在Linux系统上运行"
    exit 1
fi

# 更新包管理器
echo "更新包管理器..."
sudo apt update

# 安装系统依赖
echo "安装系统依赖..."
sudo apt install -y python3 python3-pip python3-tk python3-dev

# 安装Python依赖
echo "安装Python依赖..."
pip3 install pandas numpy matplotlib

# 创建应用程序目录
APP_DIR="/opt/quantum-design-dat-tool"
sudo mkdir -p "$APP_DIR"

# 复制源代码
sudo cp "../../Quantum Design DAT Data Visualization Tool.py" "$APP_DIR/"
sudo chmod +x "$APP_DIR/Quantum Design DAT Data Visualization Tool.py"

# 创建启动脚本
sudo tee "$APP_DIR/start.sh" > /dev/null << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
python3 "Quantum Design DAT Data Visualization Tool.py"
EOF

sudo chmod +x "$APP_DIR/start.sh"

# 创建桌面快捷方式
cat > "/tmp/quantum-design-dat-tool.desktop" << EOF
[Desktop Entry]
Name=Quantum Design DAT Data Visualization Tool
Comment=Data visualization tool for Quantum Design devices
Exec=$APP_DIR/start.sh
Icon=applications-science
Terminal=true
Type=Application
Categories=Science;DataVisualization;
Version=1.0
EOF

sudo mv "/tmp/quantum-design-dat-tool.desktop" "/usr/share/applications/"

# 创建命令行链接
sudo ln -sf "$APP_DIR/start.sh" "/usr/local/bin/quantum-design-dat-tool"

echo "✅ 安装完成！"
echo "应用程序已安装到: $APP_DIR"
echo "您可以在应用程序菜单中找到程序，或使用命令: quantum-design-dat-tool"
