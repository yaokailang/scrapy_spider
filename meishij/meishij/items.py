# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeishijItem(scrapy.Item):
    dish_name=scrapy.Field()
    popularity=scrapy.Field()
    practice=scrapy.Field()
    taste=scrapy.Field()
