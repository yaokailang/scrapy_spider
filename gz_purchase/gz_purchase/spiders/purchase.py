# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import GzPurchaseItem
import re

class PurchaseSpider(CrawlSpider):
    name = 'purchase'
    allowed_domains = ['gzzb.gd.cn']
    start_urls = ['http://www.gzzb.gd.cn/cms/wz/view/index/layout2/zfcglist.jsp?page=1&siteId=1&channelId=456']

    rules = (
        Rule(LinkExtractor(allow=r'.+layout2/zfcglist\.jsp\?page=\d+\&siteId=1\&channelId=456'),callback='paser_pageurl',follow=True),
        Rule(LinkExtractor(
            allow=r'.+/layout3/index\.jsp\?siteId=1&infoId=\d+\&channelId=456'),
             callback='parse_detail', follow=False)
    )

    def parse_detail(self, response):
        title = response.xpath('/html/body/div[2]/div[3]/div/div[3]/h1/a/span/text()').get()
        content = response.xpath('/html/body/div[2]/div[3]/div/div[3]//text()').getall()
        turnover = response.xpath('//*[@id="share"]/span[1]/text()').get()
        item = GzPurchaseItem(title=title,content=content,turnover=turnover)
        yield item
