def odsetki(oproc, czas, kwota):
    return kwota*oproc*czas/12


kwota_wartosc = 1000
print(kwota_wartosc + odsetki(0.03, 12, kwota_wartosc))

for i in range(4):
    odsetki_wartosc = odsetki(0.03, 3, kwota_wartosc)
    kwota_wartosc += odsetki_wartosc

print(kwota_wartosc)
