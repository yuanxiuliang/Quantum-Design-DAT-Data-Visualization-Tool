# Quantum Design DAT Data Visualization Tool (Third-Party)

[![Language](https://img.shields.io/badge/Language-Chinese%20%7C%20English-blue)](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-green)](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool/releases)

## 🚀 快速开始 / Quick Start

### 📥 下载安装包 / Download Installer

**当前状态：** 项目正在开发中，安装包即将发布

#### 临时使用方式 / Temporary Usage
由于安装包还在准备中，您可以：

1. **从源码运行**（推荐）
   - 克隆项目到本地
   - 安装Python依赖
   - 直接运行主程序

2. **构建自己的安装包**
   - 使用项目提供的构建脚本
   - 生成适合您系统的可执行文件

#### 即将支持的平台 / Upcoming Platforms
- **Windows**：`.exe` 可执行文件
- **macOS**：`.dmg` 安装包  
- **Linux**：`.deb`、`.rpm`、`.AppImage` 多种格式

### 🎯 5分钟快速上手 / 5-Minute Quick Start

1. **获取源码** - 克隆项目到本地或下载ZIP文件
2. **安装依赖** - 运行 `pip install -r requirements.txt` 安装必要依赖
3. **启动程序** - 运行 `python "Quantum Design DAT Data Visualization Tool.py"`
4. **打开数据文件** - 点击"打开 .dat"按钮，选择您的Quantum Design设备生成的DAT文件
5. **选择数据列** - 在X轴和Y轴下拉菜单中选择要绘制的数据列
6. **开始绘图** - 选择绘图类型（折线图/散点图/组合图），程序会自动绘制
7. **交互操作** - 使用鼠标左键框选放大，右键返回上一级缩放

## ✨ 主要功能 / Key Features

### 🔬 专为Quantum Design设备设计
- **支持PPMS、MPMS等设备** - 完美兼容Quantum Design公司各种设备的DAT文件格式
- **智能数据识别** - 自动识别数据列，无需手动配置
- **科研级精度** - 保持原始数据的完整性和精度

### 📊 强大的数据可视化
- **多种绘图模式** - 折线图、散点图、组合图，满足不同分析需求
- **交互式操作** - 左键框选放大，右键返回，滚轮缩放
- **专业图表** - 支持坐标轴标签、图例、网格线等专业元素

### 🎛️ 智能数据处理
- **自动数据段检测** - 智能识别连续的有效数据段
- **统计筛选** - 基于均值、标准差等统计指标筛选数据
- **异常值处理** - 自动识别和处理异常数据点

### 🌍 多语言支持
- **自动语言检测** - 根据系统语言自动切换中文/英文界面
- **完整本地化** - 所有界面元素都支持多语言

## 📋 系统要求 / System Requirements

| 平台 | 最低版本 | 推荐版本 | 架构 |
|------|----------|----------|------|
| Windows | Windows 10 | Windows 11 | x64 |
| macOS | 10.14 | 12.0+ | Intel/Apple Silicon |
| Linux | Ubuntu 18.04 | Ubuntu 20.04+ | x64 |

## 🛠️ 开发者选项 / Developer Options

如果您需要从源码构建或修改程序：

### 环境准备
```bash
# 克隆项目
git clone https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool.git
cd Quantum-Design-DAT-Data-Visualization-Tool

# 安装Python依赖
pip install -r requirements.txt
```

### 运行程序
```bash
python "Quantum Design DAT Data Visualization Tool.py"
```

### 构建安装包
各平台的构建脚本位于 `Releases/` 目录下：
- Windows: `Releases/Windows-x64/build_windows.bat`
- macOS: `Releases/macOS-x64/build_mac.sh`
- Linux: `Releases/Linux-x64/build_linux.sh`

## 📖 详细使用说明 / Detailed Usage

### 基本工作流程
1. **启动程序** - 运行安装包或从源码启动
2. **加载数据** - 点击"打开 .dat"选择Quantum Design设备数据文件
3. **配置绘图** - 选择X轴和Y轴数据列，选择绘图类型
4. **数据筛选** - 使用筛选功能去除异常数据（可选）
5. **交互分析** - 使用鼠标进行缩放、平移等交互操作

### 高级功能
- **自定义绘图范围** - 指定起始行和终止行
- **数据段统计** - 查看每个数据段的统计信息
- **多文件支持** - 可以同时处理多个数据文件

## 🔧 技术架构 / Technical Architecture

- **开发语言**：Python 3.8+
- **GUI框架**：Tkinter (跨平台原生界面)
- **数据处理**：Pandas + NumPy (高效数据处理)
- **可视化引擎**：Matplotlib (专业级图表)
- **打包工具**：PyInstaller (跨平台可执行文件)

## 📞 支持与反馈 / Support & Feedback

### 获取帮助
- **问题报告**：[GitHub Issues](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool/issues)
- **功能建议**：[GitHub Discussions](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool/discussions)

### 联系方式
- **开发者**：袁秀良
- **邮箱**：yuanxiuliang8@outlook.com
- **项目地址**：https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool

## 📄 许可证 / License

本项目采用MIT许可证。详情请参阅 [LICENSE](LICENSE) 文件。

### 第三方项目声明
本项目为第三方开发工具，与Quantum Design公司无直接关联。使用本工具时请遵守相关数据使用协议和法律法规。

## 🎉 更新日志 / Changelog

### v1.0.0 (2024-01-XX)
- ✨ 初始版本发布
- 🎯 支持Quantum Design DAT文件加载和可视化
- 🖱️ 实现交互式数据探索功能
- 🌍 支持中英文界面自动切换
- 📦 提供Windows/macOS/Linux多平台安装包

---

**Quantum Design DAT Data Visualization Tool (Third-Party)** - 让Quantum Design设备数据可视化变得简单高效！让科研工作更加便捷！