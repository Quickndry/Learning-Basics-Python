from string import ascii_lowercase as alc
from string import ascii_uppercase as auc

# Part 1 -----------------------------------------------------------------------

def sort_rucksack(inputfile):
    file = open(inputfile, 'r')
    lines = file.readlines()
    sum = 0
    for line in lines:
        line_adapted = line.replace("\n", "")
        halve = int(len(line_adapted) / 2)
        first_halve = line_adapted[0:halve]
        second_halve = line_adapted[halve:]
        
        double_letters = []

        for buchstabe in first_halve:
            if buchstabe in second_halve and buchstabe not in double_letters:
                double_letters.append(buchstabe)
                try:
                    sum += 1 + alc.index(buchstabe)
                except ValueError:
                    pass
                try:
                    sum += 27 + auc.index(buchstabe)
                except ValueError:
                    pass
    return sum

# Part 2 ------------------------------------------------------------------------

def find_badge(inputfile):
    a_combined = alc + auc
    sum = 0
    file = open(inputfile, 'r')
    lines = file.readlines()
    listlength = len(lines) + 1

    first_pos = 0
    last_pos = []
    for digit in range(3, listlength, 3):
        last_pos.append(digit)
    for pos in last_pos:
        current = lines[first_pos:pos]
        sanitized_line = current[0].replace("\n", "")
        double_letters = []
        for letter in sanitized_line:
            if letter in current[1] and letter in current[2] and letter not in double_letters:
                sum += 1 + a_combined.index(letter)
                double_letters.append(letter)
        first_pos = pos
    return sum

print(find_badge("input.txt"))