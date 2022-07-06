from bs4 import BeautifulSoup
import requests


url = "https://www.jumia.co.ke/song-of-fire-whiskey-limited-edition-1-litre-johnnie-walker-mpg351693.html"
# headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

results=requests.get(url)
# soup=BeautifulSoup(result.content, 'html.parser')
soup= BeautifulSoup(results.text, 'html.parser')
prices = soup.find('span', class_='-fs24').string
# print(soup.prettify())


print(prices)