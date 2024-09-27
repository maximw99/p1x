url = 'https://www.blackrock.com/de/privatanleger/markte/weekly-market-update?switchLocale=y&siteEntryPassthrough=true'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")


test = soup.find_all("div", class_ =  "para-content col-xl-7 col-lg-9 col-12 ishares-remove-bootstrap-offset")

print(test[0])