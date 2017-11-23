#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

import zipfile
try:
    with zipfile.ZipFile('1.zip') as zFile:     #创建ZipFile对象
        #解压文件
        zFile.extractall(path='./',pwd=b'1314') #实现暴力破解需要穷举字典
        print('解压完成')
except:
    print('解压失败')