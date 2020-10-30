##prvni pokus
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


pages = set()
def getLinks(pageUrl):
    html = urlopen(pageUrl)
    print(pageUrl)
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a'): #tady to neumim nastavit
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(pageUrl+"/"+newPage)
getLinks('http://www.matematickaberuska.cz/vysledky')
print(pages)
