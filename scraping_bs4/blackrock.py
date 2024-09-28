from bs4 import BeautifulSoup
import requests
import json


url = 'https://www.blackrock.com/de/privatanleger/markte/weekly-market-update?switchLocale=y&siteEntryPassthrough=true'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")


div = soup.find_all("div", class_ =  "para-content col-xl-7 col-lg-9 col-12 ishares-remove-bootstrap-offset")

headline = div[0].find('h3').text.strip()
content = div[0].find_all('p')

article = []


for line in content:
    hit = line.text.strip()
    article.append(str(hit))

article = article[0:18]
article_string = "".join(article)
article_string.replace("',", "")


obj = {
    'headline' : headline,
    'article' : article_string
}

json_obj = json.dumps(obj, ensure_ascii=False)

with open ('test.json', 'w') as outfile:
    outfile.write(json_obj)