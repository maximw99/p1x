from selenium import webdriver
import requests
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import xml.etree.ElementTree as ET

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from spacy.lang.de.stop_words import STOP_WORDS as de_stops
import matplotlib.pylab as plt

import json
import time
import traceback
from functions import blackrock_links, simplesort_links

options = Options() 
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

# driver = webdriver.Firefox()


# driver.get('')
# print(driver.title)



def get_links():

    xml_url = '' 
    response = requests.get(xml_url) 
    xml_content = response.content 
    root = ET.fromstring(xml_content) 

    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'} 
    hrefs = [elem.text for elem in root.findall('.//ns:loc', namespace)]

    return hrefs


def parse_links(links : list):

    products = []
    for link in links:
        product_stemp = link.find("produkt") # product at 58
        dummy = link[product_stemp + 8:]
        rest_stemp = dummy.find("/")
        product = dummy[:rest_stemp]
        products.append(product)

        print('------------------break-----------------')
        print(link)
        print(dummy)
        print(product)
        print('------------------break-----------------')
    
    return(products)


print('------------------break-----------------')

# links = get_links()
# products = parse_links(links=links)


# time.sleep(2)
# driver.close()