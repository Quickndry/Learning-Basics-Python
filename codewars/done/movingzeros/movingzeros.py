# Works and is fast enough
def move_zeros(array):
    indexLst = []
    zeroCount = 0
    for i, v in enumerate(array):
        if v == 0:
            indexLst.append(i)
            zeroCount += 1
    for i in indexLst[-1::-1]:
        del array[i]
    for i in range(zeroCount):
        array.append(0)
    return array