import random
from spotkanie2.zadaniedomowe2_interakcja import podaj_ruch


def gra_w_zapalki():
    liczba_zapalek = random.randint(7, 30)
    print("Liczba zapałek: " + str(liczba_zapalek))
    while liczba_zapalek > 0:
        ruch = int(podaj_ruch())
        liczba_zapalek -= ruch
        if liczba_zapalek <= 0:
            print("Przegrałeś!")
            break
        print("Liczba zapałek: " + str(liczba_zapalek))
        ruch = ruch_komputera(liczba_zapalek)
        print("Ruch przeciwnika: " + str(ruch))
        liczba_zapalek -= ruch
        if liczba_zapalek <= 0:
            print("Gratulacje! Wygrałeś!")
            break
        print("Liczba zapałek: " + str(liczba_zapalek))


def ruch_komputera(stan_gry):
    ruch = min(stan_gry, random.randint(1, 3))
    return ruch


def ruch_komputera2(stan_gry):
    """To jest prosta strategia"""
    ruch = max(1, min(3, stan_gry - 1))
    return ruch

gra_w_zapalki()
