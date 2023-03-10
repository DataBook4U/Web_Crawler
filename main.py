

#Import libraries:
import time
import requests
from bs4 import BeautifulSoup as bs



r = requests.get("https://www.spacex.com/")
#print(r.status_code)
#print(r.text)
head_info = r.headers

#get header data:
for p in head_info:
    print(p + ":" + head_info[p])
    time.sleep(1)



content = r.text
doc = bs(content, "html.parser")

for p in doc.find_all("p"):
    print(p.text)

#print(doc.find_all("p"))