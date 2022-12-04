# does not work, too high estimate.
def campclear(inputfile):
    file = open(inputfile, 'r')
    lines = file.readlines()
    sum = 0
    for line in lines:
        adapted_line = line.replace('\n', '').replace('-', ',')
        coord = adapted_line.split(',')
        f_range = [x for x in range(int(coord[0]),int(coord[1])+1)]
        s_range = [x for x in range(int(coord[2]), int(coord[3])+1)]
        f_included = False
        s_included = False
        for digit in f_range:
            if digit in s_range:
                f_included = True
        for digit in s_range:
            if digit in f_range:
                s_included = True
        if f_included == True or s_included == True: 
            sum += 1
    return sum


print(campclear("input.txt"))
