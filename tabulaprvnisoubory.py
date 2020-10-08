import pandas as pd
import tabula

df = tabula.read_pdf("D:/nagympl/nagympl/data_katka/06-2018-JanaKeplera.pdf", pages = 'all')
print(df)


#soubor = open("D:/nagympl/nagympl/data_katka/06-2018-JanaKeplera.txt")
#soubor.write(df)
#soubor.close()


# Keplera:
# df je list
# nešlo uložit jako .csv ani jako .txt, viz nad aleji


# Nad Aleji: 
#df.info = df je list
# nešlo uložit jako .csv ani jako .txt
#soubor = open("D:/nagympl/nagympl/07-2020-Alej.txt")
#ValueError: Invalid file path or buffer object type: <class 'list'>

# Nad Stolou: nelusti PDF. Výsledek je asi takový:

#[Empty DataFrame
#Gymnázium, Praha 7, Nad Štolou 1                    zpracováno:          2. května 2017, Unnamed: 1]
#Index: [], Empty DataFrame
#za ZŠMATČJAJ, PořadíRozhodnutí] o v é  h o d n o c e n í
#Index: []]