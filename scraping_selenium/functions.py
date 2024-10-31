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


def blackrock_links(driver):

    try:
        pop_ups = ["//button[text()='Nur erforderlich']"]
        # base point for crawling
        driver.get("")
        time.sleep(2) # wait for pop-ups

        # kill pop-ups
        pop_up = driver.find_element(By.XPATH, pop_ups[0])
        pop_up.click()

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

    except Exception:
        traceback.print_exc()
        pass

    # driver.quit()
    return br_links


def h2_wrapper():
    driver.get('https://www.blackrock.com/de/privatanleger/themen/multi-asset')
    time.sleep(2) # wait for pop-ups

    pop_up = driver.find_element(By.XPATH, "//button[text()='Nur erforderlich']")
    pop_up.click()
    time.sleep(2)


    pop_up = driver.find_element(By.XPATH, "//a[@data-link-event='Accept t&c: individual']")
    pop_up.click()


    content = []
    content_divs = driver.find_elements(By.XPATH, "//div[@class='content-block-data']")
    describtion_divs = driver.find_elements(By.XPATH, "//div[@class='description']")
    print(len(content_divs))

    for catch in content_divs:
        try:
            header = catch.find_element(By.XPATH, ".//h3[@class='sub-heading']").text
            print('header: ', header)
        except:
            pass
        try:
            text = catch.find_element(By.XPATH, ".//p").text
            print('text: ', text) 
        except:
            pass
    
    print('------------------break-----------------')


def describtion_wrapper(driver):
    content = []
    content_divs = driver.find_elements(By.XPATH, "//div[@class='content-block-data']")
    describtion_divs = driver.find_elements(By.XPATH, "//div[@class='description']")
    print(len(content_divs))

    for catch in describtion_divs:
        try:
            print('----------------in-------------------')
            text = catch.find_element(By.XPATH, ".//p").text
            print(text)
            content.append(text)
        except Exception:
            traceback.print_exc()
            pass


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


def cluster_topics(br_links : list):
    stop_words = list(de_stops)
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    X = vectorizer.fit_transform(br_links) # vectorize links
    terms = vectorizer.get_feature_names_out() # get features

    true_k = 6 # based on elbow method
    model = KMeans(n_clusters=true_k, random_state=42)
    model.fit(X)
    clusters = model.predict(X) # clustering

    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    cluster_names = []

    # get top topics for cluster
    for i in range(true_k):
        top_terms = [terms[ind] for ind in order_centroids[i, :5]]
        # cluster_name = ' '.join(top_terms)
        # if 'blackrock' not in cluster_name:
        cluster_names.append(top_terms)
        # print(f"Cluster {i}: {cluster_name}")
        # print(cluster_names)

    groups = []

    # sort links into clusters
    for cluster in range(true_k):
        # print(f"Cluster {cluster}:")
        group = []
        group.append(cluster_names[cluster])
        for i, link in enumerate(br_links):
            if clusters[i] == cluster:
                # print(link)
                group.append(link)
        groups.append(group)
    return groups


def search_topic(clusters : list):
    search = str(input('search topic: ', ))
    found_clusters = []
    hit = False
    for cluster in clusters:
        # print(cluster)
        if search in cluster[0]:
            found_clusters.append(cluster)
            hit = True
    return (found_clusters, hit)


def elbow_method(X):
    wcss = []
    K = range(2, 15)

    for k in K:
        model = KMeans(n_clusters=k, random_state=42)
        model.fit(X)
        wcss.append(model.inertia_)


    plt.figure(figsize=(10, 5))
    plt.plot(K, wcss, 'bx-')
    plt.xlabel('Anzahl Cluster')
    plt.ylabel('WCSS')
    plt.title('Optimale Cluster Anzahl')
    plt.show()


def loop(links : list):
    hit = False
    while hit == False:
        array, hit = search_topic(links)
        links = array[0]
        print('found links: ')
        for element in links[1:]:
            print(element[43:])