#!/bin/bash
# macOS构建脚本

echo "开始为macOS构建Quantum Design DAT Data Visualization Tool..."

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python3，请先安装Python3"
    exit 1
fi

# 安装依赖
echo "安装Python依赖..."
pip3 install pyinstaller pandas numpy matplotlib

# 创建构建目录
mkdir -p build_mac
mkdir -p dist_mac

# 使用PyInstaller构建
echo "开始打包..."
pyinstaller --onefile \
    --console \
    --name "Quantum Design DAT Data Visualization Tool" \
    --distpath "dist_mac" \
    --workpath "build_mac" \
    "Quantum Design DAT Data Visualization Tool.py"

if [ $? -eq 0 ]; then
    echo "✅ macOS版本构建成功！"
    echo "可执行文件位置: dist_mac/Quantum Design DAT Data Visualization Tool"
    echo "请将可执行文件复制到Releases/macOS-x64/目录"
else
    echo "❌ 构建失败，请检查错误信息"
    exit 1
fi
