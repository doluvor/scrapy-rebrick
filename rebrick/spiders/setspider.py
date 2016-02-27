import scrapy
import json

from rebrick.items import SetItem

class SetSpider(scrapy.Spider):
    name = "setspider"
    allowed_domains = ["rebrickable.com"]
    start_urls = [
        "https://rebrickable.com/api/search?key=0ru0idGVkf&format=json&type=S&theme1=Technic&min_year=2015&max_year=2015"]

    def parse(self, response):
        #print response.body
        jsonResponse = json.loads(response.body_as_unicode())
        print jsonResponse['results'][0]
        item = SetItem()
        item['set_id'] = '1'
        item['set_name'] = 'testName'
        item['set_pieces'] = '1000'
        yield item
