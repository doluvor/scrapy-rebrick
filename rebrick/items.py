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
    set_year = scrapy.Field()
    set_theme1 = scrapy.Field()
    set_theme2 = scrapy.Field()
    set_theme3 = scrapy.Field()
    set_descr = scrapy.Field()
    set_url = scrapy.Field()
    set_img_tn = scrapy.Field()
    set_img_small = scrapy.Field()
    set_img_big = scrapy.Field() 

