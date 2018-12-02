def silnia(n):
    wynik = 1
    i = 1
    while i < n:
        i = i + 1
        wynik = wynik * i
    return wynik


def suma_silni(n):
    wynik = 0
    i = 1
    for i in range(1, n+1):
        wynik += silnia(i)
    return wynik


print(silnia(3))
print(silnia(5))

for i in range(3,6):
    print("{0}: {1:4d}".format(i, suma_silni(i)))
