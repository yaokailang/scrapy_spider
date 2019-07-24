# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GzPurchaseItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    turnover = scrapy.Field()
    zhaobiao_type = scrapy.Field()
    title_url = scrapy.Field()
    danwei_name = scrapy.Field()
