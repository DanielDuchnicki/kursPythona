def klasyfikator(napis):
    for slowo in napis.split():
        if len(slowo) <= 5:
            print("+ " + slowo)
        else:
            print("- " + slowo)
