# -*- coding: utf-8 -*-
import scrapy

from movieProject.items import MovieprojectItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        #找到所有电影
        table_list = response.xpath('//table[@class="tbspan"]')
        for table in table_list:
            #创建对象
            item = MovieprojectItem()
            item['name'] = table.xpath('.//a[@class="ulink"]').extract_first()
            item['movie_info'] = table.xpath('.//tr[last()]/td/text()').extract_first()
            #获取电影详细信息页面链接
            movie_url = 'http://www.ygdy8.net'+ table.xpath('.//.//a[@class="ulink"]/@href').extract_first()

            yield scrapy.Request(url=movie_url, callback=self.next_page, meta={'item': item})
    # 获取item其他信息
    def next_page(self, response):
        item = response.meta['item']
        item['img_url'] = response.xpath('//div[@id="Zoom"]//p/img[1]/@src').extract_first()
        item['download_url'] = response.xpath('//div[@id="Zoom"]//td[1]/a/text()').extract_first()
