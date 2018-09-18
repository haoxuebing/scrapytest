# -*- coding: utf-8 -*-
import scrapy
from scrapytest.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    # 这里是爬虫名
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath(
            "//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_number'] = i_item.xpath(
                ".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath(
                ".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            content = i_item.xpath(
                ".//div[@class='info']/div[@class='bd']/p[1]/text()").extract_first()
            douban_item['introduce'] = "".join(content.split())
            douban_item['star'] = i_item.xpath(
                ".//div[@class='star']/span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(
                ".//div[@class='star']/span[4]/text()").extract_first()
            douban_item['describe'] = i_item.xpath(
                ".//p[@class='quote']/span/text()").extract_first()
            yield douban_item
        next_link = response.xpath(
            "//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('http://movie.douban.com/top250'+next_link, callback=self.parse)
