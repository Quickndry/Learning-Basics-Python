def count_bits(n):
    bitn = 0

    binnum = bin(n)[2:]
    sbinnum = str(binnum)

    lbinnum = [char for char in binnum]


    for i in lbinnum:

        if i == '1':

            bitn += 1

    return bitn
