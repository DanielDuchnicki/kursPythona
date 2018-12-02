def zakupy(cennik, lista):
    suma_za_zakupy = 0
    for klucz in lista:
        cena = lista[klucz]*cennik[klucz]
        vat = round(0.23*cena, 2)
        suma_za_zakupy += cena + vat
    return suma_za_zakupy
