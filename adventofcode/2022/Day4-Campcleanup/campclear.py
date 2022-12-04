
def campclear(inputfile):
    file = open(inputfile, 'r')
    lines = file.readlines()
    sum = 0

    for line in lines:
        adapted_line = line.replace('\n', '').replace('-', ',')
        coord = adapted_line.split(',')

        dif_f_f = int(coord[0]) - int(coord[2]) # 6 - 7 = -1 || 5 - 5 = 0 || 8 - 6 = 2 || 2 - 6 = -4 || 1 - 10 = -9
        dif_f_fs = int(coord[0]) - int(coord[1])
        dif_f_s = int(coord[1]) - int(coord[3]) # 7 - 8 = -1 || 5 - 6 = -1 || 9 - 10 = -1 || 3 - 7 = -4 || 9 - 12 = -3
        dif_f_ss = int(coord[1]) - int(coord[3])

        if dif_f_f < 0 and dif_f_s > 0:
            sum +=1
        elif dif_f_f > 0 and dif_f_s < 0:
            sum +=1
        elif dif_f_f == 0 or dif_f_s == 0:
            sum +=1
        elif dif_f_f > 0 and dif_f_s > 0:
            if dif_f_fs > dif_f_f or dif_f_ss > dif_f_s:
                sum +=1
        elif dif_f_f < 0 and dif_f_s < 0:
            if dif_f_fs > dif_f_f or dif_f_ss > dif_f_s:
                sum +=1
            
    return sum


print(campclear("test.txt"))