# -*- coding: utf-8 -*-

"""将随机漫步的所有点都绘制出来"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(num_points=50000)
    rw.fill_walk()

    # 设置绘图窗口的大小
    plt.figure(figsize=(19.2,10.8))   #以英寸为单位，100像素/英寸?

    points_num = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,edgecolors='none',s=3,
                c=points_num,cmap=plt.cm.Blues)  #按照点的绘制顺序映射颜色

    # 突出绘制起始点
    plt.scatter(0,0,edgecolors='none',c='orange',s=26)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],edgecolors='none',
                c='red',s=26)

    # 隐藏坐标轴
    #plt.axes().get_xaxis().set_visible(False)   #plt.axes()函数设置坐标轴可见性
    #plt.axes().get_yaxis().set_visible(False)

    #plt.savefig("随机漫步图表.png",bboc_inches='tight')
    plt.show()

    keep_running = input("继续随机漫步么?(y/n):")
    if keep_running == 'n':
        break