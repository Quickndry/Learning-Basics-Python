import math

def nbr_of_laps(x, y):
    lowestMultiple = abs(x*y) // math.gcd(x, y)
    rslt = tuple((lowestMultiple / x, lowestMultiple / y))
    return rslt