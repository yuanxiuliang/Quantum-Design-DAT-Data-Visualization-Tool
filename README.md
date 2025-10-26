# Quantum Design DAT Data Visualization Tool (Third-Party)

[![Language](https://img.shields.io/badge/Language-Chinese%20%7C%20English-blue)](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-green)](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool/releases)

## 🚀 快速开始 / Quick Start

### 📥 下载安装包 / Download Installer

#### Windows用户 / Windows Users
- **直接下载**：[Quantum Design DAT Data Visualization Tool.exe](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool/raw/master/Releases/Windows-x64/Quantum%20Design%20DAT%20Data%20Visualization%20Tool.exe)
- **安装方式**：直接双击运行，无需安装Python环境
- **系统要求**：Windows 10/11 (64-bit)

#### macOS用户 / macOS Users  
- **安装方式**：从源码构建（详见下方开发者选项）
- **系统要求**：macOS 10.14+ (支持Intel和Apple Silicon)
- **依赖环境**：需要安装Python 3.8+和相关依赖

#### Linux用户 / Linux Users
- **安装方式**：从源码构建（详见下方开发者选项）
- **系统要求**：Ubuntu 18.04+ / CentOS 7+ / 其他主流Linux发行版
- **依赖环境**：需要安装Python 3.8+和相关依赖

**所有版本下载**：[Releases页面](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool/releases)

### 🎯 5分钟快速上手 / 5-Minute Quick Start

#### Windows用户
1. **下载并运行** - 点击上方Windows下载链接，下载exe文件并双击运行
2. **打开数据文件** - 点击"打开 .dat"按钮，选择您的Quantum Design设备生成的DAT文件
3. **选择数据列** - 在X轴和Y轴下拉菜单中选择要绘制的数据列
4. **开始绘图** - 选择绘图类型（折线图/散点图/组合图），程序会自动绘制
5. **交互操作** - 使用鼠标左键框选放大，右键返回上一级缩放

#### macOS/Linux用户
1. **安装依赖** - 按照下方开发者选项安装Python和依赖
2. **运行程序** - 使用 `python "Quantum Design DAT Data Visualization Tool.py"` 启动
3. **后续步骤** - 与Windows用户相同

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
- **Windows**: 运行 `Releases/Windows-x64/build_windows.bat` 生成exe文件
- **macOS**: 运行 `Releases/macOS-x64/build_mac.sh` 生成可执行文件（需要先安装依赖）
- **Linux**: 运行 `Releases/Linux-x64/build_linux.sh` 生成可执行文件（需要先安装依赖）

**注意**: macOS和Linux的构建需要先安装PyInstaller和相关依赖。

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