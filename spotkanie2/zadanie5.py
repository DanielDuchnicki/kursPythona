def suma_dzielnikow(n):
    suma_dzielnikow_liczby_n = [item for item in range(1, n) if n % item == 0]
    return suma_dzielnikow_liczby_n


def pierwsza_zad5(n):
    suma_dzielnikow_liczby_n = [item for item in range(1, n) if n % item == 0]
    if len(suma_dzielnikow_liczby_n) == 1:
        return True
    else:
        return False


def dzielniki_pierwsze_zad5(n):
    suma_dzielnikow_liczby_n = suma_dzielnikow(n)
    for item in suma_dzielnikow_liczby_n[:]:
        if not pierwsza_zad5(item):
            suma_dzielnikow_liczby_n.remove(item)
    return suma_dzielnikow_liczby_n


def doskonala(n):
    pass
