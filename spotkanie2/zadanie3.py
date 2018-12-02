def suma_dzielnikow(n):
    suma_dzielnikow_liczby_n = [item for item in range(1, n) if n % item == 0]
    return suma_dzielnikow_liczby_n


print(suma_dzielnikow(6))
