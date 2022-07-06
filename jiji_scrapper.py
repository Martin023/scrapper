from bs4 import BeautifulSoup
import requests

url1 = "https://jiji.co.ke/search?query=johnie"

results = requests.get(url1)

soup = BeautifulSoup(results.text, 'html.parser')
tag = soup.find_all('div',class_="qa-advert-list-item")
for item in tag:
    print(item.prettify())
    # print (item.find('h4',class_="qa-advert-title").text)
    # print (item.find('p',class_="b-list-advert__item-price").text)
    print (item.find('img').get('src'))
    print (item.find('div', class_="b-list-advert__item-info").text)
    print ('\n')

