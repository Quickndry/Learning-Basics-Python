def next_bigger(n):

    digits = [x for x in str(n)]

    counter = len(digits)

    

    while counter > 0:

        safecopy = digits

        safecopy.insert(counter - 2, safecopy.pop(counter - 1))

        safecopystring = ''.join([str(elem) for elem in safecopy])

        if int(safecopystring) > n:

            return int(safecopystring)

        else:

            pass

        counter -= 1

    return(-1)
