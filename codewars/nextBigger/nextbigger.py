# Works but is too slow.
from itertools import permutations

def next_bigger(n):
    combinations = [''.join(p) for p in permutations(str(n))]
    possibilities = [int(combi) for combi in combinations if int(combi) > n]

    if len(possibilities) > 0:
        return(int(min(possibilities)))
    else:
        return(-1)

print(next_bigger(513))