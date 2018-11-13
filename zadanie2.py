def piramida(n):
    for i in range(n):
        print(" " * (n-i) + "#" * (2*i-1))


piramida(5)
