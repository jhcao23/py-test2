import requests
from bs4 import BeautifulSoup

r = requests.get(url='https://www.google.com')
print(r.headers)

soup = BeautifulSoup("<p>Some<b>bad<i>HTML", "lxml")
print(soup.prettify())
soup.find(text="bad")
soup.i

soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "xml")
print(soup.prettify())

