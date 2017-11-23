# -*- coding: utf-8 -*-

"""为做出随机决策，将所有可能的选择都存储在一个列表中，

并在每次做决策时都使用choice()来决定使用哪种选择
"""

from  random import choice

class RandomWalk():
    """一个用来生成随机漫步数据的类"""

    def __init__(self,num_points=5000): #将随机漫步包含的默认点数设置为5000
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]
        self.get_step()

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表达到指定长度
        while len(self.x_values) < self.num_points:

            x_step,y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:   #如果x_step和y_step都为零意味着原地踏步，但拒绝这样的情况，接着执行下一次循环
                continue

            # 计算下一个点的x,y值
            next_x = self.x_values[-1] + x_step   #获取漫步中下一个点的x值，将x_step与x_values中的最后一个值相加
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)    #将它们分别附加到列表x_values和y_values的末尾
            self.y_values.append(next_y)

    def get_step(self):
        """确定每次漫步的距离和方向"""

        # 决定前进方向以及沿这个方向前进的距离
        x_direction = choice([1, -1])  # choice([1, -1])给x_direction选择一个值，要么是表示向右走的1，要么是表示向左走的-1
        x_distance = choice(list(range(0, 9)))  # choice([0, 1, 2, 3, 4])随机选择一个0~4之间的整数决定沿指定的方向走多远
        x_step = x_direction * x_distance  # 移动方向乘以移动距离，确定沿x轴移动的距离

        y_direction = choice([1, -1])
        y_distance = choice(list(range(0, 9)))
        y_step = y_direction * y_distance  # 移动方向乘以移动距离，确定沿y轴移动的距离

        return x_step,y_step