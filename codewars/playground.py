# CANNOT BE DELETED <-
# CAN BE DELETED

def array_diff(a, b):
    if not a:
        return a
    elif not b:
        return a
    else:
        copy = a
        print(copy)
        for z in b:
            counter = 0
            for x in a:   #  - counter
                print(x)
                if x == z:
                    copy.remove(x)
                    counter += 1
        print(copy)
        return copy