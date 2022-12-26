
def campclear(inputfile):
    file = open(inputfile, 'r')
    lines = file.readlines()
    sum = 0

    for line in lines:
        adapted_line = line.replace('\n', '').replace('-', ',')
        coord = adapted_line.split(',')

        dif_f_f = int(coord[0]) - int(coord[2])
        dif_f_s = int(coord[1]) - int(coord[3])

        if dif_f_f < 0 and dif_f_s > 0:
            sum +=1
        elif dif_f_f > 0 and dif_f_s < 0:
            sum +=1
        elif dif_f_f == 0 or dif_f_s == 0:
            sum +=1
    return sum
    
print(campclear("input.txt"))