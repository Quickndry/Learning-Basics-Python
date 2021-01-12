

joltage = 0
one = 0
two = 0
three = 0

def split_input(textfile):
    inputlist = []
    with open(textfile, encoding='utf-8') as file:
        contents = file.read()
        input_list = contents.split('\n')
        for element in input_list:
            inputlist.append(int(element))
    return(inputlist)

def joltage_difference(inputlist):
    global joltage
    global one
    global two
    global three

    print("Inputlist: ", inputlist)

    transmitters = sorted(inputlist)
    print("Transmitters list: ", transmitters)


    for x in transmitters:
        if int(x) == joltage + 1:
            joltage = x
            one += 1

        elif x == joltage + 2:
            joltage = x
            two += 1

        elif int(x) == joltage + 3:
            joltage = x
            three += 1

        else:
            print("Error, no fitting sequence found.")

    four = three + 1
    result = one * four
    print(result)

inputlist = split_input("input.txt")
joltage_difference(inputlist)
