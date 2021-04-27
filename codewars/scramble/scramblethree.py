# Third version - still too slow

def scramble(s1, s2):
    if len(s2) > len(s1):
        return False

    scrambledlist = list(s1)
    targetword = list(s2)

    for x in targetword:
        if x not in scrambledlist:
            return False
        else:
            scrambledlist.remove(x)
    
    return True


print(scramble('cndgmpnwpinjgbf', 'beihnoymavr'))