"""
The Main, to run the crawler and gather the weather data for coburg.
"""
#Import Crawler
from weather_coburg import crawl

#Ausführen Crawler
crawler = crawl("https://www.wetteronline.de/wetter/coburg")

crawler.ConStat()
print(crawler.Content())
