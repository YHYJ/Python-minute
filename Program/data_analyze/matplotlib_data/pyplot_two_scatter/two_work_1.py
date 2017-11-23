# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

"""绘制一个图形，显示前 5 个整数的立方值"""
x_values = [1,2,3,4,5]
y_values = [x**2 for x in x_values]

plt.figure(figsize=(19.2,10.8))

plt.scatter(x_values,y_values,
            edgecolors='red',c=y_values,cmap=plt.cm.Reds,s=15)

plt.title("number³",size=22)
plt.xlabel("num",fontsize=15)
plt.ylabel("num³",fontsize=15)

plt.savefig('two_work_1——数字的立方.jpg',bbox_inches='tight')
#plt.show()