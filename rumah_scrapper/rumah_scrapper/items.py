# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class RumahItem(Item):
    # define the fields for your item here like:
    property_id = Field()
    bedroom = Field()
    bathroom = Field()
    building_area = Field()
    surface_area = Field()
    locality = Field()
    province = Field()
    price = Field()
