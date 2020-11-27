from __future__ import unicode_literals
from scrapy import Spider, Selector, Request
from rumah_scrapper.items import RumahItem

from rumah_scrapper.helpers import get_random_ua, string2integer


class RumahSpider(Spider):
    name = "rumah_spider"
    allowed_domains = ["99.co"]

    # custom_settings = {
    #     "FEEDS": {
    #         "data_%(name)s_%(time)s.json": {
    #             "format": "json",
    #             "encoding": "utf8",
    #             "store_empty": False,
    #             "fields": None,
    #             "indent": 4,
    #             "item_export_kwargs": {"export_empty_fields": True},
    #         }
    #     }
    # }

    def __init__(self, iklan=None, properti=None, max_page=1000, *args, **kwargs):
        super(RumahSpider, self).__init__(*args, **kwargs)
        self.iklan = iklan
        self.properti = properti
        # self.start_urls = [f"https://www.99.co/id/{iklan}/{properti}?urut=2"]
        self.page_count = 0
        self.max_page = int(max_page)

    def start_requests(self):
        user_agent = get_random_ua()
        for i in range(self.page_count, self.max_page, 1):
            yield Request(
                url=f"https://www.99.co/id/{self.iklan}/{self.properti}?urut=2&hlmn={i}",
                callback=self.parse,
                headers={"user-agent": user_agent},
            )

    def parse(self, response):
        selector = Selector(text=response.body)

        property_id = selector.xpath(
            '//div[contains(@class,"property-list-info")]/@data-property-id'
        ).getall()
        price = selector.xpath('//span[@itemprop="price"]/@content').getall()
        bedroom = selector.xpath(
            '//*[@id="spec-icons"]/div[1]/div/span/text()'
        ).getall()
        bathroom = selector.xpath(
            '//*[@id="spec-icons"]/div[2]/div/span/text()'
        ).getall()
        building_area = selector.xpath(
            '//*[@id="spec-icons"]/div[3]/div/span/text()'
        ).getall()
        surface_area = selector.xpath(
            '//*[@id="spec-icons"]/div[4]/div/span/text()'
        ).getall()
        locality = selector.xpath('//li[@class="locality"]/text()').getall()
        province = selector.xpath('//li[@class="province"]/text()').getall()

        data = zip(
            property_id,
            bedroom,
            bathroom,
            building_area,
            surface_area,
            locality,
            province,
            price,
        )

        for item in data:
            rumah = RumahItem()
            rumah["property_id"] = int(item[0])
            rumah["bedroom"] = int(
                "".join(list(filter(lambda x: x.isdigit(), item[1])))
            )
            rumah["bathroom"] = int(
                "".join(list(filter(lambda x: x.isdigit(), item[2])))
            )
            rumah["building_area"] = string2integer(item[3])
            rumah["surface_area"] = string2integer(item[4])
            rumah["locality"] = item[5]
            rumah["province"] = item[6]
            rumah["price"] = int(item[7])

            yield rumah

            # next_page = selector.xpath('//li[@class="next"]/a/@href').get()

            # # check if there is next page element in html page source
            # if next_page:
            #     # get random user agent to prevent get blocked by web
            #     user_agent = get_random_ua()
            #     next_page = response.urljoin(next_page)
            #     yield Request(
            #         url=next_page,
            #         callback=self.parse,
            #         headers={"Referer": "same-origin", "user-agent": user_agent},
            #     )
