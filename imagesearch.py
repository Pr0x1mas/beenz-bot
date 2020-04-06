#    ===Python Web Image Loader v1.0===
#          ===imagesearch.py===
#      ===Copyright 2020 Pr0x1mas===

# this script is a piece of utter shite but it works

from bs4 import BeautifulSoup
import urllib.request

def getImages(url):
    req = urllib.request.Request( # load webpage or something
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    urls = []

    soup = BeautifulSoup(urllib.request.urlopen(req), "html.parser") # I think this opens the html code
    
    for img in soup.find_all("img", src=True): # find literally every image on the page
        if img['src'].startswith("https://"):
            urls.append(img['src'])
    
    return urls
