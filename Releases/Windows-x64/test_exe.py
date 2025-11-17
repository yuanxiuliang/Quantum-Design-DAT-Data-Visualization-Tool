#!/usr/bin/env python3
"""
测试打包的exe文件是否正常工作
"""

import subprocess
import os
import time
import sys

def test_exe():
    """测试exe文件"""
    exe_path = "Quantum Design DAT Data Visualization Tool.exe"
    
    if not os.path.exists(exe_path):
        print("错误：找不到exe文件")
        return False
    
    # 检查文件大小
    file_size = os.path.getsize(exe_path)
    size_mb = file_size / (1024 * 1024)
    print(f"exe文件大小: {size_mb:.1f} MB")
    
    # 尝试启动程序（非阻塞）
    try:
        print("正在启动程序...")
        process = subprocess.Popen([exe_path], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE,
                                 creationflags=subprocess.CREATE_NEW_CONSOLE)
        
        # 等待一小段时间看程序是否能正常启动
        time.sleep(3)
        
        # 检查进程是否还在运行
        poll = process.poll()
        if poll is None:
            print("程序成功启动，GUI界面应该已经打开")
            print("请手动测试以下功能：")
            print("   1. 界面是否正常显示")
            print("   2. 是否能打开.dat文件")
            print("   3. 是否能正常绘图")
            
            # 终止测试进程
            try:
                process.terminate()
                process.wait(timeout=5)
                print("测试完成，已关闭程序")
            except:
                print("程序可能仍在运行，请手动关闭")
            
            return True
        else:
            stdout, stderr = process.communicate()
            print(f"程序启动失败，退出码: {poll}")
            if stderr:
                print(f"错误信息: {stderr.decode('utf-8', errors='ignore')}")
            return False
            
    except Exception as e:
        print(f"启动程序时出错: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Quantum Design DAT 可视化工具 - exe测试")
    print("=" * 50)
    
    success = test_exe()
    
    print("\n" + "=" * 50)
    if success:
        print("打包成功！exe文件可以正常运行")
        print("文件位置:", os.path.abspath("Quantum Design DAT Data Visualization Tool.exe"))
    else:
        print("打包可能存在问题，请检查错误信息")
    print("=" * 50)
