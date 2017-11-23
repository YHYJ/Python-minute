#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""编写函数时,可为其编写测试.

通过测试,可确定代码面对各种输入都能够按要求的那样工作.
使用Py模块unittest中的工具来测试代码,编写测试用例.
"""

print("*"*25 + "单元测试和测试用例" + "*"*25)
"""Py标准库中的 unittest 模块提供了代码测试工具"""
"""
【单元测试】——
    用于核实函数的一个方面没有问题的一个方法,只测试一种情况
【测试用例】——
    一组【单元测试】，这些单元测试一起核实函数在各种情形下的行为都符合要求
【全覆盖式测试用例】——
    包含一整套单元测试,涵盖了各种可能的函数使用方式
对于大型项目要实现全覆盖可能很难
通常最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖
"""


print("*"*25 + "可通过的测试" + "*"*25)
# 创建一个测试用函数 ——> name_function_1.py ——> get_formatted_name()
# 创建一个只包含一个方法的测试用例 ——> test_name_function_1.py


print("*"*25 + "未通过的测试" + "*"*25)
# 能处理中间名但不能处理不包含中间名的名字 ——> name_function_2.py ——> get_formatted_name()
# 创建一个只包含一个方法的新测试用例 ——> test_name_function_2.py


print("*"*25 + "添加新测试" + "*"*25)
# 添加新单元测试：在NamesTestCase类中再添加一个方法，用于测试包含中间名的姓名
# 添加新单元测试test_first_last_middle_name() ——> test_name_function_2.py


print("*"*25 + "work" + "*"*25)
# ——> city_functions_3.py