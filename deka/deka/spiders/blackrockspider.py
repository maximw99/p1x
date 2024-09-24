import scrapy

class Blackrockspider(scrapy.Spider):
    name = 'Blackrock'
    start_urls = ['https://www.blackrock.com/de/privatanleger/markte/weekly-market-update']

    def parse(self, response):
        pass