#    ===Python Web Image Loader v1.1===
#          ===imagesearch.py===
#      ===Copyright 2020 Pr0x1mas===

# this script is a piece of utter shite but it works

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re

def getImages(url):
    req = urllib.request.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    urls = []

    soup = BeautifulSoup(urllib.request.urlopen(req), "html.parser") # I think this opens the html code
    
    for img in soup.find_all("img", src=True): # find literally every image on the page
        if img['src'].startswith("https://"):
            urls.append(img['src'])
    
    return urls

class song:
    def __init__(self, searchterm):
        query_string = urllib.parse.urlencode({"search_query" : searchterm})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        self.url = "http://www.youtube.com/watch?v=" + search_results[0]

        req = urllib.request.Request("http://www.youtube.com/watch?v=" + search_results[0], data=None, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        soup = BeautifulSoup(urllib.request.urlopen(req), "html.parser") # I think this opens the html code
        title = soup.find("title")

        self.vname = title.contents[0]
