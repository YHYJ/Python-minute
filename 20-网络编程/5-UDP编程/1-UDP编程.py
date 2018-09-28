#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""UDP面向无连接的协议
使用UDP协议时不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包
但能不能到达就不知道了
虽然用UDP传输数据不可靠，但它的优点是比TCP速度快
对于不要求可靠到达的数据，就可以使用UDP协议"""


'''
UDP的使用与TCP类似，但是不需要建立连接
此外，服务器绑定UDP端口和TCP端口互不冲突
也就是说，UDP的9999端口与TCP的9999端口可以各自绑定
'''