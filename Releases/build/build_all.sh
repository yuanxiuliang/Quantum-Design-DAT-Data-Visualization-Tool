#!/bin/bash
# 统一构建脚本 - 自动构建Windows和macOS安装包

echo "🚀 开始统一构建Quantum Design DAT Data Visualization Tool..."
echo "=================================================="

# 检测当前操作系统
OS=$(uname -s)
echo "📍 当前操作系统: $OS"

# 设置构建目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RELEASES_DIR="$(dirname "$SCRIPT_DIR")"
PROJECT_ROOT="$(dirname "$RELEASES_DIR")"

# 清理旧的安装包
echo "🧹 清理旧的安装包..."
cd "$RELEASES_DIR"
rm -f "Quantum_Design_DAT_Tool_Windows.exe"
rm -f "Quantum_Design_DAT_Tool_macOS.dmg"
rm -f "Quantum Design DAT Data Visualization Tool.spec"  # 清理PyInstaller生成的spec文件

# 构建macOS版本（如果在macOS上）
if [[ "$OS" == "Darwin" ]]; then
    echo ""
    echo "🍎 开始构建macOS版本..."
    
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
    TEMP_BUILD_DIR="temp_macos_build"
    mkdir -p "$TEMP_BUILD_DIR/build_mac"
    mkdir -p "$TEMP_BUILD_DIR/dist_mac"
    
    # 清理PyInstaller缓存
    rm -rf ~/Library/Application\ Support/pyinstaller
    
    # 使用PyInstaller构建
    echo "🔨 开始打包可执行文件..."
    $PYTHON_PATH -m PyInstaller --onedir \
        --windowed \
        --name "Quantum Design DAT Data Visualization Tool" \
        --distpath "$TEMP_BUILD_DIR/dist_mac" \
        --workpath "$TEMP_BUILD_DIR/build_mac" \
        "$PROJECT_ROOT/Quantum Design DAT Data Visualization Tool.py"
    
    if [ $? -ne 0 ]; then
        echo "❌ macOS可执行文件构建失败"
        rm -rf "$TEMP_BUILD_DIR"
        exit 1
    fi
    
    echo "✅ 可执行文件构建成功！"
    
    # 创建DMG安装包
    echo "📀 开始创建DMG安装包..."
    
    TEMP_DMG_DIR="temp_dmg_build"
    DMG_NAME="Quantum_Design_DAT_Tool_macOS"
    
    # 清理旧文件
    rm -rf "$TEMP_DMG_DIR"
    rm -f "${DMG_NAME}.dmg"
    
    # 创建DMG临时目录结构
    mkdir -p "$TEMP_DMG_DIR"
    
    # 复制可执行文件目录
    if [ -d "$TEMP_BUILD_DIR/dist_mac/Quantum Design DAT Data Visualization Tool" ]; then
        cp -r "$TEMP_BUILD_DIR/dist_mac/Quantum Design DAT Data Visualization Tool" "$TEMP_DMG_DIR/"
        chmod +x "$TEMP_DMG_DIR/Quantum Design DAT Data Visualization Tool/Quantum Design DAT Data Visualization Tool"
    else
        echo "❌ 错误: 可执行文件目录未找到"
        rm -rf "$TEMP_BUILD_DIR" "$TEMP_DMG_DIR"
        exit 1
    fi
    
    # 创建标准的应用程序包
    APP_NAME="Quantum Design DAT Data Visualization Tool"
    APP_DIR="$TEMP_DMG_DIR/${APP_NAME}.app"
    mkdir -p "$APP_DIR/Contents/MacOS"
    mkdir -p "$APP_DIR/Contents/Resources"
    
    # 先复制整个目录
    cp -r "$TEMP_DMG_DIR/Quantum Design DAT Data Visualization Tool" "$APP_DIR/Contents/MacOS/"
    
    # 创建正确的启动脚本
    cat > "$APP_DIR/Contents/MacOS/run_app.sh" << 'EOF'
#!/bin/bash
# Apple Silicon兼容启动脚本

# 获取应用程序包资源目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_DIR="$SCRIPT_DIR/Quantum Design DAT Data Visualization Tool"

# 设置环境变量
export PYTHONPATH="$APP_DIR"
export DYLD_LIBRARY_PATH="$APP_DIR:$DYLD_LIBRARY_PATH"

# 切换到应用程序目录并运行
cd "$APP_DIR"
exec ./Quantum\ Design\ DAT\ Data\ Visualization\ Tool "$@"
EOF
    
    chmod +x "$APP_DIR/Contents/MacOS/run_app.sh"
    
    # 创建Info.plist
    cat > "$APP_DIR/Contents/Info.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>run_app.sh</string>
    <key>CFBundleIdentifier</key>
    <string>com.yuanxiuliang.quantum-design-dat-tool</string>
    <key>CFBundleName</key>
    <string>Quantum Design DAT Data Visualization Tool</string>
    <key>CFBundleDisplayName</key>
    <string>Quantum Design DAT Tool</string>
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
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>LSApplicationCategoryType</key>
    <string>public.app-category.education</string>
    <key>CFBundleSupportedPlatforms</key>
    <array>
        <string>MacOSX</string>
    </array>
    <key>LSArchitecturePriority</key>
    <array>
        <string>arm64</string>
        <string>x86_64</string>
    </array>
    <key>NSSupportsAutomaticGraphicsSwitching</key>
    <true/>
    <key>NSRequiresAquaSystemAppearance</key>
    <false/>
</dict>
</plist>
EOF
    
    # 移除原始目录
    rm -rf "$TEMP_DMG_DIR/Quantum Design DAT Data Visualization Tool"
    
    # 创建DMG
    echo "📀 创建DMG文件..."
    create-dmg \
        --volname "Quantum Design DAT Tool" \
        --window-pos 200 120 \
        --window-size 550 350 \
        --icon-size 100 \
        --icon "${APP_NAME}.app" 200 120 \
        --hide-extension "${APP_NAME}.app" \
        --app-drop-link 350 120 \
        --disk-image-size 100 \
        "${DMG_NAME}.dmg" \
        "$TEMP_DMG_DIR"
    
    DMG_EXIT_CODE=$?
    
    # 强制卸载可能挂载的DMG
    hdiutil detach /Volumes/dmg.* -force 2>/dev/null || true
    
    # 清理所有临时文件和中间目录
    rm -rf "$TEMP_BUILD_DIR"
    rm -rf "$TEMP_DMG_DIR"
    
    if [ $DMG_EXIT_CODE -eq 0 ] && [ -f "${DMG_NAME}.dmg" ]; then
        mv "${DMG_NAME}.dmg" "Quantum_Design_DAT_Tool_macOS.dmg"
        echo "✅ macOS版本构建成功！"
        echo "📁 文件: Quantum_Design_DAT_Tool_macOS.dmg"
        echo "📏 大小: $(du -sh "Quantum_Design_DAT_Tool_macOS.dmg" | cut -f1)"
    else
        echo "❌ macOS DMG创建失败"
        exit 1
    fi
else
    echo "⚠️  当前不是macOS系统，跳过macOS构建"
fi

# 构建Windows版本（如果在macOS上，使用Wine）
if [[ "$OS" == "Darwin" ]]; then
    echo ""
    echo "🪟 开始构建Windows版本..."
    
    # 检查Wine是否安装
    if ! command -v wine &> /dev/null; then
        echo "❌ 错误: Wine未找到，请先安装: brew install --cask wine-stable"
        echo "或者使用: brew install --cask wine-crossover"
        exit 1
    fi
    
    echo "✅ 使用Wine构建Windows版本"
    
    # 创建Wine环境
    WINE_PREFIX="$HOME/.wine_quantum_design"
    export WINEPREFIX="$WINE_PREFIX"
    
    # 初始化Wine环境（如果需要）
    if [ ! -d "$WINE_PREFIX" ]; then
        echo "🔧 初始化Wine环境..."
        winecfg --auto 2>/dev/null || true
    fi
    
    # 下载Windows Python（如果不存在）
    PYTHON_WINDOWS_URL="https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe"
    PYTHON_INSTALLER="$TEMP_BUILD_DIR/python-3.12.0-amd64.exe"
    
    if [ ! -f "$PYTHON_INSTALLER" ]; then
        echo "📥 下载Windows Python 3.12.0..."
        curl -L -o "$PYTHON_INSTALLER" "$PYTHON_WINDOWS_URL"
    fi
    
    # 安装Python到Wine环境（如果未安装）
    WINE_PYTHON="$WINE_PREFIX/drive_c/python312/python.exe"
    if [ ! -f "$WINE_PYTHON" ]; then
        echo "� 在Wine中安装Python 3.12.0..."
        wine "$PYTHON_INSTALLER" /quiet InstallAllUsers=0 TargetDir="C:\\python312" PrependPath=0
        
        # 等待安装完成
        sleep 10
    fi
    
    if [ ! -f "$WINE_PYTHON" ]; then
        echo "❌ Wine Python安装失败"
        exit 1
    fi
    
    echo "✅ Wine Python安装成功"
    
    # 安装Python依赖
    echo "📦 安装Windows Python依赖..."
    wine "$WINE_PYTHON" -m pip install --upgrade pip
    wine "$WINE_PYTHON" -m pip install pyinstaller pandas numpy matplotlib
    
    # 使用PyInstaller构建Windows版本
    echo "🔨 开始打包Windows可执行文件..."
    wine "$WINE_PYTHON" -m PyInstaller --onefile \
        --windowed \
        --name "Quantum Design DAT Data Visualization Tool" \
        --distpath "$TEMP_BUILD_DIR/dist_windows" \
        --workpath "$TEMP_BUILD_DIR/build_windows" \
        --exclude-module matplotlib.tests \
        --exclude-module pandas.tests \
        --exclude-module numpy.tests \
        --exclude-module unittest \
        --exclude-module pytest \
        --exclude-module scipy \
        --exclude-module sklearn \
        --exclude-module IPython \
        --exclude-module jupyter \
        --exclude-module notebook \
        --exclude-module sphinx \
        --exclude-module setuptools \
        --exclude-module pip \
        --exclude-module wheel \
        --exclude-module distutils \
        --exclude-module pydoc \
        --exclude-module doctest \
        --exclude-module pdb \
        --exclude-module profile \
        --exclude-module pstats \
        --exclude-module cProfile \
        --strip \
        --optimize 2 \
        "$PROJECT_ROOT/Quantum Design DAT Data Visualization Tool.py"
    
    if [ $? -ne 0 ]; then
        echo "❌ Windows可执行文件构建失败"
        exit 1
    fi
    
    echo "✅ Windows可执行文件构建成功！"
    
    # 复制Windows安装包到Releases目录
    if [ -f "$TEMP_BUILD_DIR/dist_windows/Quantum Design DAT Data Visualization Tool.exe" ]; then
        cp "$TEMP_BUILD_DIR/dist_windows/Quantum Design DAT Data Visualization Tool.exe" "$RELEASES_DIR/Quantum_Design_DAT_Tool_Windows.exe"
        echo "✅ Windows安装包: Quantum_Design_DAT_Tool_Windows.exe ($(du -sh "$RELEASES_DIR/Quantum_Design_DAT_Tool_Windows.exe" | cut -f1))"
    else
        echo "❌ Windows安装包未找到"
        exit 1
    fi
    
elif [[ "$OS" == "Linux" ]]; then
    echo "⚠️  Linux系统暂不支持Windows构建"
    echo "如需Windows版本，请使用GitHub Actions或在Windows系统上构建"
else
    echo "⚠️  当前系统不支持Windows构建"
fi

# 检查最终的构建结果
echo ""
echo "=================================================="
echo "🎉 构建完成！"
echo ""

# 检查macOS文件
if [ -f "Quantum_Design_DAT_Tool_macOS.dmg" ]; then
    echo "✅ macOS安装包: Quantum_Design_DAT_Tool_macOS.dmg ($(du -sh "Quantum_Design_DAT_Tool_macOS.dmg" | cut -f1))"
else
    echo "❌ macOS安装包: 未找到"
fi

# 检查Windows文件
if [ -f "Quantum_Design_DAT_Tool_Windows.exe" ]; then
    echo "✅ Windows安装包: Quantum_Design_DAT_Tool_Windows.exe ($(du -sh "Quantum_Design_DAT_Tool_Windows.exe" | cut -f1))"
else
    echo "❌ Windows安装包: 未找到"
fi

echo ""
echo "📁 构建文件位置: $(pwd)"
echo "🚀 可以开始发布这些安装包了！"

# 清理触发文件
rm -f .build-trigger

# 最终清理所有临时文件
echo "🧹 最终清理..."
rm -f "Quantum Design DAT Data Visualization Tool.spec"  # 清理PyInstaller生成的spec文件
