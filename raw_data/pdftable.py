
#----------Zpracovani pdf v convertoru PDFTABLES pres API


#nejlepe poustej z terminalu ze slozky, kde mas ulozene soubory i script, vsak to vis :) 
#import knihovny
import pdftables_api
import os
import re
import requests

#v uvozovkach je klic k accountu, je registrovan na muj mail. limit je 50 stranek, az vyprsi, muzes si zaregistrovat sama, 
# ziskat novy klic a nahradit. 
c = pdftables_api.Client('gozehk8e1ip6')

#nastaveni roku a skoly - zde priklad
year = 2017
schoolid = "03"

#----------soubor je v pocitaci:
# muzes dat vice souboru najednou jako jednotlive radky. 
# rok a skola se doplnuji automaticky podle zadanych promennych v r. 14 a 15.
# prvni retezec je adresa zdrojoveho souboru v pocitaci, druhy je cilovy soubor, ktery se automaticky 
# ulozi na uvedene adrese pod uvedenym jmenem 

c.csv(f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}-{year}-Pisnicka-neprijati.pdf', f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}_{year}_n_pythonapi.csv')
c.csv(f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}-{year}-Pisnicka-prijati.pdf', f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}_{year}_pythonapi.csv')
c.csv(f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}-{year+1}-Pisnicka-neprijati.pdf', f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}_{year+1}_n_pythonapi.csv')
c.csv(f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}-{year+2}-Pisnicka-prijati.pdf', f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}_{year+2}_pythonapi.csv')
c.csv(f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}-{year+2}-Pisnicka-neprijati.pdf', f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}_{year+2}_n_pythonapi.csv')
c.csv(f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}-{year+3}-Pisnicka-prijati.pdf', f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}_{year+3}_pythonapi.csv')
c.csv(f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}-{year+3}-Pisnicka-neprijati.pdf', f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}_{year+3}_n_pythonapi.csv')


#link na soubor na Berusce. linky stahuje script a uklada do souboru.txt. Je treba jeste napsat modul (trideni_pdf.py), 
# # který uloží link do prislusneho seznamu nebo souboru. 
# # A dale modul, ktery bude vybirat linky podle prislusneho roku a skoly 
# source_web = requests.get('http://www.matematickaberuska.cz/vysledky/2018/Praha/st%c3%a1tn%c3%ad/www.gpisnicka.cz//vysl-8l-prijati-2018.pdf')
# with open(f"D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}_{year}.pdf", "wb") as source:
#     source.write(source_web.content)


#přeuložení do CSV a nahrani 
#c.csv(f"D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}_{year}.pdf", f'D:/nagympl/trans_PDF/ostre soubory/{schoolid}/{schoolid}_{year}_pythonapi.csv')





