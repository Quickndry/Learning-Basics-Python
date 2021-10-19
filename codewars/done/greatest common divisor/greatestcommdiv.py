# Works fine
def mygcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        elif y > x:
            y = y - x
        if x < 0 or y < 0:
            return 1
    return x
        
