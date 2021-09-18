# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YoutubeItem(scrapy.Item):
    # define the fields for your item here like:
    channel_name = scrapy.Field()
    channel_url = scrapy.Field()
    subscribers = scrapy.Field()
    total_views = scrapy.Field()
    date_joined = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
    related_links = scrapy.Field()
    
