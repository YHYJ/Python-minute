# -*- coding: utf-8 -*-


import random

import requests

from conf.User_Agent_list import USER_AGENT_LIST


class Spider:
    """爬虫类"""
    def __init__(self, url, de_code, en_code="utf-8"):
        """
        :param url: 要抓取的URL
        :param de_code: 网页原始编码
        :param en_code: 转换编码
        """
        self.url = url
        self.de_code = de_code
        self.en_code = en_code
        self.user_agent = random.choice(USER_AGENT_LIST)
        self.headers = {"USer-Agent": self.user_agent}

    def load_page(self):
        """
        爬虫主体
        :return:
        """
        response = requests.get(self.url, headers=self.headers)
        return response.content.decode(self.de_code).encode(self.en_code)
