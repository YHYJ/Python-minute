#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""单进程访问2次网页用时"""

import requests, time

start_time=time.time()

[requests.get('https://www.liaoxuefeng.com/') for x in range(2)]

print("用时：{}秒".format(time.time()-start_time))
# 0.7s
