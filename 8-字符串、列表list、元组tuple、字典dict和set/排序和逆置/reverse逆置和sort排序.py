#!/home/yj/.virtualenvs/py3.6.2/bin/python
# -*- coding: utf-8 -*-

"""字典排序"""
"""
标准序: 短在前,长在后,等长的依次比字母,
    如to < up < cap < cat < too < two <boat < boot < card
字典序: 依次比字母,
    如boat < boot <cap < card < cat < to < too< two < up
"""


'''可变对象（字典、列表）的方法，在 原容器 内排序，无参数，无返回值'''
# 1.sort()——字典序、标准序排序，列表提供的排序函数
L = ['dream', 'a', 'have', 'I']
L.sort()
print(L)
'''默认从小到大排序，参数reverse=True修改为从大到小'''
'''修改原列表，不生成新列表'''

print('-' * 40)

'''对象通用，需要一个参数（字典、列表、元组、字符串），
无论传递什么参数，都将返回一个列表，如果参数是字典将返回键的列表'''
# 1.sorted()——字典序、标准序排序，Py提供的排序函数
mystring = 'FCAamd1436'  # 字符串
mytuple = ('F', 'C', 'A', 'a', 'm', 'd', '1', '4', '3', '6')  # 元组
mylist = ['F', 'C', 'A', 'a', 'm', 'd', '1', '4', '3', '6']  # 列表
print(sorted(mystring))
print(sorted(mytuple))
print(sorted(mylist))
'''不修改原列表，返回排序后的列表副本'''

print('-' * 40)


# 2.reverse()——逆置
mylist = [16, 'dream', 'a', 'have', 'I', 15]
mylist.reverse()
print(mylist)

print('*' * 40)

# 2.reversed()——逆置
print(list(reversed(['dream', 'a', 'have', 'I'])))
L = ['dream', 'a', 'have', 'I']
L.reverse()
print(L)
print(L.__reversed__())

print('*'*40)


# 通过序列的切片也可以进行逆置
mystring = "53124"
mytuple = (5, 3, 1, 4, 6)
mylist = [5, 3, 1, 4, 6]
print(mystring[::-1])
print(mytuple[::-1])
print(mylist[::-1])
