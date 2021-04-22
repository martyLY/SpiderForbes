# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from json import JSONEncoder


class SpiderforbesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    num = scrapy.Field()

# subclass JSONEncoder
class ItemEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
