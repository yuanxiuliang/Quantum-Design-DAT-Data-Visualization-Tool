# Quantum Design DAT Data Visualization Tool - 多平台发布

## 📦 发布版本

本工具支持多个操作系统平台，请根据您的系统选择对应的版本：

### 🪟 Windows x64
- **位置**: `Windows-x64/`
- **文件**: `Quantum Design DAT Data Visualization Tool.exe`
- **特点**: 即开即用，无需安装Python环境
- **系统要求**: Windows 7/8/10/11 (64位)

### 🍎 macOS x64
- **位置**: `macOS-x64/`
- **文件**: 一键安装脚本 + 可执行文件 + 构建脚本
- **特点**: 一键安装，自动配置，即开即用
- **系统要求**: macOS 10.14+

### 🐧 Linux x64
- **位置**: `Linux-x64/`
- **文件**: 一键安装脚本 + 可执行文件 + 构建脚本
- **特点**: 支持Ubuntu/Debian/CentOS，一键安装，自动配置
- **系统要求**: Ubuntu 18.04+ / CentOS 7+ / Debian 10+

## 🚀 快速开始

### Windows用户
1. 进入 `Windows-x64/` 目录
2. 双击 `Quantum Design DAT Data Visualization Tool.exe`
3. 开始使用！

### macOS用户
1. 进入 `macOS-x64/` 目录
2. 下载 `install_mac.sh` 安装脚本
3. 在终端中运行：`chmod +x install_mac.sh && ./install_mac.sh`
4. 安装完成后，在Applications文件夹中找到并运行应用程序

### Linux用户

#### Ubuntu/Debian用户
1. 进入 `Linux-x64/` 目录
2. 下载 `install_ubuntu.sh` 安装脚本
3. 在终端中运行：`chmod +x install_ubuntu.sh && ./install_ubuntu.sh`
4. 安装完成后，在应用程序菜单中找到程序，或使用命令：`quantum-design-dat-tool`

#### CentOS/RHEL用户
1. 进入 `Linux-x64/` 目录
2. 下载 `install_centos.sh` 安装脚本
3. 在终端中运行：`chmod +x install_centos.sh && ./install_centos.sh`
4. 安装完成后，在应用程序菜单中找到程序，或使用命令：`quantum-design-dat-tool`

## ✨ 主要功能

- **📊 数据可视化**: 支持线图、散点图、组合图
- **🔍 交互式缩放**: 左键框选放大，右键返回
- **🌐 多语言支持**: 中英文界面自动切换
- **🔧 数据筛选**: 智能数据分段检测和筛选
- **📁 文件支持**: 专为Quantum Design设备DAT文件优化

## 📋 系统要求对比

| 平台 | 安装包 | 可执行文件 | Python环境 | 安装难度 | 文件大小 |
|------|--------|------------|------------|----------|----------|
| Windows | .exe | ✅ | ❌ | 简单 | ~46MB |
| macOS | .dmg | ✅ | ❌ | 简单 | ~50MB |
| Linux | .deb/.AppImage | ✅ | ❌ | 简单 | ~50MB |

## 🛠️ 技术说明

- **所有平台**: 使用PyInstaller打包，包含所有依赖
- **即开即用**: 所有平台都提供可执行文件，无需安装Python环境
- **跨平台兼容**: 核心功能在所有平台上保持一致
- **构建脚本**: 提供自动化构建脚本，方便开发者重新打包

## 📞 技术支持

- **项目地址**: https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool
- **联系邮箱**: yuanxiuliang8@outlook.com
- **版权所有者**: 袁秀良

## 📄 许可证

本项目为第三方工具，仅供学习和研究使用。Quantum Design是Quantum Design公司的注册商标。
