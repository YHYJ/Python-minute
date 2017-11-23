# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

"""再绘制一个图形，显示前 5000 个整数的立方值"""
x_value = list(range(1,5001))
y_value = [x for x in x_value]

plt.figure(figsize=(19.2,10.8))

plt.scatter(x_value,y_value,
            edgecolors='none',c=y_value,cmap=plt.cm.Reds,s=15)

plt.title("number³",size=20)
plt.xlabel("num",fontsize=16)
plt.ylabel("num³",fontsize=16)

plt.axis([0,5000,0,125000000000])

plt.savefig("two_work_1——前5000数字的立方.jpg",bbox_inches='tight')
#plt.show()