def podaj_ruch():
    ruch = 0
    while ruch <= 0 or ruch > 3:
        ruch = int(input("Podaj swój ruch: "))
        if ruch <= 0 or ruch > 3:
            print("Musiz podać wartość między 1 a 3!")
    return ruch
