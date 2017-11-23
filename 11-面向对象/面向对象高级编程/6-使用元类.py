#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""动态语言和静态语言最大的区别就是函数和类不是编译时定义的，而是运行时动态创建的"""


"""创建hello.py模块，定义一个Hello类
当Py解释器载入hello模块时，就会依次执行该模块的所有语句
执行结果动态创建出一个Hello的class对象"""
# 测试如下：
from hello import Hello
h = Hello()
h.hello()
print(type(Hello))  # Hello是一个类，它的类型就是type
print(type(h))      # h是一个实例，它的类型就是class Hello
'''type()函数可以查看一个类型或变量的类型'''


"""类的定义是运行时使用type()函数动态创建的
type()函数既可以返回一个对象的类型，又可以创建出新的类型"""
# 比如可以通过type()函数创建出Hello类，而无需通过class Hello():的定义：
# 1、先定义一个函数
# 2、再使用type()函数创建一个class对象　——
#     -指定类名Hi（hiya是hh这个实例的类型名）
#     -继承的父类
#     -class的方法名和函数绑定，这里将函数fn绑定到方法名hi
def fn(self, name="world"):     # 先定义函数
    print("Hi,%s." % name)

Hi = type('Hiya', (object,), dict(hi=fn)) # 创建Hello class
hh = Hi()
hh.hi()
print(type(Hi))
print(type(hh))
'''通过type()函数创建的类和直接写class是完全一样的-
    -因为Py解释器遇到class定义时，仅仅是扫描一下class定义的语法-
    -然后调用type()函数创建出class

正常情况下都用class Xxx():来定义类
但type()函数也允许动态创建出类来
也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同
要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现
本质上都是动态编译，会非常复杂'''



print("*"*25,"metaclass —— 元类","*"*25)

"""除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass

metaclass —— 元类，简单的解释就是：
    创建实例前必须先创建类，所以：先创建类，然后创建实例
    创建类前必须先定义metaclass，所以：先定义metaclass，然后创建类
    连起来就是：先定义metaclass，就可以创建类，最后创建实例
所以，只有定义了metaclass才允许创建或者修改类
metaclass是Py面向对象里最难理解，也是最难使用的魔术代码
"""

"""一个简单的例子，元类Listmetaclass可以给自定义的MyList类增加一个add方法"""
# 先定义ListMetaclass，按习惯，元类的类名总是以Metaclass结尾，以便清楚地表示这是一个元类：
class ListMetaclass(type):
    """meatclass是类的模板，所以必须从‘type’类派生"""
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self,value: self.append(value)
        return type.__new__(cls,name,bases,attrs)
    '''__new__()方法接收到的参数依次是：
    cls：当前准备创建的类的对象
    name：类的名字
    bases：类继承的父类的集合
    attrs：类的方法集合
    '''

# 再定义MyList类，定义时指示使用元类ListMetaclass来定制类，传入关键字metaclass
class MyList(list,metaclass=ListMetaclass):
    pass
'''传入关键字metaclass时，魔术生效-
    -它指示Py解释器要通过ListMetaclass.__new__()来创建MyList
'''
L = MyList()    # 测试MyList是否可以调用add()方法
L.add(8)
L.add(12)
print(L)

'''直接在MyList定义中写上add()方法更简单
但总会遇到需要通过metaclass修改类定义的，ORM就是一个典型的例子 ——
    ORM全称“Object Relational Mapping”，即对象-关系映射-
    -就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表-
    -这样，写代码更简单，不用直接操作SQL语句
编写ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来
'''