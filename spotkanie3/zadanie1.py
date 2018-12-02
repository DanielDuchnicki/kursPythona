def zakupy(cennik, lista):
    suma_za_zakupy = 0
    for klucz in lista:
        cena = lista[klucz]*cennik[klucz]
        vat = round(0.23*cena, 2)
        suma_za_zakupy += cena + vat
    return suma_za_zakupy


cennik_w_sklepie = {
    'kawa': 14.99,
    'pomarańcze': 3.49,
    'olej': 4.99
}

twoja_lista = {'olej': 2, 'kawa': 1}

print(zakupy(cennik_w_sklepie, twoja_lista))
