

#Import libraries:
import requests
from bs4 import BeautifulSoup as bs



r = requests.get("https://www.spacex.com/")
print(r.status_code)
print(r.headers)
print(r.text)