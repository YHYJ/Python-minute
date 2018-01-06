#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

import sys

while 1:
    try:
        t = int(input('请输入:'))
        p = int(input('请输入:'))
    except EOFError:
        break
    print('相加得：', t + p)
    print('相减得：', t - p)
    print('相乘得：', t * p)
    print('相除得：', t / p)