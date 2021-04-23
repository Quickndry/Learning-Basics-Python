# Passes Tests but times out later on - too slow.

def scramble(s1, s2):
    scrambledlist = [x for x in s1]
    targetword = [x for x in s2]
    missingnumbers = 0

    safecopytargetword = targetword.copy()
    
    for letter in targetword:
        print("\nLetter: ", letter)

        if letter in scrambledlist:
            safecopytargetword.remove(letter)
            scrambledlist.remove(letter)
            print("\nWord: ", safecopytargetword, "\nScrambled: ", scrambledlist)
            
        else:
            missingnumbers += 1
            print("\nMissing Numbers: ", missingnumbers)
    
    if missingnumbers > 0:
        return False
    else:
        return True


print(scramble('cndgmpnwpinjgbf', 'beihnoymavr'))