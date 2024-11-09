from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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


def page_wrapper(driver):
    # driver.get('')
    driver.get('')
    time.sleep(2) # wait for pop-ups

    pop_up = driver.find_element(By.XPATH, "//button[text()='Nur erforderlich']")
    pop_up.click()
    time.sleep(2)


    pop_up = driver.find_element(By.XPATH, "//a[@data-link-event='Accept t&c: individual']")
    pop_up.click()



    # content_divs = driver.find_elements(By.XPATH, "//div[@class='content-block-data']")
    # describtion_divs = driver.find_elements(By.XPATH, "//div[@class='description']")
    # print(len(rows))

    content = []

    try:
        tabs = driver.find_element(By.XPATH, "//div[@class='tabs']")
        elements = tabs.find_elements(By.XPATH, './/a')
        # print(len(element))
        for element in elements:
                
        # time.sleep(3)
        # element[2].click()
        # time.sleep(3)
            try:
                element.click()
                rows = driver.find_elements(By.XPATH, "//div[@class='row']")
                data = []
                for row in rows:
                    headers = row.find_elements(By.XPATH, ".//h2 | .//h3")
                    paragraphs = row.find_elements(By.XPATH, ".//p") 
                    header_texts = [header.text for header in headers]
                    paragraph_texts = [paragraph.text for paragraph in paragraphs] 
                    data.append({'headers': header_texts, 'paragraphs': paragraph_texts})

                    # for element in data:
                    #     print('--------------------------------------------------------------')
                    #     print(element)
                    #     print('--------------------------------------------------------------')

                    content.append(data)
                driver.back()
            except:
                traceback.print_exc()
                driver.back()
                pass

    except:
        pass



    print(content[0])

    # with open('wrapper.json', 'w', encoding='utf-8') as f:
    #     json.dump(content, f, ensure_ascii=False, indent=4)

    # except:
    #     traceback.print_exc()
    #     pass



# page_wrapper(driver=driver)
print('------------------break-----------------')



driver.get("")
print(driver.title) 


time.sleep(2)
driver.close()