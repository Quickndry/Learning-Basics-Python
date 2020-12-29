def findcorruption(sequencefile):
    list_of_list_sequence = []
    with open(sequencefile) as document:
        lines = document.readlines()
        list_of_sequence = [x.strip() for x in lines]
        for line in list_of_sequence:
            adapted_line = line[2:-2]
            list_of_elements = adapted_line.split('\', \'')
            list_of_list_sequence.append(list_of_elements)
    print(list_of_list_sequence)
    return(list_of_list_sequence)


findcorruption('firstsequence.txt')
