def automorphic(n):
    s = str(n)
    sqr = str(n * n)

    nrev = s[len(s)::-1]
    sqrrev = sqr [len(sqr)::-1]

    if (nrev == sqrrev[0:len(nrev)]):
        return "Automorphic Number"
    else:
        return "Not Automorphic"
