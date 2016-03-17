import scrapy
import json

from rebrick.items import SetItem

class SetSpider(scrapy.Spider):

    custom_settings = {
        'DOWNLOAD_DELAY' : 1
    }

    name = "setspider"
    allowed_domains = ["rebrickable.com"]
    # start_urls = [
    #     "https://rebrickable.com/api/search?key=0ru0idGVkf&format=json&type=S&theme1=Technic&min_year=2015&max_year=2015",
    #     "https://rebrickable.com/api/search?key=0ru0idGVkf&format=json&type=S&theme1=Technic&min_year=2014&max_year=2014"
    # ]

    startYear = 2015
    endYear = 2015

    theme1 = ["Technic",
              "Super Heroes",
              "Creator",
              "Modular Buildings",
              "Town",
              "Ninjago",
              "Star Wars",
              "Friends",
              "Classic",
              "Agents",
              "Seasonal",
              "Speed Champions",
              "Legends of Chima",
              "Pirates",
              "Scooby-Doo",
              "Elves",
              "LEGO Ideas and CUUSOO",
              "Other",
              "Disney Princess",
              "Space",
              "Bionicle",
              "Train",
              "Castle"]

    def start_requests(self):
        for i in range(2014, 2014+1):
            yield scrapy.Request("https://rebrickable.com/api/search?key=0ru0idGVkf&format=json&type=S&min_year=%d&max_year=%d" % (i, i), self.parse)

    def parse(self, response):
        #print response.body
        jsonResponse = json.loads(response.body_as_unicode())
        print len(jsonResponse['results'])
        #item = SetItem()
        #item['set_id'] = '1'
        #item['set_name'] = 'testName'
        #item['set_pieces'] = '1000'
        #yield item
