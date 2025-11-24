# 打包说明

## 📦 项目打包指南

本项目提供了标准化的打包脚本，支持macOS和Windows两个平台。

---

## 🍎 macOS打包

### 环境要求
- macOS 10.14+ (支持Intel和Apple Silicon)
- Python 3.12.0
- Xcode Command Line Tools
- Homebrew (可选，用于安装依赖)

### 快速打包
```bash
cd Releases/build
./build_macos.sh
```

### 输出文件
- **文件名**: `Quantum_Design_DAT_Tool_macOS.dmg`
- **位置**: `Releases/`目录
- **大小**: 约37MB
- **安装方式**: 标准拖拽安装

### 安装流程
1. 双击DMG文件挂载
2. 将应用程序拖拽到Applications文件夹
3. 在Launchpad或Applications中启动应用

---

## 🪟 Windows打包

### 环境要求
- Windows 7/8/10/11 (64位)
- Python 3.12.0

### 快速打包
```cmd
cd Releases\build
build_windows.bat
```

### 输出文件
- **文件名**: `Quantum_Design_DAT_Tool_Windows.exe`
- **位置**: `Releases\`目录
- **大小**: 约44MB
- **安装方式**: 直接运行

---

## 🔧 打包特性

### 干净打包原则
- ✅ **只产生最终安装包**: 无中间文件残留
- ✅ **自动清理**: 构建完成后自动清理临时文件
- ✅ **标准化输出**: 符合各平台的标准安装流程

### 自动化功能
- **依赖检查**: 验证必要工具和库
- **环境检测**: 自动识别Python环境
- **错误处理**: 详细的错误信息和退出码
- **文件清理**: 自动删除所有临时文件

---

## 📁 项目结构

```
Quantum-Design-DAT-Data-Visualization-Tool/
├── Quantum Design DAT Data Visualization Tool.py  # 源代码
├── requirements.txt                               # 依赖文件
├── README.md                                     # 项目说明
└── Releases/
    ├── Quantum_Design_DAT_Tool_macOS.dmg         # macOS安装包
    ├── Quantum_Design_DAT_Tool_Windows.exe        # Windows安装包
    └── build/
        ├── build_macos.sh                        # macOS打包脚本
        ├── build_windows.bat                     # Windows打包脚本
        └── PACKAGING.md                          # 本说明文档
```

---

## 🛠️ 故障排除

### macOS打包问题

#### Python环境错误
```bash
# 安装Python 3.12.0
brew install python@3.12 pyenv
pyenv install 3.12.0
pyenv global 3.12.0
```

#### 依赖安装失败
```bash
# 手动安装依赖
pip install pyinstaller pandas numpy matplotlib
```

#### DMG创建失败
- 检查磁盘空间是否充足
- 确保没有其他DMG挂载
- 重启系统后重试

### Windows打包问题

#### Python未找到
- 下载Python 3.12.0: https://www.python.org/downloads/release/python-3120/
- 安装时勾选"Add Python to PATH"

#### 依赖安装失败
```cmd
# 使用管理员权限运行
python -m pip install --upgrade pip
python -m pip install pyinstaller pandas numpy matplotlib
```

#### 构建失败
- 检查防病毒软件是否阻止
- 确保有足够的磁盘空间
- 以管理员身份运行脚本

---

## 📋 发布流程

### 1. 构建各平台版本
```bash
# macOS构建
./build_macos.sh

# Windows构建（在Windows系统中）
build_windows.bat
```

### 2. 验证安装包
- 测试DMG挂载和拖拽安装
- 测试EXE文件运行
- 检查文件大小和完整性

### 3. 创建GitHub Release
```bash
# 使用GitHub CLI
gh release create v2.0.0 \
  Releases/Quantum_Design_DAT_Tool_macOS.dmg \
  Releases/Quantum_Design_DAT_Tool_Windows.exe \
  --title "Version 2.0.0" \
  --notes "智能选择系统、筛选标签、字体优化"
```

### 4. 更新文档
- 更新README.md中的版本号
- 更新下载链接
- 更新发布说明

---

## 🎯 最佳实践

### 开发环境
- 使用虚拟环境隔离依赖
- 定期更新构建工具
- 保持Python版本一致

### 版本管理
- 使用语义化版本号
- 每次发布前完整测试
- 保留发布说明

### 质量保证
- 在多个系统版本上测试
- 检查安装包完整性
- 验证安装流程

---

## 📞 技术支持

如果遇到打包问题，请：

1. 检查本说明文档的故障排除部分
2. 确认环境要求已满足
3. 查看构建脚本的错误信息
4. 在GitHub Issues中报告问题

---

**最后更新**: 2024年11月24日  
**版本**: v2.0.0
