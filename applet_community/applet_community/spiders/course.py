# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AppletCommunityItem

class CourseSpider(CrawlSpider):
    name = 'course'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+portal\.php\?mod=list\&catid=2\&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-\d+-1.html'),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        title = response.xpath('//h1[@class="ph"]/text()').get()
        author_p = response.xpath("//p[@class='authors']")
        author = author_p.xpath(".//a/text()").get()
        pub_time = author_p.xpath(".//span/text()").get()
        artice_content = response.xpath("//td[@id='article_content']//text()").getall()
        content = "".join(artice_content).strip()
        print('title', title)
        print('author_p', author_p)
        print('author', author)
        print('pub_time', pub_time)
        print('artice_content', artice_content)
        item = AppletCommunityItem(title=title, author=author
                         , pub_time=pub_time,
                         content=content)
        yield item