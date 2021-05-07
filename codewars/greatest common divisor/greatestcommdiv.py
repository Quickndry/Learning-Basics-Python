def mygcd(x, y):
    if x > y:
        while x > y:
            x = x - y
        return x
    elif y > x:
        while y > x:
            y = y - x
        return y
    else:
        return 1