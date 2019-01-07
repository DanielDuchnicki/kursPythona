class NotStringError(Exception):
    pass


def klasyfikator(napis):
    if not isinstance(napis, str):
        raise NotStringError
    for slowo in napis.split():
        if len(slowo) <= 5:
            print("+ " + slowo)
        else:
            print("- " + slowo)


#klasyfikator(123)
