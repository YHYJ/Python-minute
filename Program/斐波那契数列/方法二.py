#!/home/yj/.virtualenvs/py3.6.2/bin/python
# -*- coding: utf-8 -*-

def fib(max):
    n,a,b = 0,0,1
    L = []
    while n < max:
        L.append(b)
        a,b = b,a+b
        n += 1
    yield L

for x in fib(12):
    print(x)

'''改写后的fib函数通过返回List能满足复用性的要求，但是.

该函数在运行中占用的内存会随着参数max的增大而增大.
如果要控制内存，最好不要用List来保存中间结果，而是用迭代'''
