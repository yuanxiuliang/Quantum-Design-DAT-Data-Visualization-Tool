# Quantum Design DAT Data Visualization Tool - macOS x64

## 系统要求
- macOS 10.14 或更高版本
- 无需安装Python环境（可执行文件版本）

## 使用方法

### 方法1：一键安装（推荐）
1. 下载 `install_mac.sh` 安装脚本
2. 在终端中运行：
```bash
chmod +x install_mac.sh
./install_mac.sh
```
3. 安装完成后，在Applications文件夹中找到并运行应用程序

### 方法2：使用可执行文件
1. 下载 `Quantum Design DAT Data Visualization Tool` 可执行文件
2. 在终端中运行：
```bash
chmod +x "Quantum Design DAT Data Visualization Tool"
./"Quantum Design DAT Data Visualization Tool"
```

### 方法3：从源代码构建
如果您想自己构建可执行文件：
```bash
# 1. 克隆仓库
git clone https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool.git
cd Quantum-Design-DAT-Data-Visualization-Tool

# 2. 运行构建脚本
cd Releases/macOS-x64
chmod +x build_mac.sh
./build_mac.sh
```

### 方法4：使用Python运行（开发模式）
```bash
# 1. 安装Python依赖
pip3 install pandas numpy matplotlib

# 2. 运行程序
python3 "Quantum Design DAT Data Visualization Tool.py"
```

## 使用方法
1. 启动程序后，点击 "打开 .dat" 按钮选择Quantum Design设备生成的DAT文件
2. 选择X轴和Y轴数据列
3. 根据需要设置数据筛选条件
4. 选择绘图类型（线图/散点图/组合图）
5. 程序会自动绘制数据图表

## 功能特点
- 支持Quantum Design设备（如PPMS）的DAT文件格式
- 交互式缩放：左键框选放大，右键返回上一级
- 中英文界面自动切换
- 数据筛选和分段检测
- 多种绘图类型支持

## 注意事项
- 确保已安装Python 3.8或更高版本
- 首次运行需要安装依赖包
- 如遇到权限问题，可能需要授予终端完全磁盘访问权限

## 技术支持
- 项目地址: https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool
- 联系邮箱: yuanxiuliang8@outlook.com
- 版权所有者: 袁秀良

## 版本信息
- 版本: 1.0.0
- 构建日期: 2025年10月26日
