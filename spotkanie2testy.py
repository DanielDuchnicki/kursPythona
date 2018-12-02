from spotkanie2.palindromy import *
from spotkanie2.przestepne import *
# from spotkanie2.rozmienianie import *
from spotkanie2.zadanie1 import *
from spotkanie2.zadanie2 import *
from spotkanie2.zadanie3 import *
from spotkanie2.zadanie4 import *
from spotkanie2.zadanie5 import *
# from spotkanie2.zadanie6 import *
from spotkanie2.zadaniedomowe1 import *
from spotkanie2.zadaniedomowe2_algorytm import *


# palindromy
dane = ['kajak', 'kobyłamamałybok', 'palindrom', [1, 2, 1], [2, 3]]
wersje = [wersja1, wersja2]
for funkcja in wersje:
    for slowo in dane:
        print("{0}: {1}".format(slowo, funkcja(slowo)))

# przestepne
print(nadchodzace_lp(4))

# rozmienianie

# zadanie1
print(funkcja_ackermanna(3, 3))

# zadanie2
kwota_wartosc = 1000
print(kwota_wartosc + odsetki(0.03, 12, kwota_wartosc))
for i in range(4):
    odsetki_wartosc = odsetki(0.03, 3, kwota_wartosc)
    kwota_wartosc += odsetki_wartosc
print(kwota_wartosc)

# zadanie3
print(suma_dzielnikow_zad3(6))

# zadanie4
pierwsza(2)

# zadanie5
print(dzielniki_pierwsze_zad5(150))

# zadanie6

# zadaniedomowe1
nominaly_w_portfelu = [20, 10, 5, 2, 1]
twoj_portfel = [8, 6, 2, 1, 0]
for kwota_do_zaplaty in range(8, 300, 37):
    wypisz_nominaly(kwota_do_zaplaty, rozmien(nominaly_w_portfelu, twoj_portfel, kwota_do_zaplaty))

# zadaniedomowe2
gra_w_zapalki()
