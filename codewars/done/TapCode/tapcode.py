# Tap code is a way to communicate using a series of taps and pauses for each letter.
# In this kata, we will use dots . for the taps and whitespaces for the pauses.
# The number of taps needed for each letter matches its coordinates in the following
# polybius square (note the c/k position). Then you "tap" the row, a pause, then the
# column. Each letter is separated from others with a pause too.
#
#

def tap_code_translation(text):
    translatedCharacters = []

    switcher = {
        'a' : '. .',
        'b' : '. ..',
        'c' : '. ...',
        'd' : '. ....',
        'e' : '. .....',
        'f' : '.. .',
        'g' : '.. ..',
        'h' : '.. ...',
        'i' : '.. ....',
        'j' : '.. .....',
        'k' : '. ...',
        'l' : '... .',
        'm' : '... ..',
        'n' : '... ...',
        'o' : '... ....',
        'p' : '... .....',
        'q' : '.... .',
        'r' : '.... ..',
        's' : '.... ...',
        't' : '.... ....',
        'u' : '.... .....',
        'v' : '..... .',
        'w' : '..... ..',
        'x' : '..... ...',
        'y' : '..... ....',
        'z' : '..... .....',
    }

    for i in text:
        translatedCharacters.append(switcher.get(i, "invalid character"))
    
    translatedString = ' '.join(translatedCharacters)
    print(translatedString)
    return(translatedString)
