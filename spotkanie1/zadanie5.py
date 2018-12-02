def vat_faktura(lista):
    suma = 0
    for element in lista:
        suma = suma + element
    vat = round(0.23*suma, 2)
    return vat


def vat_paragon(lista):
    suma_vat = 0
    for element in lista:
        vat = round(0.23*element, 2)
        suma_vat += vat
    return suma_vat
