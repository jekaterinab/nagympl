#---------------zpracovani linku na .pdf ulozenych v souboru seznampdf.txt
#rozpracovany

pdf_seznam = open("D:/nagympl/trans_PDF/seznampdf.txt", "r", encoding = "utf8")
data = pdf_seznam.read()
print(type(data))

#rozdeleni textu na jednotlive linky
data_new = data.split(' ')
new = data_new[0].split("\n")

#zde budou seznamy linku pro kazdou skolu
1 = []
2 = []
3 = []
4 = []
5 = []
6 = []
7 = []
8 = []
9
10
11
12
13
14
15
16
17
18
19
20
21
22

print(new[0])

#zde trideni dle roku, chci trideni dle skoly
for link in new:
    if "2017" in link:
        year2017.append(link)
    elif "2018" in link:
        year2018.append(link)

print(year2018[6:9])
