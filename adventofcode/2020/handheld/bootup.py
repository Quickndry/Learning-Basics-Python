indexposition = 0
accumulator = 0
ind = 0

def splitfile(textfile):
    with open(textfile) as document:
        lines = document.readlines()
        list_of_lines = [x.strip() for x in lines]
    return(list_of_lines)

def split_by_pattern(oneline):
    oneline_string = oneline[:5] + ' ' + oneline[5:]
    oneline_list = oneline_string.split(' ')
    return(oneline_list)

def splitlist(list_of_lines):
    list_of_oneliners = []
    for i in list_of_lines:
        list_of_oneliners.append(split_by_pattern(i))
    return list_of_oneliners

def bootupseq(list_of_oneliners):
    global indexposition
    global accumulator

    oneline = list_of_oneliners[indexposition]
    oneline.insert(0, str(indexposition))
    print(oneline)

    if len(oneline) > 4:
        return(accumulator)

    else:
        if oneline[1] == 'acc':
            if oneline[2] == '-':
                accumulator -= int(oneline[3])
                indexposition += 1
                oneline.append('marker')
            else:
                accumulator += int(oneline[3])
                indexposition += 1
                oneline.append('marker')

        elif oneline[1] == 'jmp':
            if oneline[2] == '-':
                indexposition -= int(oneline[3])
                oneline.append('marker')
            else:
                indexposition += int(oneline[3])
                oneline.append('marker')

        elif online[0] == 'nop':
            indexposition += 1
            oneline.append('marker')

        else:
            message = 'Boot up complete'
            return(message)

        bootupseq(list_of_oneliners)

def findcorruption(sequencefile, bootupfile):
    with open(sequencefile) as document:
        lines = document.readlines()
        firstsequence = [x.strip() for x in lines]
#       move the  file  converter to a new function
#       and ensure each element is turned into a
#       concurring list element.

        for line in firstsequence:
            modifier = int(indexposition) + 1

            if line[1] == 'jmp':
                for element in bootupfile[line[0]]:
                    modifiedline = element.replace("jmp", "nop")

                bootupfile.insert(line[0], modifiedline)
                oldline = bootupfile.pop(modifier)
                result = bootupseq(bootupfile)

                if type(result) == str:
                    print('Boot successful. Line changed: ', line)

                else:
                    bootupfile.inster(line[0], oldline)
                    bootupfile.pop(modifiedline)
                    pass

            elif line[1] == 'nop':
                for element in bootupfile[line[0]]:
                    modifiedline = element.replace("nop", "jmp")

                bootupfile.insert(line[0], modifiedline)
                oldline = bootupfile.pop(modifier)
                result = bootupseq(bootupfile)

                if type(result) == str:
                    print('Boot successful. Line changed: ', line)

                else:
                    bootupfile.inster(line[0], oldline)
                    bootupfile.pop(modifiedline)
                    pass
            else:
                pass

def partone(textfile):
    list_of_lines = splitfile(textfile)
    list_of_oneliners = splitlist(list_of_lines)
    result = bootupseq(list_of_oneliners)
    print(result)

def parttwo()


#second part
list_of_lines = splitfile("bootup.txt")
list_of_oneliners = splitlist(list_of_lines)
findcorruption('firstsequence.txt', list_of_oneliners)
