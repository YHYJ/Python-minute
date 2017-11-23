#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""程序总会有各种各样的bug需要修正
有的bug很简单，看看错误信息就知道
有的bug很复杂，需要知道出错时哪些变量的值是正确的，哪些变量的值是错误的
因此，需要一整套调试程序的手段来修复bug
"""

"""第一种方法简单直接粗暴有效"""
# 用print()把可能有问题的变量打印出来看看：
def foo(s):
    n = int(s)
    print(">>> n = %d" % n)
    return 10 / n

def main():
    foo('0')

main()
'''用print()最大的坏处是将来还得删掉它，于是有了其他方法'''