#Libraries:
import time
from itertools import product

import requests
from bs4 import BeautifulSoup as bs


class crawl():

    def __init__(self, address):
        self.address = address
        self.r = requests.get(self.address)
        self.head_info = self.r.headers

    def ConStat(self):
        if self.r.status_code == 200:
            print("200 - Connection successful established")
        else:
            print(str(self.r.status_code) + " - Something went wrong")
        time.sleep(1)

    def Content(self):
         self.page_cont = bs(self.r.text, "html.parser")
         selected = self.page_cont.select_one("#product_display")
         if selected:
             date = selected.select_one("span.date_time")

             if date:
                 return date
             else:
                 print("No <span class='date_time' found!")
         else:
            print("DIV with id='content' not found!")


    def GetRawContent(self):
        for p in self.head_info:
            print(p + " : " + self.head_info[p])
            time.sleep(1)



