# Quantum Design DAT Data Visualization Tool (Third-Party)
# Quantum Design DAT 数据可视化工具（第三方）

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Language](https://img.shields.io/badge/Language-Chinese%20%7C%20English-red.svg)](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool)

A third-party data visualization and analysis tool designed for Quantum Design device data files, particularly PPMS (Physical Property Measurement System) .dat files, featuring interactive zooming, data filtering, and intelligent segment detection capabilities.

专为Quantum Design设备数据文件设计的第三方绘图和分析工具，特别针对PPMS（Physical Property Measurement System）.dat文件，支持交互式缩放、数据筛选和智能段检测功能。

**Disclaimer / 免责声明**: This is an independent third-party project and is not affiliated with, endorsed by, or sponsored by Quantum Design. Quantum Design and PPMS are trademarks of Quantum Design, Inc.

**免责声明**: 这是一个独立的第三方项目，与Quantum Design公司无任何关联，未经其认可或赞助。Quantum Design和PPMS是Quantum Design公司的商标。

---

## 🚀 Features / 功能特性

### 📊 Data Visualization / 数据可视化
- **Multiple Plot Types / 多种绘图类型**: Support line plots, scatter plots, or both combined / 支持折线图、散点图或两者结合
- **Interactive Zooming / 交互式缩放**: Left-click to select and zoom in, right-click to zoom back / 左击框选放大，右击回退缩放
- **High DPI Support / 高DPI支持**: Perfect adaptation to high-resolution displays / 完美适配高分辨率显示器
- **Real-time Plotting / 实时绘图**: Automatic redraw when selecting plot types / 选择绘图类型时自动重绘

### 🔍 Intelligent Data Analysis / 智能数据分析
- **Segment Detection Algorithm / 段检测算法**: Automatically identify continuous segments with approximately constant values / 自动识别数据中约为恒定值的连续段
- **Flexible Filtering / 灵活筛选**: Support both absolute and relative tolerance detection modes / 支持绝对容差和相对容差两种检测模式
- **Segment Overlay Display / 段叠加显示**: Support up to 8 detection segments overlay / 支持最多8个检测段的叠加显示
- **Segment Sorting / 段排序**: Sort detection results by different columns / 支持按不同列对检测结果排序

### 🎯 Professional Features / 专业功能
- **Timestamp Conversion / 时间戳转换**: Automatically convert timestamps to readable time format / 自动将时间戳转换为可读时间格式
- **Data Range Selection / 数据范围选择**: Flexible selection of data range for plotting / 灵活选择绘图的数据范围
- **Axis Selection / 坐标轴选择**: Free selection of X/Y axis corresponding data columns / 自由选择X/Y坐标轴对应的数据列
- **Status Monitoring / 状态监控**: Real-time display of operation status and data information / 实时显示操作状态和数据信息

---

## 📋 System Requirements / 系统要求

### Required Dependencies / 必需依赖
- Python 3.7+
- tkinter (usually included with Python)
- matplotlib
- pandas
- numpy

### Installation / 安装依赖
```bash
pip install matplotlib pandas numpy
```

---

## 🛠️ Installation and Usage / 安装和使用

### Quick Start / 快速开始
1. Ensure Python 3.7+ is installed / 确保已安装Python 3.7或更高版本
2. Install required dependencies / 安装所需依赖包
3. Run the program / 运行程序:
```bash
python "Quantum Design DAT Data Visualization Tool.py"
```

### Usage Workflow / 使用流程

#### 1. Load Data / 加载数据
- Click "Open .dat" button / 点击"打开 .dat"按钮
- Select Quantum Design device .dat file (e.g., PPMS) / 选择Quantum Design设备.dat文件（如PPMS）
- Program automatically parses file header and data / 程序自动解析文件头部和数据

#### 2. Select Coordinates / 选择坐标
- Choose X-axis data column from dropdown / 从下拉框选择X轴数据列
- Choose Y-axis data column from dropdown / 从下拉框选择Y轴数据列
- Plot automatically updates / 绘图自动更新

#### 3. Interactive Analysis / 交互式分析
- **Box Selection Zoom / 框选放大**: Left-click and drag in plot area to select region / 在绘图区域左击并拖拽选择感兴趣的区域
- **Zoom Back / 回退缩放**: Right-click plot area to return to previous view / 右击绘图区域回到上一级视图
- **Segment Detection / 段检测**: Use filtering function to automatically identify stable segments / 使用筛选功能自动识别数据中的稳定段

---

## 🎮 Operation Guide / 操作指南

### Mouse Operations / 鼠标操作
| Operation / 操作 | Function / 功能 |
|------------------|-----------------|
| Left-click drag / 左击拖拽 | Box select region for zooming / 框选区域进行放大 |
| Right-click / 右击 | Return to previous zoom view / 回退到上一级缩放视图 |
| Mouse wheel / 滚轮 | Zoom (if supported) / 缩放（如果支持） |

### Interface Layout / 界面布局
```
┌─────────────────────────────────────────────────────────┐
│ Toolbar: [Open .dat] / 工具栏: [打开 .dat]                │
├─────────────────┬───────────────────────────────────────┤
│ Left Control Panel / 左侧控制面板    │ Right Plot Area / 右侧绘图区域    │
│                 │                                       │
│ File Information / 文件信息        │  ┌─────────────────────────────────┐   │
│ - File Path / 文件路径      │  │                                 │   │
│ - Data Points / 数据点数      │  │    Interactive Plot Area /    │   │
│                 │  │    交互式绘图区域           │   │
│ Coordinate Selection / 坐标选择        │  │                                 │   │
│ - X-axis Selection / X轴选择       │  │                                 │   │
│ - Y-axis Selection / Y轴选择       │  │                                 │   │
│                 │  └─────────────────────────────────┘   │
│ Data Filtering / 数据筛选        │                                       │
│ - Filter Column / 筛选列        │                                       │
│ - Tolerance Settings / 容差设置      │                                       │
│ - Filter Button / 检测按钮      │                                       │
│ - Segment List / 段列表        │                                       │
│                 │                                       │
│ Plot Control / 绘图控制        │                                       │
│ - Start/End Rows / 起始/终止行   │                                       │
│ - Plot Types / 绘图类型      │                                       │
└─────────────────┴───────────────────────────────────────┘
│ Status Bar: Display current operation status and data info / 状态栏: 显示当前操作状态和数据信息                        │
└─────────────────────────────────────────────────────────┘
```

---

## 🔬 Advanced Features / 高级功能

### Segment Detection Algorithm / 段检测算法
The program uses intelligent algorithms to detect continuous segments with approximately constant values in data:

程序使用智能算法检测数据中约为恒定值的连续段：

1. **Tolerance Setting / 容差设置**: Set detection tolerance range / 设置检测的容差范围
2. **Minimum Length / 最小长度**: Set minimum continuous rows for segments / 设置段的最小连续行数
3. **Detection Modes / 检测模式**:
   - Absolute tolerance / 绝对容差: Based on absolute numerical differences / 基于数值的绝对差异
   - Relative tolerance / 相对容差: Based on relative percentage of values / 基于数值的相对百分比

### Segment Management / 段管理
- **Segment List / 段列表**: Display all detected segments and their statistics / 显示所有检测到的段及其统计信息
- **Segment Operations / 段操作**:
  - Double-click segment / 双击段: Automatically set plot range to that segment / 自动设置绘图范围到该段
  - Left-click segment / 左击段: Replace current plot with that segment / 替换当前绘图为该段
  - Shift+Left-click segment / Shift+左击段: Overlay display that segment (max 8) / 叠加显示该段（最多8个）

### Timestamp Processing / 时间戳处理
- Automatic FILEOPENTIME parsing / 自动解析FILEOPENTIME信息
- Support timestamp to readable time conversion / 支持时间戳到可读时间的转换
- Intelligent handling of different time formats / 智能处理不同时间格式

---

## 📁 Supported File Formats / 支持的文件格式

### Quantum Design Device Files / Quantum Design设备文件
This third-party tool is designed to process data files generated by Quantum Design devices, particularly PPMS systems:

这个第三方工具设计用于处理Quantum Design公司设备生成的数据文件，特别是PPMS系统：

- Automatic [Data] section recognition / 自动识别`[Data]`段
- Parse file header metadata / 解析文件头部元数据
- Handle duplicate column names and empty column names / 处理列名重复和空列名问题
- Support timestamp conversion / 支持时间戳转换

### File Structure Example / 文件结构示例
Example of Quantum Design PPMS .dat file format / Quantum Design PPMS .dat文件格式示例:
```
[Header]
FILEOPENTIME,3862854806.58759,05/27/2022,11:13 pm
[Data]
Time Stamp (sec),Moment (emu),Temperature (K),Field (Oe)
0.0,1.2345,300.0,0.0
0.1,1.2346,300.0,0.0
...
```

---

## 🎨 Interface Features / 界面特性

### High DPI Support / 高DPI支持
- Automatic system DPI detection / 自动检测系统DPI
- Dynamic interface scaling / 动态调整界面缩放
- Optimized font and icon sizes / 优化字体和图标大小

### Responsive Layout / 响应式布局
- Left-right split design / 左右分栏设计
- Adaptive window sizing / 自适应窗口大小
- Compact toolbar layout / 紧凑的工具栏布局

### Status Feedback / 状态反馈
- Real-time status bar display / 实时状态栏显示
- Operation result prompts / 操作结果提示
- Error message display / 错误信息显示

---

## 🔧 Technical Architecture / 技术架构

### Core Technology Stack / 核心技术栈
- **GUI Framework / GUI框架**: Tkinter + ttk
- **Data Processing / 数据处理**: pandas + numpy
- **Visualization / 可视化**: matplotlib
- **File Processing / 文件处理**: Standard library

### Key Classes and Methods / 关键类和方法
- `DatPlotterApp`: Main application class / 主应用程序类
- `open_file()`: File loading and parsing / 文件加载和解析
- `draw_plot()`: Plotting functionality / 绘图功能
- `run_detect()`: Segment detection algorithm / 段检测算法
- `find_candidates()`: Core detection algorithm / 核心检测算法

---

## 🐛 Troubleshooting / 故障排除

### Common Issues / 常见问题

**Q: Program won't start / 程序无法启动**
A: Check if Python version and dependencies are correctly installed / 检查Python版本和依赖包是否正确安装

**Q: Cannot open .dat files / 无法打开.dat文件**
A: Ensure Quantum Design device .dat file format is correct and contains [Data] section / 确保Quantum Design设备.dat文件格式正确，包含`[Data]`段

**Q: Plot display is abnormal / 绘图显示异常**
A: Check if data column selection is correct and data is numeric type / 检查数据列选择是否正确，确保数据为数值类型

**Q: Zoom function doesn't work / 缩放功能不工作**
A: Ensure mouse operations are performed within the plot area / 确保在绘图区域内进行鼠标操作

### Performance Optimization / 性能优化
- Large dataset processing: Program optimized for large data files / 大数据集处理：程序已优化处理大型数据文件
- Memory management: Limit zoom history stack size to prevent memory leaks / 内存管理：限制缩放历史栈大小防止内存泄漏
- Rendering optimization: Use matplotlib's blit technology for animation optimization / 渲染优化：使用matplotlib的blit技术优化动画

---

## 📝 Update Log / 更新日志

### v1.0.0
- Initial version release / 初始版本发布
- Basic plotting functionality / 基础绘图功能
- Interactive zoom functionality / 交互式缩放功能
- Segment detection algorithm / 段检测算法
- High DPI support / 高DPI支持
- Multi-language support (Chinese/English) / 多语言支持（中英文）

---

## 🤝 Contributing / 贡献

Welcome to submit issue reports and feature suggestions! / 欢迎提交问题报告和功能建议！

---

## 📄 License / 许可证

This project is licensed under the MIT License. / 本项目采用MIT许可证。

**Third-Party Project Notice / 第三方项目声明**: This is an independent open-source project created by the community for the scientific research community. It is not an official Quantum Design product or service.

**第三方项目声明**: 这是一个由社区为科研社区创建的独立开源项目。它不是Quantum Design的官方产品或服务。

---

## 📞 Support / 支持

For questions or suggestions, please contact us through: / 如有问题或建议，请通过以下方式联系：

- **Email / 邮件**: yuanxiuliang8@outlook.com
- **Project Repository / 项目仓库**: https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool
- **Submit Issue / 提交Issue**: Use the GitHub Issues feature / 使用GitHub Issues功能
- **Project Discussion / 项目讨论**: GitHub Discussions / GitHub讨论区

**Contact Information / 联系信息**:
- **Developer / 开发者**: Yuan Xiuliang (袁秀良)
- **Email / 邮箱**: yuanxiuliang8@outlook.com
- **Project / 项目**: Quantum Design DAT Data Visualization Tool (Third-Party)

---

**Quantum Design DAT Data Visualization Tool (Third-Party)** - Making scientific data analysis simpler and more efficient! / 让科学数据分析更简单、更高效！