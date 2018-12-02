def funkcja_ackermanna(m, n):
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return funkcja_ackermanna(m-1, 1)
    if m > 0 and n > 0:
        return funkcja_ackermanna(m-1, funkcja_ackermanna(m, n-1))


print(funkcja_ackermanna(3, 3))
