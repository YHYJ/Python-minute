# -*- coding: utf-8 -*-

import random
import urllib
import urllib2

from Python2.conf.User_Agent_list import USER_AGENT_LIST


def bdtb_spider(kw, a_page, z_page):
    """
    抓取百度贴吧
    :param kw: 抓取关键词
    :param a_page: 起始页
    :param z_page: 结束页
    :return:
    """
    url = "http://tieba.baidu.com/f"




file_name = "/home/yj/Documents/Project/Python/Python-minute/" \
                "24-爬虫/Python2/1-爬虫原理与数据抓取/data/html/" \
                "7_批量_贴吧_“{}”.html".format(wd)



if __name__ == '__main__':
    kw = raw_input("输入关键字：")
    a_page = raw_input("输入起始页(min=0)：")
    z_page = raw_input("输入结束页(step=50)：")
