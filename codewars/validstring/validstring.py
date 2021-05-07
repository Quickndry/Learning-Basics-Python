# current version
def valid_word(seq, word):
    newWord = ''
    testWord = ''
    for x in seq:
        if x in word:
            newWord += x

    for x in set(newWord):
        if newWord.count(x) > word.count(x):
            testword += x
    
    if len(testWord) <= len(set(newWord)):
        return True
    else:
        return False
        

    

     



    

    



