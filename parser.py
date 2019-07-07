import requests
from bs4 import BeautifulSoup

URL = "https://hotline.ua/computer-noutbuki-netbuki/" \
      "apple-macbook-air-13-silver-2018-mrec2/prices/"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

page = requests.get(URL, headers=headers)

bs = BeautifulSoup(page.content, 'html.parser')
# print(bs.prettify())
offers = bs.findAll('div', {'class': 'offers-item'})
print(offers)