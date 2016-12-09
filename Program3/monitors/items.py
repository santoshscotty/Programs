# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MonitorsItem(scrapy.Item):
    Url = scrapy.Field()
    Title = scrapy.Field()
    Name = scrapy.Field()
    Thumbnail = scrapy.Field()
    Price = scrapy.Field()
    ProductId = scrapy.Field()
    DeliveryInfo = scrapy.Field()
