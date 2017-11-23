#!/home/yj/.virtualenvs/py3.6.2/bin/python
# -*- coding: utf-8 -*-

"""特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符"""


import re

# 举例如下：
'''匹配出数字后面的0'''
vi = re.match(r'^(\d+)(0*)$', '102300').groups()
print(vi)
'''
由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
'''

'''必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来
加个?就可以让\d+采用非贪婪匹配：'''
vi_1 = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(vi_1)


# "*"，表示前面的字符可以重复任意多次（包括0次），表示任意长度但最短为1———— +
text = "I am Shirley Hilton. I am his wife"
m = re.findall(r"I.*e",text)    #.和*搭配 “I.*e” 表示I开头，e结尾，中间任意长度的任意字符，*导致优先匹配最长的字符串，称为贪婪匹配
print(m)    #匹配最长,贪婪匹配
m = re.findall(r"I.*?e",text)   #.*和?搭配，限制优先匹配最短的字符串
print(m)    #匹配最短，懒惰匹配
