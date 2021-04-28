

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
    

     



    

    



