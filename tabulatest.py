# import tabula
#import camelot

#tables = camelot.read_pdf("D:/data_gymply/Doppler_M_2019.pdf", pages='1', password=None, flavor='lattice', suppress_stdout=False, layout_kwargs={}, **kwargs)

import tabula
df = tabula.read_pdf("D:/data_gymply/GJH-2019.pdf", pages = 'all')
#df = tabula.read_pdf("D:/data_gymply/Doppler_M_2019.pdf")
#print(df)
with open(r"D:/pythonprocvicovani/tabulatest.csv") as soubor:
    soubor.write(df)

soubor.close()