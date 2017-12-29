# -*- coding: utf-8 -*-
import scrapy


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']
    start_urls = ['http://capi.douyucdn.cn/']

    def parse(self, response):
        pass
