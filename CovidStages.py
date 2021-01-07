import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.traviscountytx.gov/news/2020/1945-novel-coronavirus-covid-19-information#:~:text=Austin%2DTravis%20County%20is%20currently,%2D19%20Risk%2DBased%20Guidelines.")
soup = BeautifulSoup(r.text, 'html.parser')
stage = soup.findAll('p')

longtext = stage[4].text

poop = longtext.split(".")
print(poop[0])
