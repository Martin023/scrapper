import requests
from bs4 import BeautifulSoup
# def find_a_product():

#     url = "https://www.jumia.co.ke/catalog/?q=johnie+walker" 
#     results = requests.get(url)


#     # print(results.text)
#     soup = BeautifulSoup(results.text, 'html.parser')
#     # product = soup.find_all('div', class_='info', )

#     product = soup.find_all('div', class_='img-c')
#     for item in product:
#         print(item.prettify())
#         # print(item.find('h3', class_='name').text)
#         # print(item.find('div', class_='prc').text)
#         # print(item.find('div', class_='_s').text)
        
#         print (item.find('img[data-src]'))
       
#         print('\n')

# find_a_product()

##-----------------------------------------------------------------------------------
url = "https://www.jumia.co.ke/catalog/?q=dress"

results = requests.get(url)

soup = BeautifulSoup(results.text, 'html.parser')
# tag = soup.find_all('h3', class_='name')
# product_name = soup.find_all('h3', class_='prc')
# stars = soup.find_all('div', class_='_s')

product = soup.find_all('article')


for item in product:
    # print(item.prettify())
    # print(item.find('a').get('href'))
    if item.find('a').get('href')and item.find('h3', class_='name') and item.find('div', class_='prc')and item.find('img',class_='img') and item.find('div', class_='_s'):
        # print(item.find('h3', class_='name').text)
        # print(item.find('div', class_='prc').text)
        # print(item.find('div', class_='_s').text)
        # print(item.find('img',class_="img").get('data-src'))
        print('https://jumia.co.ke'+item.find('a').get('href'))
        print('\n')


# print(product)