# 构建说明

## 🍎 macOS构建

### 环境要求
- macOS 10.14+ (支持Intel和Apple Silicon)
- Python 3.12.0
- Xcode Command Line Tools
- Homebrew

### 安装依赖
```bash
# 安装Python环境
brew install python@3.12 pyenv
pyenv install 3.12.0
pyenv global 3.12.0

# 安装构建工具
brew install create-dmg

# 安装Python依赖
pip install pyinstaller pandas numpy matplotlib
```

### 构建步骤
```bash
cd Releases/build
chmod +x build_macos.sh
./build_macos.sh
```

### 输出文件
- `Releases/Quantum_Design_DAT_Tool_macOS.dmg`
- 大小: 约40MB

---

## 🪟 Windows构建

### 环境要求
- Windows 7/8/10/11 (64位)
- Python 3.12.0

### 安装依赖
```cmd
# 下载Python 3.12.0
# https://www.python.org/downloads/release/python-3120/

# 安装Python依赖
python -m pip install --upgrade pip
python -m pip install pyinstaller pandas numpy matplotlib
```

### 构建步骤
```cmd
cd Releases\build
build_windows.bat
```

### 输出文件
- `Releases/Quantum_Design_DAT_Tool_Windows.exe`
- 大小: 约44MB

---

## 🔧 跨平台构建

### 在macOS上构建Windows版本（实验性）
```bash
# 安装Wine
brew install --cask wine-stable

# 使用Wine运行Windows构建脚本
wine build_windows.bat
```

**注意**: Wine构建可能遇到兼容性问题，建议在真实Windows环境中构建。

---

## 📦 发布流程

### 1. 构建各平台版本
```bash
# macOS构建
./build_macos.sh

# Windows构建（在Windows系统中）
build_windows.bat
```

### 2. 创建GitHub Release
```bash
# 使用GitHub CLI
gh release create v2.0.0 \
  Releases/Quantum_Design_DAT_Tool_macOS.dmg \
  Releases/Quantum_Design_DAT_Tool_Windows.exe \
  --title "Version 2.0.0" \
  --notes "智能选择系统、筛选标签、字体优化"
```

### 3. 更新README
- 更新版本号
- 更新下载链接
- 更新发布说明

---

## 🛠️ 故障排除

### macOS构建问题
- **Python路径错误**: 确保使用正确的Python路径
- **create-dmg错误**: 检查Homebrew安装
- **权限问题**: 使用`chmod +x`设置执行权限

### Windows构建问题
- **Python版本错误**: 确保使用Python 3.12.0
- **依赖安装失败**: 使用管理员权限运行
- **路径问题**: 确保在正确的目录中运行

### 通用问题
- **依赖冲突**: 使用虚拟环境
- **构建失败**: 检查Python和依赖版本
- **文件权限**: 确保有读写权限

---

## 📊 构建优化

### 减小文件大小
- 使用UPX压缩
- 排除不必要的依赖
- 优化导入语句

### 提高构建速度
- 使用缓存
- 并行构建
- 增量构建

### 安全性
- 代码签名
- 病毒扫描
- 安全审计
