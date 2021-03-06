class NotStringError(Exception):
    pass


def statystyka(nazwa_pliku):
    if not isinstance(nazwa_pliku, str):
        raise NotStringError
    liczba_zdan_slow_znakow_list = [0, 0, 0]
    with open(nazwa_pliku, 'r') as fh:
        tekst = fh.read()
        liczba_zdan_slow_znakow_list[2] = len(tekst)
        slowa = tekst.split(" ")
        liczba_zdan_slow_znakow_list[1] = len(slowa)
        for slowo in slowa:
            if "." in slowo or "!" in slowo or "?" in slowo:
                liczba_zdan_slow_znakow_list[0] += 1

    return liczba_zdan_slow_znakow_list


statystyka("123")
