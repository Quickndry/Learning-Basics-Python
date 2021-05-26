def comparelists(a,b):
    newlist = [] 

    for i in b:
        newlist.append(i)
        counter = 0
        for x in a:
            if i == x:
                counter += 1
        newlist.append(counter)
    return newlist
