#!/home/yj/.virtualenvs/py3.6.2/bin/python
# -*- coding: utf-8 -*-

"""一个模块是包含python定义和语句的文件，文件名是【模块名.py】.

在模块中，模块的名字（可以作为一个字符串）是一个作为全局变量 _name_ 的值的变量
"""
print("*"*25 + "导入整个fibo模块" + "*"*25)
#
import fibo     #导入整个fibo模块
fibo.fib(10)  #使用fibo模块的 fib() 方法，要加模块名前缀
fibo.fib2(20)  #使用fibo模块的 fib2() 方法，要加模块名前缀
fib = fibo.fib  #在调用模块的方法中，常常把模块里的方法赋一个本地名字
fib(5)


print("*"*25 + "导入特定方法" + "*"*25)
#
from fibo import fib2   #只调用fibo模块的fib2方法
fib2(10)    #不用加模块名前缀


print("*"*25 + "导入模块中所有方法" + "*"*25)
#使用并非自己编写的大型模块时，最好不要采用这种导入方法：
# 如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：
# Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数.
# 最佳的做法是使用上面两个导入方法.
from fibo import *
fib2(93)


print("*"*25 + "使用 as 给方法指定别名" + "*"*25)
#避免与importing_fibo可能包含的函数fibo2()混淆
from fibo import fib2 as f2
f2(15)


print("*"*25 + "使用 as 给模块指定别名" + "*"*25)
#上述import语句给模块fibo指定了别名fb，但该模块中所有方法的名称都没变
import fibo as fb
fb.fib2(31)

print('*'*50,'深入模块','*'*50)
#
"""每个模块都有自己私有的符号表，定义在模块内的所有方法可以把它当做全局符号表来用.

因此模块作者可以在模块中用全局变量而不用担心与用户全局变量的意外冲突.
"""
"""模块中可以导入其他模块.

习惯上把所有的 import 语句放在一个模块的开始位置，但不是强制的.
"""
'''
import fibo    #调用fibo模块
from fibo import fib,fib2   #调用fibo模块的fib，fib2方法。这种方法不会把模块名放在本地符号表中
from fibo import *   #导入fibo模块中以下划线开头之外的所有方法，一般不用，避免引入已定义的方法
'''