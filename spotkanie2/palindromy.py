def wersja1(slowo):
    for i in range(len(slowo)):
        if slowo[i] != slowo[-i - 1]:
            return False
    return True


def wersja2(slowo):
    return slowo == slowo[::-1]


dane = ['kajak', 'kobyłamamałybok', 'palindrom', [1, 2, 1], [2, 3]]
wersje = [wersja1, wersja2]
for funkcja in wersje:
    for slowo in dane:
        print("{0}: {1}".format(slowo, funkcja(slowo)))
