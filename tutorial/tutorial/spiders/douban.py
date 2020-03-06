# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li") 
        for i_item in movie_list:
        	douban_item = TutorialItem()
        	douban_item['serial_number'] = i_item.xpath(".//div[@class='item']/div[@class='pic']/em/text()").extract_first()
        	douban_item['movie_name'] = i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
        	content = i_item.xpath(".//div[@class='info']/div[@class='bd']/p[1]/text()").extract()
        	for i_content in content:
        		content_s = "".join(i_content.split())
        		douban_item['introduce'] = content_s
        	douban_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
        	douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
        	douban_item['describe'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()
        	yield douban_item
        # 获取下一页内容
        next_link = response.xpath("//div[@class='article']/div[@class='paginator']/a//@href").extract()[1:]
        self.log(next_link)
        if next_link is not None:
            for url in next_link:  
                url = "https://movie.douban.com/top250" + url  
                yield scrapy.Request(url, callback=self.parse)  
            # next_link = next_link[0]
            # yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)
