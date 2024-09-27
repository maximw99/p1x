import scrapy
from bs4 import BeautifulSoup
import requests



# class Blackrockspider(scrapy.Spider):
#     name = 'Blackrock'
#     start_urls = ['https://www.blackrock.com/de/privatanleger/markte/weekly-market-update?switchLocale=y&siteEntryPassthrough=true']

#     def parse(self, response):
#         blocks = response.css('div.para-content.col-xl-7.col-lg-9.col-12.ishares-remove-bootstrap-offset')

        # for x in response.css('div.para-content.col-xl-7.col-lg-9.col-12.ishares-remove-bootstrap-offset'):
        #     yield{
        #         'topic' : x.css('h3 *::text').getall(), 
        #         'item' : x.css('p *::text').getall()
        #     }

        
