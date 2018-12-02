def wersja1(slowo):
    for i in range(len(slowo)):
        if slowo[i] != slowo[-i - 1]:
            return False
    return True


def wersja2(slowo):
    return slowo == slowo[::-1]
