# current version
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

# Prototype
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
    

     



    

    



