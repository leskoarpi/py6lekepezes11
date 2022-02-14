'''
Listaelemek leképezése, Comprehensive list:
----------
eredeti = [11, 19, 7, -3]
eredmeny = [x * 2 for x in eredeti]
eredmeny_szurve = [x * 2 for x in eredeti if x > 0]
----------
szamok = [5, 8, 3, 11, 12]
paros_szamok = [x for x in szamok if x % 2 == 0]
---------
1.1 Feladat
Készíts egy programot, listaleképzéssel (Comprehensive list), amely a felhasználó által megadott szót, csupa nagybetűs formában írja ki a képernyőre!

A megoldáshoz használd a sztringek upper() metódusát! 
'''
beker = input('kisbetus: ')
eredmeny = [print(beker.upper())]
