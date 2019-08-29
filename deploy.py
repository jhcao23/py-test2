import requests

r = requests.get(url='https://www.google.com')
print(r.headers)
