# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class TuSpider(scrapy.Spider):
    name = 'souhu'
    # start_urls = ['http://www.itcast.cn/']
    start_urls = ("https://book.douban.com/",)

    def parse(self, response):
        items = []
        for each in response.xpath("//div[@class='slide-list']/ul[@class='list-col list-col5 list-express slide-item'][1]/li/div[@class='info']"):
            item = TutorialItem()
            name = each.xpath("div[@class='author']/text()").extract()
            title = each.xpath("div[@class='title']/a/text()").extract()
            item['title'] = title[0]
            item['name'] = name[0]
            items.append(item)

        return items

