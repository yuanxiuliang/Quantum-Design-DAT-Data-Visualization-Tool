# Quantum Design DAT Data Visualization Tool - Linux x64

## 系统要求
- Ubuntu 18.04+ / CentOS 7+ / Debian 10+ 或其他主流Linux发行版
- 无需安装Python环境（可执行文件版本）

## 使用方法

### 方法1：一键安装（推荐）

#### Ubuntu/Debian系统
1. 下载 `install_ubuntu.sh` 安装脚本
2. 在终端中运行：
```bash
chmod +x install_ubuntu.sh
./install_ubuntu.sh
```
3. 安装完成后，在应用程序菜单中找到程序，或使用命令：`quantum-design-dat-tool`

#### CentOS/RHEL系统
1. 下载 `install_centos.sh` 安装脚本
2. 在终端中运行：
```bash
chmod +x install_centos.sh
./install_centos.sh
```
3. 安装完成后，在应用程序菜单中找到程序，或使用命令：`quantum-design-dat-tool`

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
cd Releases/Linux-x64
chmod +x build_linux.sh
./build_linux.sh
```

### 方法4：使用Python运行（开发模式）

#### Ubuntu/Debian系统
```bash
# 1. 更新包管理器
sudo apt update

# 2. 安装Python和依赖
sudo apt install python3 python3-pip python3-tk

# 3. 安装Python包
pip3 install pandas numpy matplotlib

# 4. 运行程序
python3 "Quantum Design DAT Data Visualization Tool.py"
```

#### CentOS/RHEL系统
```bash
# 1. 安装Python和依赖
sudo yum install python3 python3-pip tkinter

# 2. 安装Python包
pip3 install pandas numpy matplotlib

# 3. 运行程序
python3 "Quantum Design DAT Data Visualization Tool.py"
```

#### 使用conda环境
```bash
# 1. 创建conda环境
conda create -n qd-tool python=3.9

# 2. 激活环境
conda activate qd-tool

# 3. 安装依赖
conda install pandas numpy matplotlib tk

# 4. 运行程序
python "Quantum Design DAT Data Visualization Tool.py"
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

## 故障排除
- 如果遇到tkinter相关错误，请安装：`sudo apt install python3-tk`
- 如果matplotlib显示问题，请安装：`sudo apt install python3-matplotlib`
- 如果权限问题，请确保文件有执行权限：`chmod +x "Quantum Design DAT Data Visualization Tool.py"`

## 技术支持
- 项目地址: https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool
- 联系邮箱: yuanxiuliang8@outlook.com
- 版权所有者: 袁秀良

## 版本信息
- 版本: 1.0.0
- 构建日期: 2025年10月26日
