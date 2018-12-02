def znajdz_nominaly(nominaly, kwota):
    wybrane_nominaly = {}
    for item in nominaly:
        reszta_z_dzielenia = kwota % item
        if reszta_z_dzielenia == 0:
            wybrane_nominaly[item] = kwota // item
            break
        else:
            if ((kwota - reszta_z_dzielenia) / item) != 0:
                wybrane_nominaly[item] = (kwota - reszta_z_dzielenia) // item
                kwota = reszta_z_dzielenia
    return wybrane_nominaly


def wypisz_nominaly(kwota, wybrane_nominaly):
    print("Aby zapłacić " + str(kwota) + " zł musisz wyjąć z portfela: ")
    for key in wybrane_nominaly:
        if key > 5:
            print("- " + str(wybrane_nominaly[key]) + " razy banknot " + str(key) + "-złotowy")
        else:
            print("- " + str(wybrane_nominaly[key]) + " razy monetę " + str(key) + "-złotową")
