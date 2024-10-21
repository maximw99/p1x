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


driver = webdriver.Firefox()

pop_ups = ["//button[text()='Nur erforderlich']"]

# base point for crawling
driver.get("")
time.sleep(2) # wait for pop-ups

# kill pop-ups
pop_up = driver.find_element(By.XPATH, pop_ups[0])
pop_up.click()

try:
    # get the navbar topics
    navbar_topics = []
    for catch in driver.find_elements(By.XPATH, "//li[@class='display-cell menu']"):
        topic_name = catch.find_element(By.XPATH, ".//*").get_attribute('data-id')
        navbar_topics.append(topic_name)

    # get all href links
    links = []
    menu_points = driver.find_elements(By.XPATH, "//a[@class='menu-item']")
    for catch in menu_points:
        href = catch.get_attribute('href')
        links.append(href)

    # clean and group links
    br_links = []
    other_links = []
    for link in links:
        if 'www.blackrock.com' in link:
            br_links.append(link)
        else:
            other_links.append(link)


    # print(len(br_links))
    # print(len(other_links))


    # sort links
    for link in br_links:
        seperator = link.find('privatanleger/')
        # print(link)
        # print(link[43:])
        # print(seperator)


    stop_words = list(de_stops)
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    X = vectorizer.fit_transform(br_links)

    # wcss = []
    # K = range(2, 15)

    # for k in K:
    #     model = KMeans(n_clusters=k, random_state=42)
    #     model.fit(X)
    #     wcss.append(model.inertia_)


    # plt.figure(figsize=(10, 5))
    # plt.plot(K, wcss, 'bx-')
    # plt.xlabel('Anzahl Cluster')
    # plt.ylabel('WCSS')
    # plt.title('Optimale Cluster Anzahl')
    # plt.show()



    true_k = 6
    model = KMeans(n_clusters=true_k, random_state=42)
    model.fit(X)
    clusters = model.predict(X)

    # print(len(clusters))


    # for res in clusters:
    #     print(res)

    for cluster in range(true_k):
        print(f"Cluster {cluster}:")
        for i, link in enumerate(br_links):
            if clusters[i] == cluster:
                print(link)
    










    # res = driver.find_element(By.XPATH, "//div[@class='tray']")
    # print(len(res))

    # topics = res.find_elements(By.XPATH, "//ul[@role='menu']")
    # for item in topics:
    #     print(type(item))
    #     lines = item.find_elements(By.XPATH, "//li")
    #     for a in lines:
    #         points = a.find_elements(By.XPATH, "//a[@class='menu-item']")
    #         for link in points:
    #             href = link.get_attribute('href')

    # for item in topics:
    #     line = item.find_element(By.XPATH, "//li")
    #     points = line.find_elements(By.XPATH, "//a[@class='menu-item']")
    #     print(len(line))
        # for link in points:
        #     href = link.get_attribute('href')
        #     print(href)

    # sub_topics = []
    # for topic in res:
    #     results = topic.find_elements(By.XPATH, "//li")
    #     for item in results:
    #         href = item.find_element(By.XPATH, "//a[@class='menu-item']").get_attribute('href')
    #         print(href)

    # get second line points    
    # for topic in navbar_topics:
    #     points = topic[1].find_elements(By.XPATH, ".//*")
    #     topic.append(points)
    #     # topic.append((topic[1].find_element(By.XPATH, ".//*").get_attribute('data-id'), topic[1].find_element(By.XPATH, ".//*").get_attribute('href')))
        # topic.append((topic[1].find_element(By.XPATH, "//a[@id='mm-lsd4m4op']").get_attribute('data-id'), topic[1].find_element(By.XPATH, "//a[@id='mm-lsd4m4op']").get_attribute('href')))
        
    # driver.get(navbar_topics[0])

    # navbar_points.append(navbar.find_elements(By.TAG_NAME('li')))

except Exception:
    traceback.print_exc()
    pass






# shut down
# time.sleep(1)
driver.quit()