# Works and is quick enough

def next_bigger(n):
    # Checker to ensure that a bigger number was found
    checker = False

    # Loop through index of n in reverse, comparing each number with the 
    # upcoming one. If it is bigger then the next, the n-string is split
    # into individual components, the checker checked and the loop broken
    for i in range(len(str(n)), 0, -1):

        # Try-Except as index can fall out of range
        try:
            if int(str(n)[i]) > int(str(n)[i-1]):
                firstHalve = str(n)[:i-1]
                targetDigit = str(n)[i]
                controlDigit = str(n)[i-1]
                secondHalve = str(n)[i-1] + str(n)[i+1:]
                checker = True
                break
        except:
            pass

    # Making sure that there is a bigger number, if not, return -1
    if checker == False:
        return -1

    # Loop through the second halve of the n-string, to compare numbers with 
    # the number switched earlier, ensuring that it is bigger than the original
    # yet the smallest number possible
    halveList = [x for x in secondHalve]

    emptyList = []

    for i in range(len(halveList)):
        if int(halveList[i]) < int(targetDigit) and int(halveList[i]) > int(controlDigit):
            emptyList.append(int(halveList[i]))
    
    if len(emptyList) > 0:
        controlDigit = min(emptyList)
        halveList[halveList.index(str(controlDigit))] = targetDigit
        targetDigit = controlDigit

    # Convert the halve list back into a string and add the original first
    # halve with the reworked second halve
    reworkedHalve = ""
    for x in sorted(halveList):
        reworkedHalve += str(x)
    
    finalString = firstHalve + str(targetDigit) + reworkedHalve

    return int(finalString)

    
print(next_bigger(35624473238766))
