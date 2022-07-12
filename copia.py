from bs4 import BeautifulSoup
import requests

url = 'https://copia.co.ke/?s=chair&post_type=product&title=1&excerpt=0&content=0&categories=0&attributes=0&tags=0&sku=1&orderby=date-DESC&ixwps=1'

results=requests.get(url)
# soup=BeautifulSoup(result.content, 'html.parser')
soup= BeautifulSoup(results.text, 'html.parser')
prices = soup.find_all('div',class_='product-small')
for item in prices:
    print(item.find('a').get('href'))
    # print(item.find('img').get('data-src'))
    # print(item.find('p', class_='woocommerce-loop-product__title').text)

    # print(item.find('bdi').text)
    print('\n')

    # print(prices)
