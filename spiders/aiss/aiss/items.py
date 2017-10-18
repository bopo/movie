# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

    
class AissItem(scrapy.Item):
    catalog = scrapy.Field()
    author = scrapy.Field()
    source = scrapy.Field()
    level = scrapy.Field()
    title = scrapy.Field()
    cover = scrapy.Field()
    count = scrapy.Field()
    issue = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()


