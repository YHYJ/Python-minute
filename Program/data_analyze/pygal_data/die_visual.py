# -*- coding:utf-8 -*-

import pygal

from die import Die

class RollData(Die):
    """对掷骰子数据进行分析的类"""

    def __init__(self,num_sides=6,number=100):    #骰子默认6面，默认投掷100次
        """继承父类Die,"""
        super().__init__(num_sides)     #继承来自父类的属性
        self.results = []               #子类自己的属性
        self.frequencies = []           #子类自己的属性
        self.number = number            #子类自己的属性

    def roll_die(self):
        """转骰子，默认100次"""
        for roll_num in range(self.number):
            result = self.roll()    #调用父类Die的方法roll()，将返回值赋给result
            self.results.append(result)

    def analyze_result(self):
        """分析结果"""
        for value in range(1,self.num_sides+1):     #遍历骰子的结果
            frequency = self.results.count(value)   #计算每个结果的出现次数
            self.frequencies.append(frequency)
        return self.frequencies


# 对结果进行可视化处理
hist = pygal.Bar()  #创建pygal.Bar()实例
die = RollData(num_sides=16,number=1000)    #创建RollData()实例
die.roll_die()     #调用RollData类的roll_die()方法投掷骰子并记录结果

hist.title = str(die.num_sides) + "面骰子投掷%d次每面出现的频率"%die.number    #图表标题
hist.x_labels = list(range(1,die.num_sides+1))  #x轴坐标为掷D6可能的结果
hist.x_title = "结果"                       #x轴标题
hist.y_title = "每面出现的次数"              #y轴标题

my_data=die.analyze_result()   #调用RollData类的analyze_result()方法对投掷结果进行分析
hist.add('D%d'%die.num_sides,my_data)      #将出现次数的列表添加到图表，并指定标签
hist.render_to_file('die_visual.svg')       #生成文件名