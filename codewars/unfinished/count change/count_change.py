# Steps to find all possible combinations of coins that add up to the given change:
# Create a recursive function that loops through coins and substracts each from the change.
# If the change is 0, add combination to a combination list, so that duplicates can be
# filtered out. If change is negative, combination is discounted. If change is positive,
# function recurses over itself. 
# Function returns the combinations collected and adds them to a final combination list
# before checking the list for duplicates and returning the list without them. 
# A second function returns the number of combinations.

# Ineffeciencies:
# Memory -> Duplicates are all recorded in a list and only checked afterwards.
# All combinations are calculated manually.

import itertools

def find_combo(change, coins, combination, combinations):
    for coin in coins:
        change_leftover = change - coin
        print("Change", change ,"Coin", coin, "leftover", change_leftover)
        combination_next = combination.copy()
        combination_next.append(coin)
        print("Combinations: ", combinations, "n\Combination: ", combination_next)
        if change_leftover == 0:
            combination_next.sort()
            print("Combination sorted: ", combination_next)
            if combination_next not in combinations:
                combinations.append(combination_next)
        elif change_leftover > 0:
            combinations_other = find_combo(change_leftover, coins, combination_next, combinations)
        elif change_leftover < 0:
            pass
    if "combinations_other" in locals():
        combinations.extend(combinations_other)
    return combinations


def count_change(change, coins):
    combination_possibilities = find_combo(change, coins, [], [])
    combination_possibilities.sort()
    return len(list(combination_possibilities for combination_possibilities,_ in itertools.groupby(combination_possibilities)))