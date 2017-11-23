#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""10进程访问10次网页用时"""

import multiprocessing, time, requests

start_time = time.time()

def run(url):
    r = requests.get(url)

if __name__ == '__main__':
    pool = multiprocessing.Pool(10)
    [pool.apply_async(run,args=('https://www.liaoxuefeng.com/',))
     for x in range(10)]
    pool.close()
    pool.join()
    print("用时：{}秒".format(time.time() - start_time))
# 35s