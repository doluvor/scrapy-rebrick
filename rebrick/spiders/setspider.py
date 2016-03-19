import scrapy
import json

from rebrick.items import SetItem

class SetSpider(scrapy.Spider):

    custom_settings = {
        'DOWNLOAD_DELAY' : 5
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
        for i in range(1950, 2017):
            yield scrapy.Request("https://rebrickable.com/api/search?key=0ru0idGVkf&format=json&type=S&min_year=%d&max_year=%d" % (i, i), self.parse)

    def parse(self, response):
        #print response.body
        jsonResponse = json.loads(response.body_as_unicode())

        for itemData in jsonResponse['results']:
            item = SetItem()
            item['set_id'] = itemData['set_id']
            item['set_name'] = ''
            item['set_pieces'] = itemData['pieces']
	    item['set_year'] = itemData['year']
	    item['set_theme1'] = itemData['theme1']
	    item['set_theme2'] = itemData['theme2']
	    item['set_theme3'] = itemData['theme3']
	    item['set_descr'] = itemData['descr']
	    item['set_img_small'] = itemData['img_sm']
	    item['set_img_tn'] = itemData['img_tn']
	    item['set_img_big'] = itemData['img_big']
	    item['set_url'] = itemData['url']
            yield item

