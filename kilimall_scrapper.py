from bs4 import BeautifulSoup
import requests

url = "https://www.kilimall.co.ke/new/commoditysearch?q=bag"
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'}
results = requests.get(url, headers=header)

soup = BeautifulSoup(results.text, 'lxml')
tag = soup.find_all('div', class_="el-row")
# for item in tag:

#     print (item.find('h4',class_="qa-advert-title").text)
#     print (item.find('p',class_="b-list-advert__item-price").text)
#     print ('\n')


# for item in tag:
#     print(item.prettify())

print(tag)



# import requests
# from bs4 import BeautifulSoup

# #############
# #code to use a searchterm
# searchterm = 'bag'
# url = 'https://www.kilimall.co.ke/new/commoditysearch?q={searchterm}'

# # url = 'https://www.kilimall.co.ke/new/goods/16602047-Womens-sport-shoes--sneakers-athletic-ladies-flat-shoes-students-casual-running-shoes-girls-PU-leather-shoes'
# headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

# page=requests.get(url,headers=headers)
# soup=BeautifulSoup(page.content, 'html.parser')

# # print(soup.prettify())
# all_scripts = soup.find_all('script')

# print(all_scripts)

# # script = all_scripts[2]
# # print(script)
# # name = (script[0])
# # price = (script[1])
# # rating = (script[2].split(',')[5])

# # print(script)
# # print(name)
# # print(price)
# # print(rating)
