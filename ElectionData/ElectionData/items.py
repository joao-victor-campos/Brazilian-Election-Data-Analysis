# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ElectiondataItem(scrapy.Item):
   
    file_urls = scrapy.Field()
    original_file_name = scrapy.Field()
    files = scrapy.Field
