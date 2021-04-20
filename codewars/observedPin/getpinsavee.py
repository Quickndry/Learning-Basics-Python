import math
def get_pins(observed):

    # Turn string input into list
    placeholderList = list(observed)
    observedList = []
    for i in placeholderList:
        observedList.append(int(i))
    print("observed: ", observedList)

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
    for digit in observedList:
        lengths.append(len(buttonDic[digit]))

    print("Lengths: ", lengths)

    # Multiply the list of lengths to obtain total number of pin possibilities
    totalPossibilities = 1
    for x in lengths:
        totalPossibilities = totalPossibilities * x
    
    print("Total Possibilities: ", totalPossibilities)
    
    # Find out how many pins contain the specific possible digit
    digitOccurence = []
    temp = totalPossibilities
    for x in lengths:
        digitOccurence.append(math.floor(temp / x))
        temp = math.floor(temp / x)

    # Create list of loops
    numberOfLoops =[1]
    for digit in observedList:
        placeholder = numberOfLoops[observedList.index(digit)] * lengths[observedList.index(digit)]
        numberOfLoops.append(placeholder)
    numberOfLoops = numberOfLoops[:len(observedList)]

    print("\nDigit Occurence: ", digitOccurence, "\nNumber of loops: ", numberOfLoops)

    possiblePins = [[] for i in range(0, totalPossibilities)]

    print("First digit list: ", possiblePins)
    print("\nThese are the object IDs of the first to sublists:\n", id(possiblePins[0]), "\n", id(possiblePins[1]))

    # Fill the sublists with the remaining digit possibilities
    for digit in observedList:
        possibilities = buttonDic[digit]
        # Next one needs to take the nEnd instead of digitOccurence[0]
        scounter = 0 # To find the startindex when looping through values

        print("These for Digit: ", digit, "\nThis are its possibilities: ", possibilities)

        for val in possibilities:
            counter = 0 # To find the startindex when looping through range of possibilities
            nStart = 0
            nEnd = digitOccurence[observedList.index(digit)] 
            nStart += scounter
            nEnd += scounter

            print("\nThe following is for value: ", val)
            
            for x in range(0,numberOfLoops[observedList.index(digit)]):
                nStart += counter
                nEnd += counter 

                print("Currently in loop: ", x + 1)
                print("Start: ", nStart, "\nEnd: ", nEnd)

                for i in range(nStart, nEnd):
                    possiblePins[i].append(val)
                
                counter = digitOccurence[observedList.index(digit)-1]

            scounter += digitOccurence[observedList.index(digit)]
            # Problem lies with the fact that index() only finds first occurence
            # For every loop through a digit, delete previous digit and adapt
            # all other called lists (i.e. remove previous value)

    finalResult = []
    for pin in possiblePins:
        resultPlaceholder = ''.join(map(str, pin))
        finalResult.append(resultPlaceholder)

    return finalResult

sample = "11"
example = get_pins(sample)
print(example)
