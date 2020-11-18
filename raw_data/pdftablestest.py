import pdftables_api

c = pdftables_api.Client('d8eseyzkn3ar')
c.csv('http://www.matematickaberuska.cz/vysledky/2017/Praha/státní/www.gjk.cz/8_vysledky_web-dle_poradi.pdf', 'D:/nagympl/trans_PDF/06_2017_pythonapi.csv')