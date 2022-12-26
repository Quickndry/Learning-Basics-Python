def supply(inputfile):
    with open(inputfile, 'r') as file:
        file_as_string = file.read()

    truck = file_as_string.split("\n\n")[0]
    truckrows = truck.replace("[", " ").replace("]", " ").split("\n")
    tr_sanitized = [''.join(s) for s in zip(*truckrows)]
    tr_adapted = [x.replace(" ", "")[::-1] for x in tr_sanitized if x != "         "]

    instructions = file_as_string.split("\n\n")[1].split("\n")

    for instruction in instructions:
        i_components = instruction.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")

        for i in range(int(i_components[0])):
            tr_adapted[int(i_components[2])-1] = tr_adapted[int(i_components[2])-1] + tr_adapted[int(i_components[1])-1][-1]
            tr_adapted[int(i_components[1])-1] = tr_adapted[int(i_components[1])-1][:-1]             

    result = []
    for row in tr_adapted:
        result.append(row[-1])
    
    finalstring = "".join(result)
    return finalstring



print(supply("input.txt"))


