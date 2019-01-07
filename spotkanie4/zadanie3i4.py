class NotStringError(Exception):
    pass


class NotIntError(Exception):
    pass


class Wyrazenie:
    pass


class Zmienna(Wyrazenie):

    def __init__(self, nazwa):
        if not isinstance(nazwa, str):
            raise NotStringError
        self.nazwa = nazwa

    def __str__(self):
        return self.nazwa

    def oblicz(self, stan):
        return stan[self.nazwa]


class Stala(Wyrazenie):

    def __init__(self, wartosc):
        if not isinstance(wartosc, int):
            raise NotIntError
        self.wartosc = wartosc

    def __str__(self):
        return str(self.wartosc)

    def oblicz(self):
        return self.wartosc


class Dodawanie(Wyrazenie):

    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " + " + str(self.prawy)

    def oblicz(self, stan):
        if type(self.lewy) is Stala and type(self.prawy) is Stala:
            return self.lewy.oblicz() + self.prawy.oblicz()
        elif type(self.prawy) is Stala:
            return self.lewy.oblicz(stan) + self.prawy.oblicz()
        elif type(self.lewy) is Stala:
            return self.lewy.oblicz() + self.prawy.oblicz(stan)
        else:
            return self.lewy.oblicz(stan) + self.prawy.oblicz(stan)

    def uprosc(self):
        if (type(self.lewy) is Stala and type(self.prawy) is Stala) or \
                (self.lewy.oblicz() == 0 or self.prawy.oblicz() == 0):
            return Stala(self.lewy.oblicz() + self.prawy.oblicz())


class Mnozenie(Wyrazenie):

    def __init__(self, lewy, prawy):
        self.lewy = lewy
        self.prawy = prawy

    def __str__(self):
        return str(self.lewy) + " * " + str(self.prawy)

    def oblicz(self, stan):
        if type(self.lewy) is Stala and type(self.prawy) is Stala:
            return self.lewy.oblicz() * self.prawy.oblicz()
        elif type(self.prawy) is Stala:
            return self.lewy.oblicz(stan) * self.prawy.oblicz()
        elif type(self.lewy) is Stala:
            return self.lewy.oblicz() * self.prawy.oblicz(stan)
        else:
            return self.lewy.oblicz(stan) * self.prawy.oblicz(stan)

    def uprosc(self):
        if (type(self.lewy) is Stala and type(self.prawy) is Stala) or \
                (self.lewy.oblicz() == 1 or self.prawy.oblicz() == 1):
            return Stala(self.lewy.oblicz() * self.prawy.oblicz())


# aktualny_stan = {'x': 1, 'y': 3, 'z': 3}
#
# wyrazenie = Dodawanie(Dodawanie(Zmienna("x"), Zmienna("y")), Zmienna("z"))
# print(wyrazenie)
# print(wyrazenie.oblicz(aktualny_stan))
#
# wyrazenie2 = Mnozenie(Mnozenie(Zmienna("x"), Zmienna("y")), Zmienna("z"))
# print(wyrazenie2)
# print(wyrazenie2.oblicz(aktualny_stan))
#
# wyrazenie3 = Dodawanie(Dodawanie(Stala(2), Zmienna("y")), Zmienna("z"))
# print(wyrazenie3)
# print(wyrazenie3.oblicz(aktualny_stan))
#
# wyrazenie4 = Mnozenie(Mnozenie(Stala(2), Zmienna("y")), Stala(2))
# print(wyrazenie4)
# print(wyrazenie4.oblicz(aktualny_stan))
#
# wyrazenie5 = Dodawanie(Stala(0), Stala(6))
# nowe = wyrazenie5.uprosc()
# print("nowe = " + str(nowe))
#
# wyrazenie6 = Mnozenie(Stala(1), Stala(6))
# nowe2 = wyrazenie6.uprosc()
# print("nowe2 = " + str(nowe2))
#
# wyrazenie7 = Dodawanie(nowe, nowe2)
# print(wyrazenie7)
# print(wyrazenie7.oblicz(aktualny_stan))
