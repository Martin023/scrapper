
import requests
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')
    # print(doc.prettify())

    # name = doc.find_all(text = "Hello World")

    # print(name)

    tag = doc.find_all('div')
    
    print(tag)