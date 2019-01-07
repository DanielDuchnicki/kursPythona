from urllib.request import *
from collections import defaultdict
import re


def statystyka(plik):
    slownik = defaultdict(int)
    plik_do_czytania = urlopen(plik)

    for linia in plik_do_czytania:
        linia_zdekodowana = linia.decode("utf-8").lower()
        for slowo in re.split(' |!|\\?|\.|;|:|, |,|\*|\n|/|—|\r', linia_zdekodowana):
            if not re.match(r'^\s*$', slowo):
                slownik[slowo] += 1

    slownik_posortowany_po_wartosciach = {}
    for slowo in sorted(slownik, key=slownik.get, reverse=True):
        slownik_posortowany_po_wartosciach[slowo] = slownik[slowo]

    return slownik_posortowany_po_wartosciach


def porownaj_statystyki(statystyka1, statystyka2):
    for klucz_stat1 in statystyka1:
        for klucz_stat2 in statystyka2:
            if klucz_stat1 == klucz_stat2:
                print("Słowo '{0}' występuje w obu tekstach. Różnica: {1}".
                      format(klucz_stat1, abs(statystyka1[klucz_stat1]-statystyka2[klucz_stat2])))

    for klucz_stat1 in statystyka1:
        if klucz_stat1 not in statystyka2:
            print("Słowo '{0}' występuje tylko w tekście nr 1.".format(klucz_stat1))

    for klucz_stat2 in statystyka2:
        if klucz_stat2 not in statystyka1:
            print("Słowo '{0}' występuje tylko w tekście nr 2.".format(klucz_stat2))


makbet = "https://wolnelektury.pl/media/book/txt/makbet.txt"
wiele_halasu_o_nic = "https://wolnelektury.pl/media/book/txt/shakespeare-wiele-halasu-o-nic.txt"

slowa_makbet = statystyka(makbet)
slowa_wiele_halasu_o_nic = statystyka(wiele_halasu_o_nic)
print(slowa_makbet)
print(slowa_wiele_halasu_o_nic)
porownaj_statystyki(slowa_makbet, slowa_wiele_halasu_o_nic)
