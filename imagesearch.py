from bs4 import BeautifulSoup
import urllib.request

def getImages(url):
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    urls = []

    soup = BeautifulSoup(urllib.request.urlopen(req), "html.parser")
    
    for img in soup.find_all("img", src=True):
        if img['src'].startswith("https://"):
            urls.append(img['src'])
    
    return urls
