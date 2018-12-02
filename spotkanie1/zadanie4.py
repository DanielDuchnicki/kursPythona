def podatek(kwota):
    wynik = 0
    if kwota <= 44490:
        wynik = 0.19 * kwota
    elif 44490 < kwota <= 85528:
        wynik = 0.19 * 44490 + 0.3 * (kwota-44490)
    elif kwota > 85528:
        wynik = 0.19 * 44490 + 0.3 * (85528-44490) + 0.4 * (kwota - 85528)

    return wynik


print(podatek(85529))
