# -*- coding:utf-8 -*-

from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self,num_sides=6):
        """骰子默认6面"""
        self.num_sides = num_sides

    def roll(self):
        """摇动骰子，返回一个1～骰子面数之间的随机整数"""
        return randint(1,self.num_sides)