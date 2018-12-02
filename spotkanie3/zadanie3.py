def statystyka(nazwa_pliku):
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


wyniki = statystyka("tekst.txt")
print("Liczba zdań: " + str(wyniki[0]))
print("Liczba słów: " + str(wyniki[1]))
print("Liczba znaków: " + str(wyniki[2]))
