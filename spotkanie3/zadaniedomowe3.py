def wczytaj_plik_notowan(plik_notowan):
    notowania = {}
    with open(plik_notowan, 'r') as plik:
        for line in plik:
            spolka = line.split(',')
            notowania[spolka[0]] = spolka[1]

    return notowania


def policz_wartosc_spolek(akcje, notowania):
    twoj_portfel = {}
    for spolka in akcje:
        if spolka in notowania:
            twoj_portfel[spolka] = (akcje[spolka], float(akcje[spolka]) * float(notowania[spolka]))

    return twoj_portfel


def policz_wartosc_portfela(twoj_portfel):
    wartosc_calego_portfela = 0
    for spolka in twoj_portfel:
        wartosc_calego_portfela += twoj_portfel[spolka][1]

    return wartosc_calego_portfela


def wyswietl_portfel(twoj_portfel):
    wartosc_portfela = policz_wartosc_portfela(twoj_portfel)
    print("Twoje spółki:\n")
    for spolka in twoj_portfel:
        print("{0}: ilość akcji: {1}, wartość: {2} zł".format(spolka, twoj_portfel[spolka][0], twoj_portfel[spolka][1]))
    print("\nWartość całego portfela: {0} zł".format(wartosc_portfela))


portfel = {"Energa SA": 500, "PGE SA": 400, "PGNiG SA": 1000, "Tauron Polska Energia SA": 1000,
           "Trakcja PRKiI SA": 1000, "Ursus SA": 1000}
plik_z_notowaniami = 'moneypl-1544518926335.csv'

portfel_z_wartosciami = policz_wartosc_spolek(portfel, wczytaj_plik_notowan(plik_z_notowaniami))
wyswietl_portfel(portfel_z_wartosciami)
