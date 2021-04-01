# CANNOT BE DELETED <-
# CAN BE DELETED




def one(x):
    lst = x

    if lst:
        if lst[0] == "x":
            return(1 * lst[1])
        elif lst[0] == "+":
            return(1 + lst[1])
        elif lst[0] == "-":
            return(1 - lst[1])
        else:
            return(1 / lst[1])
    else:
        return(1)
        
def two(x):
    lst = x
    if lst:
        if lst[0] == "x":
            return(2 * lst[1])
        elif lst[0] == "+":
            return(2 + lst[1])
        elif lst[0] == "-":
            return(2 - lst[1])
        else:
            return(2 / lst[1])
    else:
        return(2)


def plus(x):
    plus = []
    plus.append('+')
    plus.append(x)
    return(plus)

def minus(x): 
    minus = []
    minus.append('-')
    minus.append(x)
    return(minus)

def times(x): 
    times = []
    times.append('x')
    times.append(x)
    return(times)

def divided_by(x): 
    divided = []
    divided.append('/')
    divided.append(x)
    return(divided)

print(one(times(two)))
print(two(minus(one)))



    if n > 9:
        tenners = floor(n/10)
        decis = (n/10) - tenners
