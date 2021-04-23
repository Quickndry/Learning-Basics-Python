
def scramble(s1, s2):
    scrambledlist = [x for x in s1]
    targetword = [x for x in s2]

    missingletters = [x for x in targetword if x not in scrambledlist]

    if len(missingletters) > 0:
        return False
    else:
        return True

print(scramble('cndgmpnwpinjgbf', 'beihnoymavr'))