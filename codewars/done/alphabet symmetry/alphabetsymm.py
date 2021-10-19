# Works
def solve(arr):
    # List of alphabet letters, to be converted into a dictionary with letter index as key
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphaDic = dict((i,a) for i,a in enumerate(alphabet))

    # Each element in array is split into a list, where key is index and value is letter
    # The dictionaries are collected in a list
    dicList = []
    for ele in arr:
        eleDic = dict((i,j) for i,j in enumerate(ele.lower()))
        dicList.append(eleDic)
    
    # Loop through dictionaries in list and through elementpair in dictionary
    # Compare the key of the element with the key of the same element in alphabet
    # dictionary. If its the same, at one to the counter. Before going to the next
    # element in list, append counter to list of endresults
    endResult = []
    for ele in dicList:
        counter = 0
        for k, letter in ele.items():
            if k == alphabet.index(letter):
                counter += 1
        endResult.append(counter)  
    
    return endResult
