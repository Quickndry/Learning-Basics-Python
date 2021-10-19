# 1.0
def valid_word(seq, word):
    print('Seq: ', seq, '\nword: ', word)

    cutouts = []
    target = ""

    for x in seq:
        cutout = word.replace(x, '')
        
        if len(cutout) == len(x):
            cutouts.append(word.replace(x,''))
        else:
            multiplier = len(cutout) / len(x)
            for i in range(multiplier):
                cutouts.append(x)
                
    for x in cutouts:
        target += x

    if len(target) == len(word):
        return True

    else:
        return False


# 2.0
def valid_word_prototype(seq, word):
    print("Seq: ", seq, "\nWord: ", word)
    lenct = 0

    for i in seq:
        ct = word.count(i)
        if ct == 1:
            lenct += len(i)
        elif ct > 1:
            lenct += len(i) * ct

    if lenct == len(word):
        return True
    else:
        return False

print(valid_word(['ab', 'a', 'bc'], 'abc'))



# 3.0
def valid_word(seq, word):
    print("Seq: ", seq, "\nWord: ", word)
    newWord = ''
    testlist = []
    if len(seq) == 0:
        return False
    for x in seq:
        if x in word:
            newWord += x * word.count(x)

    for x in newWord:
        if newWord.count(x) >= word.count(x):
            testlist.append("yes")
        else:
            testlist.append("no")
    for x in set(word):
        if newWord.count(x) >= word.count(x):
            testlist.append("yes")
        else:
            testlist.append("no")

    for x in testlist:
        if x == "no":
            return False

    return True
