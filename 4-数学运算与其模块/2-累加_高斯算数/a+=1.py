#!/home/yj/.virtualenvs/py3.6.2/bin/python
# -*- coding: utf-8 -*-

# 任意给定一个最高值num，,求1+2+3+……+num的值
print('请给定一个值，我将计算出从1累加到这个值的得数')

game = True
while game == True:
    max_Num = int(input('请输入任意整数：'))

    num = 1
    ber = 1

    over = False
    while over == False:
        ber += 1
        num += ber

        if ber >= max_Num:
            print('累加得数为：', num)
            over = True
