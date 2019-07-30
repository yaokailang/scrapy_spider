# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MaoyanfilmItem

class MaoyanSpider(CrawlSpider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4/']

    rules = (
        Rule(LinkExtractor(allow=r'.+?offset=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.+/films/\d+'),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        title=response.xpath('/html/body/div[3]/div/div[2]/div[1]/h3/text()').get()
        type=response.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/text()').get()
        release_date=response.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()').get()
        time=response.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()').get()
        plot=response.xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/span/text()').get()
        item=MaoyanfilmItem(title=title,type=type,release_date=release_date,time=time,plot=plot)
        yield item