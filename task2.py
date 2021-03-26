import requests
from bs4 import BeautifulSoup

d = {}
url = 'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту'
r = requests.get(url).text
soup = BeautifulSoup(r, 'lxml')
pages = soup.find('div', class_='toccolours plainlinks center').find_all('a', class_='external text')[2:32]
for i in pages:
    b = requests.get(i.get('href')).text
    soup = BeautifulSoup(b, 'lxml')
    title = soup.find('div', class_='mw-category-group').find('h3').text.strip()
    page = soup.find('div', class_='mw-category-group').find_all('li')
    d[title] = len(page)
for q,w in d.items():
    print((q + ':'), w)