#crawler stranek matematickaberuska.cz
# 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#funkce kontrola obsahu linku 
def check_content(word, content):
    for c in content:
        if word in str(c):
            return True
    return False

#seznam linku na soubory .pdf
pdfs = []

#funkce prochazeni linku a hledani linku na .pdf
def getLinks(pageUrl):
    html = urlopen(pageUrl)
    # print(pageUrl)
    bs = BeautifulSoup(html, 'html.parser')

    for link in bs.find_all('a'):
        if 'href' in link.attrs and check_content('folder.png', link.contents):
            # print(link)
            newPage = link.attrs['href']
            # pages.add(pageUrl + "/" +newPage)
            getLinks(pageUrl+ "/" + newPage)
            #print(pageUrl + "/" +newPage)
        if 'href' in link.attrs and check_content('pdf.png', link.contents):
            newPage = link.attrs['href']
            pdfs.append(pageUrl + "/" + newPage)
           # print(pageUrl + "/" +newPage) 


#volani funkce s argumentem - linkem na jednotlive rocniky
getLinks('http://www.matematickaberuska.cz/vysledky/2017/Praha/st%c3%a1tn%c3%ad')
getLinks('http://www.matematickaberuska.cz/vysledky/2018/Praha/st%c3%a1tn%c3%ad')
getLinks('http://www.matematickaberuska.cz/vysledky/2019/Praha/st%c3%a1tn%c3%ad')
getLinks('http://www.matematickaberuska.cz/vysledky/2020/Praha/st%c3%a1tn%c3%ad')
#print(pdfs)

#zapis linku na .pdf do souboru seznampdf.txt na pocitaci na uvedene adrese
with open("D:/nagympl/trans_PDF/seznampdf.txt", "w") as seznampdf:
    for pdf in pdfs:
        seznampdf.write(pdf)
        seznampdf.write("\n")

#je treba napsat funkci, ktera bude tridit linky pdf do slozek, nejlepe dle skol. 
# Zatim bohuzel nevim, jak vyfilfrovat kriteria, vysledky, vysledky skol, ktere nejsou relevantni
# 


