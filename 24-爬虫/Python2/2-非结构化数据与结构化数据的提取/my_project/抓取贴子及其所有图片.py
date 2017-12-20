# -*- coding: utf-8 -*-

"""用XPath做一个爬虫，尝试爬取某个贴吧里的所有帖子
并且将该这个帖子里每个楼层发布的图片下载到本地"""

from plugs_two import print_info
from plugs_two.Spider import Spider
from plugs_two.DataTreat import DataTreat
from plugs_two.Save import SaveData