# Quantum Design DAT Data Visualization Tool

[![Language](https://img.shields.io/badge/Language-Chinese%20%7C%20English-blue)](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS-green)](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool/releases)
[![Version](https://img.shields.io/badge/Version-2.0.0-orange)](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool)

专为Quantum Design设备设计的数据可视化工具，支持PPMS、MPMS等设备的DAT文件格式。

## 📦 下载安装

### Windows版本
- **状态**: 🚧 开发中（Wine兼容性问题）
- **替代方案**: 使用Python源码运行：`python "Quantum Design DAT Data Visualization Tool.py"`
- **大小**: 预计44MB
- **系统要求**: Windows 7/8/10/11 (64位)
- **安装方式**: 双击运行，无需安装Python环境

### macOS版本
- **下载**: [Quantum_Design_DAT_Tool_macOS.dmg](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool/releases/latest/download/Quantum_Design_DAT_Tool_macOS.dmg)
- **大小**: 40MB
- **系统要求**: macOS 10.14+ (支持Intel和Apple Silicon)
- **安装方式**: 
  1. 双击DMG文件挂载
  2. 将应用程序拖拽到Applications文件夹
  3. 从Launchpad启动应用
  4. 如遇安全提示，右键应用 → "打开"

## 🚀 快速开始

1. **下载对应平台的安装包**
2. **安装并启动应用程序**
3. **点击"打开.dat"选择数据文件**
4. **自动智能识别数据类型并设置默认参数**
5. **使用筛选功能分析特定条件下的数据段**

## 🎯 核心功能

### 📊 智能数据识别
- **自动检测**: 比热、磁学、电阻等数据类型
- **智能默认**: 根据数据类型自动设置X/Y轴和筛选列
- **参数优化**: 自动配置容差和连续行数

### 🖱️ 高级选择功能
- **普通点击**: 选择单个数据段
- **Shift+点击**: 范围选择（从起始行到当前行）
- **Ctrl+点击**: 累积选择（添加/移除数据段）
- **智能标签**: 显示筛选条件（如"磁场 = 1000"）

### 📈 可视化功能
- **多种图表**: 折线图、散点图、组合图
- **叠加显示**: 支持多个数据段同时对比
- **轴标签保持**: 选择切换时保持横纵轴标题
- **优化字体**: 7-8pt紧凑字体设计

### 🔍 数据筛选
- **智能筛选**: 根据数据类型选择合适的筛选列
- **自适应参数**: 磁场列容差50/连续20行，温度列容差0.2/连续10行
- **实时预览**: 筛选结果实时显示在图表中

## 📋 支持的数据类型

| 数据类型 | X轴 | Y轴 | 筛选列 | 应用场景 |
|---------|-----|-----|--------|----------|
| 比热 | 温度 | 比热值 | 磁场 | 磁场对比热的影响 |
| 磁学 | 磁场 | 磁化强度 | 温度 | 温度对磁化曲线的影响 |
| 电阻 | 温度/时间 | 电阻值 | 磁场 | 磁场对电阻的影响 |

## 🛠️ 开发环境

### 系统要求
- **Python**: 3.12.0
- **依赖库**: pandas, numpy, matplotlib, tkinter
- **开发平台**: macOS, Windows, Linux

### 构建安装包
```bash
# 统一构建脚本（推荐）
cd Releases/build
./build_all.sh

# 手动构建（如需要）
# macOS: 使用Releases/build/build_all.sh
# Windows: 使用Wine在macOS上构建
```

### 环境配置
```bash
# Python环境
pyenv install 3.12.0
pyenv global 3.12.0

# 依赖安装
pip install -r requirements.txt

# macOS额外依赖
brew install create-dmg
brew install --cask wine-stable  # Windows交叉编译
```

## 📁 项目结构

```
Quantum-Design-DAT-Data-Visualization-Tool/
├── Quantum Design DAT Data Visualization Tool.py  # 主程序文件
├── README.md                                       # 项目说明
├── requirements.txt                                # Python依赖
├── Releases/                                       # 发布文件
│   ├── Quantum_Design_DAT_Tool_macOS.dmg          # macOS安装包
│   └── build/                                      # 构建脚本
│       ├── build_all.sh                           # 统一构建脚本
│       └── BUILD.md                               # 构建说明
├── .git/                                          # Git版本控制
└── .github/                                       # GitHub配置
```

## 🎨 界面特色

### 多语言支持
- **自动检测**: 系统语言自动切换中英文界面
- **完整翻译**: 所有界面元素和提示信息

### 用户友好设计
- **紧凑布局**: 20%控制面板 + 80%图表区域
- **智能默认**: 减少用户手动配置
- **实时反馈**: 操作状态实时显示

### 高DPI支持
- **自适应缩放**: 支持高分辨率显示器
- **字体优化**: 轴标题8pt，轴标签7pt，图例7pt

## 🔧 技术特点

### 性能优化
- **内存管理**: 大文件分块加载
- **渲染优化**: matplotlib高效绘图
- **响应式UI**: 非阻塞界面操作

### 兼容性
- **文件格式**: 支持所有Quantum Design DAT格式
- **编码支持**: 自动检测文件编码
- **版本兼容**: 向下兼容旧版本数据

### 错误处理
- **友好提示**: 详细的错误信息和建议
- **容错机制**: 异常数据自动跳过
- **日志记录**: 操作日志便于调试

## 📞 支持与反馈

### 问题报告
- **GitHub Issues**: [提交问题](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool/issues)
- **功能建议**: 欢迎提出改进建议

### 更新日志
- **v2.0.0**: 智能选择系统、筛选标签、字体优化
- **v1.5.0**: 多语言支持、高DPI适配
- **v1.0.0**: 基础数据可视化功能

## 📄 许可证

本项目采用 MIT 许可证，详见 [LICENSE](https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool/blob/main/LICENSE) 文件。

## 🙏 致谢

感谢 Quantum Design 公司提供的设备数据格式文档，以及所有贡献者的反馈和建议。

---

**开发团队**: [yuanxiuliang](https://github.com/yuanxiuliang)  
**最后更新**: 2025年11月23日  
**项目状态**: ✅ 生产就绪
