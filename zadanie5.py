def vat_faktura(lista):
    suma = 0
    for element in lista:
        suma = suma + element
    vat = round(0.23*suma, 2)
    return vat


def vat_paragon(lista):
    vat = 0
    suma_vat = 0
    for element in lista:
        vat = round(0.23*element, 2)
        suma_vat += vat
    return suma_vat


zakupy = [0.2, 0.5, 4.59, 6]
print(vat_faktura(zakupy))
print(vat_paragon(zakupy))
