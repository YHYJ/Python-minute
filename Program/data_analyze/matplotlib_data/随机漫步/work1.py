# -*- coding: utf-8 -*-

"""分子运动"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(num_points=5000)
    rw.fill_walk()

    # 设置绘图窗口的大小
    plt.figure(figsize=(19.2,10.8))   #以英寸为单位，100像素/英寸?

    points_num = list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values,
                c='blue',linewidth=12)  #按照点的绘制顺序映射颜色

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)   #plt.axes()函数设置坐标轴可见性
    plt.axes().get_yaxis().set_visible(False)

    plt.savefig("work1.png",bboc_inches='tight')
    #plt.show()

    keep_running = input("继续随机漫步么?(y/n):")
    if keep_running == 'n':
        break