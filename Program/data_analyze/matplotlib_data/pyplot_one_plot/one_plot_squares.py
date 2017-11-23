# -*- coding: utf-8 -*-

"""绘制一个简单的折线图，再对其进行定制，以实现信息更丰富的数据可视化"""

import matplotlib.pyplot as plt   #导入模块pyplot，包含很多用于生成图表的函数

input_values = [1,2,3,4,5]  #输入列表
squares = [1,4,9,16,25]     #输出列表

# 函数plot()根据两个列表的数字绘制有意义的图形
plt.plot(input_values,squares,linewidth=3)   #线条粗细

# 设置图标标题，并给坐标轴加上标签
plt.title("square numbers".title(),fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='y',labelsize=14)   #both、x或y轴

plt.savefig('one_plot_squares.png',bbox_inches='tight')
#plt.show()  #打开matplotlib查看器，并显示绘制的图形