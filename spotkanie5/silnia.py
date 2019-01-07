class NotIntError(Exception):
    pass

def silnia(n):
    if type(n) != type(1):
        raise NotIntError()
    if n < 2:
        return 1
    return n*(silnia(n-1))


#silnia("dwa")
