# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from typing import Any

import scrapy
from scrapy import Field


class GetNewsItem(scrapy.Item):
    nsTITLE = scrapy.Field()
    nsURL = scrapy.Field()
    nsCONTENT = scrapy.Field()
    nsKEYWORDS = scrapy.Field()
