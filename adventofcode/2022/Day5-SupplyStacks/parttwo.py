def supply(inputfile):
    with open(inputfile, 'r') as file:
        file_as_string = file.read()

    truck = file_as_string.split("\n\n")[0]
    tr = truck.replace("[", " ").replace("]", " ").split("\n")
    tr_sanitized = [''.join(s) for s in zip(*tr)]
    tr_clean = [x.replace(" ", "") for x in tr_sanitized if x != "         "]
    
    instructions = file_as_string.split("\n\n")[1].split("\n")

    for instruction in instructions:
        compo = instruction.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
        co_clean = []
        for co in compo:
            co_clean.append(int(co) - 1)

        tr_clean[co_clean[2]] = tr_clean[co_clean[1]][:int(compo[0])] + tr_clean[co_clean[2]]
        tr_clean[co_clean[1]] = tr_clean[co_clean[1]][int(compo[0]):]

    result = []
    for row in tr_clean:
        result.append(row[0])
    
    finalstring = "".join(result)
    return finalstring



print(supply("input.txt"))


