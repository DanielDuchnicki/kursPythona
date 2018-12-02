def suma_w_portfelu(nominaly, portfel):
    kwota_w_portfelu = 0
    for nominal, ilosc in enumerate(portfel):
        kwota_w_portfelu += nominaly[nominal]*ilosc
    return kwota_w_portfelu


def rozmien(nominaly, portfel, kwota):
    kwota_poczatkowa = kwota
    wybrane_nominaly = {}
    kwota_w_portfelu = suma_w_portfelu(nominaly, portfel)

    if kwota_w_portfelu < kwota:
        return wybrane_nominaly

    for index, item in enumerate(nominaly):
        if portfel[index] == 0:
            continue
        liczba_nominalow = kwota // item
        wybrane_nominaly[item] = min(portfel[index], liczba_nominalow)
        kwota -= item * wybrane_nominaly[item]

    if kwota != 0:
        kwota = kwota_poczatkowa + 1
        wybrane_nominaly = rozmien(nominaly, portfel, kwota)

    return wybrane_nominaly


def wypisz_nominaly(kwota, wybrane_nominaly):
    if not wybrane_nominaly:
        print("Masz do zapłaty " + str(kwota) + " zł ale niestety nie masz wystarczająco dużo pieniędzy w portfelu!")
    else:
        print("Aby zapłacić " + str(kwota) + " zł musisz wyjąć z portfela: ")
        for key in wybrane_nominaly:
            if key > 5:
                print("- " + str(wybrane_nominaly[key]) + " razy banknot " + str(key) + "-złotowy")
            else:
                print("- " + str(wybrane_nominaly[key]) + " razy monetę " + str(key) + "-złotową")
