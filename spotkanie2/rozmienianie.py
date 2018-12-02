def rozmien(portfel, kwota):
    wynik = [0] * len(portfel)
    zostalo = kwota
    for nominal in reversed(range(len(portfel))):
        if zostalo <= 0:
            break
        if portfel[nominal] == 0:
            continue

        liczba_nominalow = min(zostalo // nominal, portfel[nominal])
        zostalo -= liczba_nominalow * nominal
        portfel[nominal] -= liczba_nominalow
        wynik[nominal] = liczba_nominalow

    while zostalo > 0:
        if portfel == [0] * len(portfel):
            break
        for nominal in range(len(portfel)):
            if portfel[nominal] > 0:
                zostalo -= nominal
                portfel[nominal] -= 1
                wynik[nominal] += 1

    return wynik

