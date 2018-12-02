from spotkanie3.testpakietu import *
from spotkanie3.zadanie1 import *
from spotkanie3.zadanie2 import *
from spotkanie3.zadanie3 import *

# testpakietu
print(modul1.foo())
print(foo())

# zadanie1
cennik_w_sklepie = {
    'kawa': 14.99,
    'pomarańcze': 3.49,
    'olej': 4.99
}
twoja_lista = {'olej': 2, 'kawa': 1}

print(zakupy(cennik_w_sklepie, twoja_lista))

# zadanie 2
files_dictionary = {}
przegladanie('.', files_dictionary)
print(files_dictionary)
znajdz_pliki_o_tym_samym_rozmiarze(files_dictionary)

# zadanie 3
wyniki = statystyka("spotkanie3/tekst.txt")
print("Liczba zdań: " + str(wyniki[0]))
print("Liczba słów: " + str(wyniki[1]))
print("Liczba znaków: " + str(wyniki[2]))
