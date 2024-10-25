from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from spacy.lang.de.stop_words import STOP_WORDS as de_stops
import matplotlib.pylab as plt

import time
import traceback
from functions import blackrock_links


driver = webdriver.Firefox()

links = blackrock_links(driver)
# print(links)



def simplesort_links(links : list):
    fonds_links = []
    markt_links = []
    topic_links = []
    product_links = []
    wiki_links = []
    left_links = []

    for link in links:
        if 'fonds-im-fokus' in link:
            fonds_links.append(link)
        elif 'markte' in link:
            markt_links.append(link)
        elif 'themen' in link:
            topic_links.append(link)
        elif 'produkt' in link:
            product_links.append(link)
        elif 'wissenswertes' in link:
            wiki_links.append(link)
        else:
            left_links.append(link)

    # for link in fonds_links:

    print(fonds_links)
    print('***************')
    print(topic_links)
    print('***************')
    print(markt_links)
    print('***************')
    print(product_links)
    print('***************')
    print(wiki_links)
    print('***************')
    print(left_links)
    print('***************')


simplesort_links(links)