# Third version - still too slow

def scramble(s1, s2):
    scrambledlist = list(s1)
    targetword = list(s2)

    for x in targetword:
        if x not in scrambledlist:
            return False
        else:
            scrambledList.remove(x)
            pass
    
    return True


print(scramble('cndgmpnwpinjgbf', 'beihnoymavr'))