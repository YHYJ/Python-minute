# -*- coding: utf-8 -*-

import csv

file_path = './Data/beijing.csv'
with open(file_path) as f:
    reader = csv.reader(f)  #创建与file_path指向的文件相关联的阅读器（reader）对象
    header_row = next(reader)
    print(header_row)