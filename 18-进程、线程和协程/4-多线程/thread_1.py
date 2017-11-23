#!/home/yj/.virtualenvs/py3.6.2/bin/python
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-13 20:39:26
Last modified: 2017-09-13 20:39:26
Python release: 3.6.2

线程执行顺序
"""


import threading, time

def sing():
    for i in range(3):
        print("子进程 %s >>> %s" % (threading.current_thread().name, i))
        print("%d 正在唱歌..." % i)
        time.sleep(1)


def dance():
    for i in range(3):
        print("子进程 %s >>> %s" % (threading.current_thread().name, i))
        print("%d 正在跳舞..." % i)
        time.sleep(1)


if __name__ == '__main__':
    print("主进程 %s 开始" % threading.current_thread().name)
    t1 = threading.Thread(target=sing, name='SingThread')
    t2 = threading.Thread(target=dance, name='DanceThread')

    t1.start()
    t1.join()
    t2.start()
    t2.join()

    print("主进程 %s 结束" % threading.current_thread().name)
