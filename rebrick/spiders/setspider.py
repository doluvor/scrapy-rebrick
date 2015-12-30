import scrapy

class SetSpider(scrapy.Spider):
    name = "setspider"
    allowed_domains = ["rebrickable.com"]
    start_urls = [
        "https://rebrickable.com/api/search?key=0ru0idGVkf&format=json&type=S&theme1=Technic&min_year=2015&max_year=2015"]

    def parse(self, response):
        filename = 'search_result.json'
        with open(filename, 'wb') as f:
            f.write(response.body)
