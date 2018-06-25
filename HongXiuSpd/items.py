# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HongxiuspdItem(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()
    words = scrapy.Field()
    status = scrapy.Field()
    gender = scrapy.Field()
    collections = scrapy.Field()
    clicks = scrapy.Field()
    author = scrapy.Field()
    introduce = scrapy.Field()
    directory = scrapy.Field()
    url = scrapy.Field()
