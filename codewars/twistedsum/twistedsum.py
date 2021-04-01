def compute_sum(n):
    sumlist = []

    digitlist = [x for x in range(0, n+1)]

    for i in digitlist:
        if len(str(i)) > 1:
            splitlist = list(str(i))

            for ele in splitlist:
                sumlist.append(int(ele))

        else:
            sumlist.append(i)
    
    total = sum(sumlist)
    return total
