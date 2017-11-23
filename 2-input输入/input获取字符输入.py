#!/home/yj/.virtualenvs/py3.6.2/bin/python
# -*- coding: utf-8 -*-

"""input()的工作原理
input()使程序暂停运行等待用户输入，获取输入后存储在一个变量中方便调用.
"""

message = input("复读机： ")     # 提示用户输入的内容
print(message)


prompt = "如果告诉我你是谁，我也不会知道我会干什么。"    # 创建多行字符串
prompt += "\n你叫什么？请输入你的名字：　"
name = input(prompt)
print("Hello," + name)
