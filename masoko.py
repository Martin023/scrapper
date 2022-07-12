from bs4 import BeautifulSoup
import requests

url = "https://www.masoko.com/search-results?query=techno"

results = requests.get(url)

soup = BeautifulSoup(results.text, 'html.parser')
tag = soup.find_all('li')

# print(tag)
for item in tag:
    print(item.prettify())