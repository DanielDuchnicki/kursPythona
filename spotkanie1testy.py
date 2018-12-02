from spotkanie1.zadanie1 import *
from spotkanie1.zadanie2 import *
from spotkanie1.zadanie3 import *
from spotkanie1.zadanie4 import *
from spotkanie1.zadanie5 import *
from spotkanie1.zadanie6 import *
from spotkanie1.zadanie7 import *
from spotkanie1.zadaniedomowe1 import *
from spotkanie1.zadaniedomowe2 import *


# zadanie1
kwadrat(6)
kwadrat2(6)

# zadanie2
piramida(5)

# zadanie3
print(silnia(3))
print(silnia(5))
for i in range(3, 6):
    print("{0}: {1:4d}".format(i, suma_silni(i)))

# zadanie4
print(podatek(85529))

# zadanie5
zakupy = [0.2, 0.5, 4.59, 6]
print(vat_faktura(zakupy))
print(vat_paragon(zakupy))

# zadanie6
print(suma_dzielnikow(6))

# zadanie7
klasyfikator("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

# zadaniedomowe1
for waga in range(50, 151, 5):
    print("Waga: " + str(waga) + "; Wzrost: 190; Twoje BMI: " + str(bmi(waga, 190)) +
          " - " + komentarz_bmi(bmi(waga, 190)))

# zadaniedomowe2
nominaly_w_portfelu = [20, 10, 5, 2, 1]
for kwota_do_zaplaty in range(8, 250, 37):
    wypisz_nominaly(kwota_do_zaplaty, znajdz_nominaly(nominaly_w_portfelu, kwota_do_zaplaty))
