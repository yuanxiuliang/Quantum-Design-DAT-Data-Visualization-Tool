# 构建说明

## 🚀 统一构建

### 快速构建
```bash
cd Releases/build
./build_all.sh
```

### 构建流程
1. **自动检测操作系统**
2. **本地构建macOS版本** - 生成 `../Quantum_Design_DAT_Tool_macOS.dmg`
3. **本地构建Windows版本** - 通过Wine生成 `../Quantum_Design_DAT_Tool_Windows.exe`
4. **自动清理中间文件** - 只保留最终安装包

### 最终输出
```
Releases/
├── build/
│   ├── build_all.sh                    # 统一构建脚本
│   └── BUILD.md                        # 构建说明
├── Quantum_Design_DAT_Tool_macOS.dmg   # macOS安装包
└── Quantum_Design_DAT_Tool_Windows.exe  # Windows安装包
```

## 📋 环境要求

### macOS构建
- Python 3.12.0 (推荐使用pyenv)
- create-dmg工具: `brew install create-dmg`
- 依赖包: `pip install pyinstaller pandas numpy matplotlib`

### Windows构建（macOS上）
- Wine环境: `brew install --cask wine-stable` 或 `brew install --cask wine-crossover`
- 自动下载Windows Python 3.12.0
- 自动安装PyInstaller和依赖包

### Windows构建（Windows系统）
- Python 3.12.0
- 依赖包: `pip install pyinstaller pandas numpy matplotlib`

## 🧹 自动清理

构建完成后，所有中间文件都会被自动清理：
- temp_* 目录
- build/, dist/ 目录
- .spec, .pyc 文件
- 只保留最终安装包和构建脚本
