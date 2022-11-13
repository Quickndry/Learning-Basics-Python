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