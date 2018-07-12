# -*- coding: utf-8 -*-
import scrapy


class Xiaohua2Spider(scrapy.Spider):
    name = 'xiaohua2'
    allowed_domains = ['http://www.xiaohuar.com']

    page = 0
    start_urls = ['http://www.xiaohuar.com/list-1-0.html']

    def parse(self, response):
        #解析数据获取所有校花
        pass
