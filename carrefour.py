
from bs4 import BeautifulSoup
import requests


url = "https://www.carrefour.ke/mafken/en/v4/search?keyword=tecno"
# headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

results=requests.get(url)
# soup=BeautifulSoup(result.content, 'html.parser')
soup= BeautifulSoup(results.text, 'html.parser')

tag = soup.find_all('a', class_='css-yqd9tx')

for item in tag:
    print(item.prettify())