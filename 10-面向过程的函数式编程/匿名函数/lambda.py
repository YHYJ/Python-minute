#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""Python对匿名函数提供了有限支持

传入函数时，有些时候不需要显式地定义函数，直接传入匿名函数更方便
"""
''''以map()函数为例，计算f(x)=x2'''
# 除了定义一个f(x)的函数外，还可以直接传入匿名函数：
print(list(map(lambda x: x*x,[1,2,3,4,5,6,7,8,9,])))

'''关键字lambda表示匿名函数，冒号前面的x表示函数参数
匿名函数有个限制 —— 
    只能有一个表达式，不用写return
    该表达式的结果就是返回值
'''
'''匿名函数有个好处 —— 因为函数没有名字，不必担心函数名冲突'''


"""匿名函数也是一个函数对象"""
# 可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x*x
print(f)        # 输出显示f的指向类型为lambda函数
print(f(5))     # 调用f变量指向的匿名函数，输出结果25

# 也可以把匿名函数作为返回值返回，比如：
def build(x,y):
    return lambda : x*x + y*y
B = build(3,6)  # 因为build函数的返回值是一个函数（匿名函数），所以B指向一个函数而不是计算的结果
print(B())      # 要获得结果需要调用B

# 小结：Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数