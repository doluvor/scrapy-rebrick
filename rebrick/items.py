# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SetItem(scrapy.Item):
    # define the fields for your item here like:
    set_id = scrapy.Field()
    set_name = scrapy.Field()
    set_pieces = scrapy.Field()
    
