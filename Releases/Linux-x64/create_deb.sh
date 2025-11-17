#!/bin/bash
# 创建Linux .deb安装包

echo "开始创建Linux .deb安装包..."

# 检查必要工具
if ! command -v dpkg-deb &> /dev/null; then
    echo "错误: dpkg-deb未找到，请安装: sudo apt install dpkg-dev"
    exit 1
fi

PACKAGE_NAME="quantum-design-dat-tool"
VERSION="1.0.0"
ARCH="amd64"
DEB_NAME="${PACKAGE_NAME}_${VERSION}_${ARCH}.deb"

# 清理旧文件
rm -rf "deb_build"
rm -f "$DEB_NAME"

# 创建deb包结构
mkdir -p "deb_build/DEBIAN"
mkdir -p "deb_build/usr/bin"
mkdir -p "deb_build/usr/share/applications"
mkdir -p "deb_build/usr/share/doc/${PACKAGE_NAME}"

# 复制可执行文件
if [ -f "Quantum Design DAT Data Visualization Tool" ]; then
    cp "Quantum Design DAT Data Visualization Tool" "deb_build/usr/bin/"
    chmod +x "deb_build/usr/bin/Quantum Design DAT Data Visualization Tool"
else
    echo "错误: 可执行文件未找到，请先运行 build_linux.sh"
    exit 1
fi

# 复制README
cp "README.md" "deb_build/usr/share/doc/${PACKAGE_NAME}/"

# 创建control文件
cat > "deb_build/DEBIAN/control" << EOF
Package: ${PACKAGE_NAME}
Version: ${VERSION}
Section: science
Priority: optional
Architecture: ${ARCH}
Depends: libc6 (>= 2.17), libgcc1 (>= 1:3.0), libstdc++6 (>= 4.8.1)
Maintainer: Yuan Xiuliang <yuanxiuliang8@outlook.com>
Description: Quantum Design DAT Data Visualization Tool
 A data visualization tool for Quantum Design devices (such as PPMS).
 Features include interactive zoom, data filtering, and multiple plot types.
 Supports both Chinese and English interfaces.
Homepage: https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool
EOF

# 创建postinst脚本
cat > "deb_build/DEBIAN/postinst" << EOF
#!/bin/bash
set -e
# 创建桌面快捷方式
if [ -d "/usr/share/applications" ]; then
    cat > /usr/share/applications/quantum-design-dat-tool.desktop << 'DESKTOP_EOF'
[Desktop Entry]
Name=Quantum Design DAT Data Visualization Tool
Comment=Data visualization tool for Quantum Design devices
Exec=Quantum Design DAT Data Visualization Tool
Icon=applications-science
Terminal=true
Type=Application
Categories=Science;DataVisualization;
Version=1.0
DESKTOP_EOF
fi
exit 0
EOF

chmod +x "deb_build/DEBIAN/postinst"

# 创建prerm脚本
cat > "deb_build/DEBIAN/prerm" << EOF
#!/bin/bash
set -e
# 删除桌面快捷方式
rm -f /usr/share/applications/quantum-design-dat-tool.desktop
exit 0
EOF

chmod +x "deb_build/DEBIAN/prerm"

# 创建copyright文件
cat > "deb_build/usr/share/doc/${PACKAGE_NAME}/copyright" << EOF
Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: Quantum Design DAT Data Visualization Tool
Source: https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool

Files: *
Copyright: 2025 Yuan Xiuliang <yuanxiuliang8@outlook.com>
License: MIT

Files: debian/*
Copyright: 2025 Yuan Xiuliang <yuanxiuliang8@outlook.com>
License: MIT

License: MIT
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 .
 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.
 .
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
EOF

# 创建changelog
cat > "deb_build/usr/share/doc/${PACKAGE_NAME}/changelog.Debian" << EOF
${PACKAGE_NAME} (${VERSION}) unstable; urgency=medium

  * Initial release
  * Quantum Design DAT data visualization tool
  * Interactive zoom and data filtering features
  * Multi-language support (Chinese/English)

 -- Yuan Xiuliang <yuanxiuliang8@outlook.com>  $(date -R)
EOF

gzip -9 "deb_build/usr/share/doc/${PACKAGE_NAME}/changelog.Debian"

# 创建deb包
echo "创建.deb包..."
dpkg-deb --build "deb_build" "$DEB_NAME"

# 清理临时文件
rm -rf "deb_build"

if [ -f "$DEB_NAME" ]; then
    echo "✅ Linux .deb安装包创建成功！"
    echo "文件位置: $DEB_NAME"
    echo "安装方法: sudo dpkg -i $DEB_NAME"
    echo "用户可以直接双击安装包进行安装"
else
    echo "❌ .deb包创建失败"
    exit 1
fi
