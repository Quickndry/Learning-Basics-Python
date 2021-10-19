# works fine
from collections import OrderedDict

def the_janitor(word):
    rword = word[::-1]
    letters = OrderedDict((letter, None) for letter in word).keys()
    alphabet = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }


    for letter in letters:
        firstindex = word.find(letter)
        secondindex = len(word) - rword.find(letter)
        swipe = secondindex - firstindex
        alphabet[letter] = swipe
    
    swipesneeded = list(alphabet.values())

    
    return swipesneeded
