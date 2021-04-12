import math
def get_pins(observed):
    
    # Dictionary with observed digit as key and possible digits as value
    buttonDic = {
        0:[0,8],
        1:[1,2,4],
        2:[1,2,3,5],
        3:[2,3,6],
        4:[1,4,7,5],
        5:[2,4,5,6,8],
        6:[3,5,6,9],
        7:[4,7,8],
        8:[0,5,7,8,9],
        9:[6,8,9]
        }

    # Get list of lengths of value, i.e. how many possible other digits exist
    lengths = []
    for digit in observed:
        lengths.append(len(buttonDic[digit]))
    
    # Multiply the list of lengths to obtain total number of pin possibilities
    totalPossibilities = 1
    for x in lengths:
        totalPossibilities = totalPossibilities * x
    
    # Find out how many pins contain the specific possible digit
    # REWRITE, AS ONLY [0] IS USED
    digitOccurence = []
    temp = totalPossibilities
    for x in lengths:
        digitOccurence.append(math.floor(temp / x))
        temp = math.floor(temp / x)

    # Create list of sublists whereby the sublists are different pin possibilities
    # The sublists are filled with the possible digits of the first digit of the pin
    possiblePins = []
    firstpossibilities = buttonDic[observed[0]]
    for val in firstpossibilities:
        vallist = [val]
        for i in range(0, digitOccurence[0]):
            possiblePins.append(vallist)

    # Fill the sublists with the remaining digit possibilities
    for digit in observed[1:-1]:
        possibilities = buttonDic[digit]
        # Next one needs to take the nEnd instead of digitOccurence[0]
        counter = 0

        for val in possibilities:
            nStart = 0
            nEnd = math.floor(digitOccurence[0] / lengths[digit-1]) 
            nStart += counter
            nEnd += counter
            
            for x in range(0,lengths[digit-2]):
                for i in range(nStart, nEnd):
                    possiblePins[i-1].append(val)
                nStart += digitOccurence[digit-2]
                nEnd += digitOccurence[digit-2]
            nStart = 0
            nEnd = math.floor(digitOccurence[digit-2] / lengths[digit-1])
            counter += math.floor(digitOccurence[digit-2] / lengths[digit-1])




    return possiblePins

sample = [1,2,3]
example = get_pins(sample)
print(example)
