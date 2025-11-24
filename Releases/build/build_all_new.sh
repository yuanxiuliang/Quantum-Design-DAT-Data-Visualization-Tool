#!/bin/bash
# 统一构建脚本 - 自动检测平台并调用相应构建脚本

echo "🚀 开始统一构建Quantum Design DAT Data Visualization Tool..."
echo "=================================================="

# 检测当前操作系统
OS=$(uname -s)
echo "📍 当前操作系统: $OS"

# 设置脚本目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 根据操作系统选择构建脚本
case "$OS" in
    Darwin*)
        echo "🍎 检测到macOS系统，使用macOS构建脚本..."
        if [ -f "$SCRIPT_DIR/build_macos.sh" ]; then
            chmod +x "$SCRIPT_DIR/build_macos.sh"
            exec "$SCRIPT_DIR/build_macos.sh"
        else
            echo "❌ 错误: 未找到macOS构建脚本 build_macos.sh"
            exit 1
        fi
        ;;
    CYGWIN*|MINGW*|MSYS*)
        echo "🪟 检测到Windows系统，使用Windows构建脚本..."
        if [ -f "$SCRIPT_DIR/build_windows.bat" ]; then
            exec "$SCRIPT_DIR/build_windows.bat"
        else
            echo "❌ 错误: 未找到Windows构建脚本 build_windows.bat"
            exit 1
        fi
        ;;
    Linux*)
        echo "🐧 检测到Linux系统..."
        echo "⚠️  Linux系统暂不支持图形界面构建，请使用命令行版本"
        echo "💡 建议在macOS或Windows系统中构建"
        exit 1
        ;;
    *)
        echo "❌ 错误: 未知操作系统 $OS"
        exit 1
        ;;
esac
