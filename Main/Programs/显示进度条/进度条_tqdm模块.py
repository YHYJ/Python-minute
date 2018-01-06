#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""
tqdm是一个快速。扩展性强的进度条工具库，github地址：
https://github.com/tqdm/tqdm
"""
from tqdm import tqdm
from time import sleep

for i in tqdm(range(0,1000)):
    sleep(0.01)