# -*- coding: utf-8 -*-

"""绘制散点图并设置各个数据点的样式"""

import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,edgecolors='none',s=10,
            c=y_values,cmap=plt.cm.Reds)
'''
#edgecolors=设置数据点轮廓的颜色，'none'为删除数据点轮廓
s设置点的尺寸
c设置颜色，可以是c = 'red'，或者c = (0,0,1)——取值为1以内
cmap告诉pyplot使用哪个颜色映射,c同时设为要使用颜色映射的列表
'''

# 设置标题并给坐标轴添加标签
plt.title("square number".title(),size=24)
plt.xlabel("Value",fontsize=12)
plt.ylabel("Square of Value",fontsize=12)

# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])    #x(0~1100)，y(0~1100000)

# 设置刻度标记字体大小
#plt.tick_params(axis='both',which='major',labelsize=10)

# 保存图标，可在保存完后调用plt.show()查看
plt.savefig("two_scatter_squares.png",bbox_inches='tight')
#plt.show()
'''
第一个实参指定保存的图表的文件名
第二个实参指定将图表多余的空白区域裁剪掉——如果要保留图表周围多余的空白区域可省略
'''