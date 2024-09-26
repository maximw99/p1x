import scrapy

class Blackrockspider(scrapy.Spider):
    name = 'Blackrock'
    start_urls = ['https://www.blackrock.com/de/privatanleger/markte/weekly-market-update']

    def parse(self, response):
        # blocks = response.css('div.para-content.col-xl-7.col-lg-9.col-12.ishares-remove-bootstrap-offset')

        for x in response.css('div.para-content.col-xl-7.col-lg-9.col-12.ishares-remove-bootstrap-offset'):
            yield{
                'test' : x.css('p').get()
            }