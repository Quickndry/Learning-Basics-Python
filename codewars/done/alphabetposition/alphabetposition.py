import re 
def alphabet_position(text):
    only_letters = re.sub(r'[^a-zA-Z]', '', text)
    translation = []
    for letter in only_letters:
        if letter.isupper():
            translation.append(str(ord(letter) - 64))
        else:
            translation.append(str(ord(letter) - 96))
    final = ' '.join(translation)
    return(final)