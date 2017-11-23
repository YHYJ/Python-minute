#!/home/yj/.virtualenvs/py3.6.2/bin/python
# -*- coding: utf-8 -*-

age = input("How old are you:")     # 使用函数input()时，默认输入的是字符串类型
print(type(age), age)

'''将输入转换为数值.

'''
ages = input("HOw old are you:")
ages = int(ages)    # int()转换
print(type(ages), ages)


c = eval(input('请输入c的值：'))
d = eval(input('请输入d的值：'))
print('c+d=', c+d)       # 加上 eval 后input获得的是int类型
