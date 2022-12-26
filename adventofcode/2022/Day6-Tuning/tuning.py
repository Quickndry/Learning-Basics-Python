# four digits as list, turn to set, if length the same, return 
# 
# 
# PART ONE
def tuning(inputfile):
    with open(inputfile, 'r') as file:
        f_string = file.read()

    for ind in range(len(f_string)):
        current = [x for x in f_string[ind:ind+4]]
        c_set = set(current)
        print("Current: ", current, "\nSet: ", c_set)

        if len(current) == len(c_set):
            return ind+4

# PART TWO
def message(inputfile):
    with open(inputfile, 'r') as file:
        f_string = file.read()

    for ind in range(len(f_string)):
        current = [x for x in f_string[ind:ind+14]]
        c_set = set(current)

        if len(current) == len(c_set):
            return ind+14

print(message("input.txt"))