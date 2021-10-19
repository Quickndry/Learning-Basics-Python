# Fifth version - works fine

from collections import Counter

def scramble(s1, s2):
    scrambledlist = Counter(s1)
    targetword = Counter(s2)
    checker = targetword - scrambledlist

    if len(checker) == 0:
        return True
    else:
        return False