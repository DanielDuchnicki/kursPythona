def pierwsza(n):
    suma_dzielnikow_liczby_n = []
    for item in range(1, n):
        if n % item == 0:
            suma_dzielnikow_liczby_n.append(item)
    if len(suma_dzielnikow_liczby_n) == 1:
        return print("Liczba " + str(n) + " jest liczbą pierwszą.")
    else:
        return print("Liczba " + str(n) + " NIE jest liczbą pierwszą.")
