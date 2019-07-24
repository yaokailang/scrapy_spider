# -*- coding: utf-8 -*-
import scrapy
from ..items import MeishijItem
import string

class MeishiSpider(scrapy.Spider):
    name = 'meishi'
    allowed_domains = ['meishij.net/']
    start_urls = ['https://www.meishij.net/chufang/diy/jiangchangcaipu/?&page=1']
    qq=1

    def parse(self, response):
        div_div=response.xpath('//*[@id="listtyle1_list"]').extract()
        for div in div_div:
            dish_name = response.xpath('//div[@class="listtyle1"]/a/@title').extract()
            popularity = response.xpath('//div[@class="listtyle1"]//div[@class="c1"]/span/text()').extract()
            practice = response.xpath('//*[@id="listtyle1_list"]/div/a/div/div/div[2]/ul/li[1]/text()').extract()
            taste = response.xpath('//*[@id="listtyle1_list"]/div/a/div/div/div[2]/ul/li[2]/text()').extract()
            item = MeishijItem(dish_name=dish_name, popularity=popularity, practice=practice, taste=taste)
            yield item
        next_url=response.xpath('//*[@id="listtyle1_w"]/div[2]/div/a[last()]/@href').get()
        zhyy=response.xpath('//*[@id="listtyle1_w"]/div[2]/div/span/form/input[@type="text"]/@value').extract()
        q=int(zhyy[0])
        self.qq+=1
        print(self.qq)
        if self.qq is 57:
            return
        else:
            yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)