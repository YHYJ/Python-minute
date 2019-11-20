#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""如果要匹配'010-12345'这样的号码：
由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以正则是\d{3}\-\d{3,8}
但仍无法匹配'010 - 12345'，因为带有空格
所以需要更复杂的匹配方式"""


# 要做更精确地匹配，可以用[]表示范围，比如：
'''
[0-9a-zA-Z\_]   ——
——可以匹配一个数字、字母或者下划线；

[0-9a-zA-Z\_]+  ——
——可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等

[a-zA-Z\_][0-9a-zA-Z\_]*    ——
——可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量

[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}  ——
——更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）

A|B     可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'

^       表示行的开头，^\d表示必须以数字开头

$       表示行的结束，\d$表示必须以数字结束

py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了
'''

# 匹配手机号————[]
'''
表示数字：[0-9] 或者 \d
#任意长度：[0-9]* 或者 \d*
'''

# 注意：*表示任意长度，包括零，也就是没有数字的空字符也会被匹配出来，所以要用 +

# 匹配任意长度的所有数字串：[0-9]+ 或者 \d+

# 限定匹配的串的长度为11：[0-9]{11} 或者 \d{11}

# 限定第一位为1：1[0-9]{10} 或者 1\d{10}


'''练习，在一堆数字中抓出手机号码'''
import re
num = "18765426009 15166694202 13953299413 122916939006 "

m = re.findall(r"\b1[0-9]{10}\b", num)
print(m)
