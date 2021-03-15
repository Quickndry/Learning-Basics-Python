# function to convert string into list, translate elements into a new list and combine
# to return the translated sentence
def pig_it(text):

    stringEnglish = str(text)

    emptyList = stringEnglish.split(" ")
    
    newList = [x + "f" if x not in ["!", ".", "?"] else x for x in emptyList]
    
    translatedList = [x[1:-1] + x[0] + "ay" if x not in ["!", ".", "?"] else x for x in newList]
    
    print(newList)
    print(translatedList)
    
    stringOutput = " ".join(translatedList)

    return(stringOutput)