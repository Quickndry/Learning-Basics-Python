def scramble(s1, s2):
    scrambledlist = list(s1)
    targetword = list(s2)
    target = [x if x in scrambledlist else '1' for x in targetword]

    if '1' in target:
        return False
    else:
        return True