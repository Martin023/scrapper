import requests
from bs4 import BeautifulSoup

url = 'https://sky.garden/search/bag/products?s=bag'


results = requests.get(url)

soup = BeautifulSoup(results.text, 'html.parser')
tag = soup.find_all('app-product')
print(len(tag))
for item in tag:
    print(item.find('div', class_='ng-star-inserted').text)
    print("\n")