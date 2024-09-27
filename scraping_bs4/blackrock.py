from bs4 import BeautifulSoup
import requests


url = 'https://www.blackrock.com/de/privatanleger/markte/weekly-market-update?switchLocale=y&siteEntryPassthrough=true'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")


div = soup.find_all("div", class_ =  "para-content col-xl-7 col-lg-9 col-12 ishares-remove-bootstrap-offset")


text = div[0].find_all('p')
strong = div[0].find_all('strong')

# for hit in div[0].find_all('strong'):
#     hit = hit.text.strip()
#     print(hit)


# for hit in div[0].find_all('strong'):
#     hit = hit.text.strip()
#     print(hit)

arcticle = []
for hit in div[0].find_all('p'):
    # hit = hit.text.strip()
    # print(hit)
    arcticle.append(hit)

article_stripped = []
for line in arcticle:
    print(line)
    if line.find('<strong>') == -1:
        print('no hit')
    else:
        print('hit')
        hit = line.text.strip()
        article_stripped.append(hit)
    print('=============================')



print(article_stripped)