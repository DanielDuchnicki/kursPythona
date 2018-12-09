from wskaznikbmi import *


class Osoba:

    def __init__(self, imie, nazwisko, waga, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost

    def __str__(self):
        return self.__class__.__name__ + ": " + self.imie + " " + self.nazwisko

    def wskaznik_bmi(self):
        wskaznik = bmi(self.waga, self.wzrost)
        return "BMI: " + str(wskaznik) + " - " + komentarz_bmi(wskaznik)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja, waga, wzrost):
        Osoba.__init__(self, imie, nazwisko, waga, wzrost)
        self.pensja = pensja

    def wyplata(self):
        return self.pensja * 1.2


class Kierownik(Pracownik):
    """
    def __init__(self, imie, nazwisko, pensja):
        Pracownik.__init__(self, imie, nazwisko, pensja)
    """

    def wyplata(self):
        return super().wyplata() + 1200.0


o = Osoba("Jan",  "Kowalski", 80, 190)
print(o)
print(o.wskaznik_bmi())

p = Pracownik("Jan", "Nowak", 2250, 80, 190)
print("{0} wypłata {1}".format(p, p.wyplata()))
print(p.wskaznik_bmi())

k = Kierownik("Anna", "", 5000, 50, 160)
print(k)
print(k.wskaznik_bmi())
