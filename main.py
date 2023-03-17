

#Import libraries:
import time
import requests
from bs4 import BeautifulSoup as bs



r = requests.get("https://www.spacex.com/vehicles/starship/")
#print(r.status_code)
#print(r.text)
head_info = r.headers

#get header data:
for p in head_info:
    print(p + ":" + head_info[p])
    #time.sleep(1)



content = r.text
doc = bs(content, "html.parser")


#SpaceX Info:
#print(doc.select(".section"))

for item in doc.select(".section"):
    print(item.select(".animate"))