import requests
from bs4 import BeautifulSoup
import lxml
import xml

r = requests.get(url='https://www.google.com')
print(r.headers)

soup = BeautifulSoup("<p>Some<b>bad<i>HTML", "xml")
print(soup.prettify())
soup.find(text="bad")
soup.i

soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "xml")
print(soup.prettify())

