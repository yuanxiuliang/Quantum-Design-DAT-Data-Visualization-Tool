# Quantum Design DAT Data Visualization Tool - Windows x64

## 系统要求
- Windows 7/8/10/11 (64位)
- 无需安装Python或其他依赖

## 使用方法
1. 双击 `Quantum Design DAT Data Visualization Tool.exe` 启动程序
2. 点击 "打开 .dat" 按钮选择Quantum Design设备生成的DAT文件
3. 选择X轴和Y轴数据列
4. 根据需要设置数据筛选条件
5. 选择绘图类型（线图/散点图/组合图）
6. 程序会自动绘制数据图表

## 功能特点
- 支持Quantum Design设备（如PPMS）的DAT文件格式
- 交互式缩放：左键框选放大，右键返回上一级
- 中英文界面自动切换
- 数据筛选和分段检测
- 多种绘图类型支持

## 注意事项
- 确保DAT文件格式正确
- 程序首次启动可能需要几秒钟时间
- 如遇到问题，请检查文件路径中是否包含特殊字符

## 技术支持
- 项目地址: https://github.com/yuanxiuliang/Quantum-Design-DAT-Data-Visualization-Tool
- 联系邮箱: yuanxiuliang8@outlook.com
- 版权所有者: 袁秀良

## 开发者选项

### 重新构建可执行文件
如果您需要重新构建exe文件（例如优化文件大小）：

```cmd
双击运行 build_windows.bat
```

### 优化说明
- 脚本会自动排除不必要的模块（测试文件、scipy、sklearn等）
- 使用 `--strip` 和 `--optimize 2` 参数减少文件大小
- 预期文件大小：25-35MB（相比原来的46MB）

## 版本信息
- 版本: 1.0.0
- 构建日期: 2025年10月26日
- 文件大小: 约46MB（优化后预计25-35MB）
