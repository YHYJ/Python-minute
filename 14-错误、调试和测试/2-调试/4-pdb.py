#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""第4种方式是启动Py的调试器pdb，让程序以单步方式运行，可以随时查看运行状态"""

s = '0'
n = int(s)
print(10 / n)

"""
命令行启动：python3 -m pdb 4-pdb.py
"""
# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'

"""
输入命令n可以单步执行代码
"""

"""
任何时候都可以输入命令p 变量名来查看变量
"""

"""
输入命令q结束调试，退出程序
"""