indexposition = 0
accumulator = 0
ind = 0

#function that splits a string by a specific pattern
def split_by_pattern(oneline):
    oneline_string = oneline[:5] + ' ' + oneline[5:]
    oneline_list = oneline_string.split(' ')
    return(oneline_list)

#function that bootup txt file into a list of lists containing each line as an
#element
def splitfile(textfile):
    list_of_oneliners = []
    with open(textfile) as document:
        lines = document.readlines()
        list_of_lines = [x.strip() for x in lines]
        for i in list_of_lines:
            list_of_oneliners.append(split_by_pattern(i))
    return(list_of_oneliners)

#function that checks the accumulator value after running through the bootup
#sequence
def bootupseq(list_of_oneliners):
    global indexposition
    global accumulator

    #reads the line given by the global indexposition
    oneline = list_of_oneliners[indexposition]
    oneline.insert(0, str(indexposition))
    #test print(oneline)

    #checks if list element oneline contains marker that shows it has been
    #looped through previously (i.e. now would be its second iteration)
    if len(oneline) > 4:
        return(accumulator)

    #else it checks the content of one line and proceeds with following its
    #order
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

        #re-run the sequence until either bootup is completed or second
        #iteration is reached
        bootupseq(list_of_oneliners)

#function to find error in bootup sequence, after finding that it moves into an
#endless loop
def findcorruption(sequencefile, list_of_oneliners):
    #read sequencefile obtained through previous iteration
    with open(sequencefile) as document:
        lines = document.readlines()
        firstsequence = [x.strip() for x in lines]

        #loop through the sequence to search for any jmp/not and replace them
        #with the other. If found, change the item in the list of oneliners and
        #run the bootup function to test if corruptio is fixed. If not, return
        #list of oneliners to its original state and loop through to the next
        #element in the sequence.
        for line in firstsequence:
            modifier = int(indexposition) + 1

            if line[1] == 'jmp':
                for element in list_of_oneliners[line[0]]:
                    modifiedline = element.replace("jmp", "nop")
                    print(modifiedline)

                list_of_oneliners.insert(line[0], modifiedline)
                oldline = list_of_oneliners.pop(line[0] + 1)
                result = bootupseq(list_of_oneliners)

                if type(result) == str:
                    print('Boot successful. Line changed: ', line)

                else:
                    list_of_oneliners.insert(line[0], oldline)
                    list_of_oneliners.pop(line[0] + 1)
                    pass

            elif line[1] == 'nop':
                for element in bootupfile[line[0]]:
                    modifiedline = element.replace("nop", "jmp")
                    print(modifiedline)

                list_of_oneliners.insert(line[0], modifiedline)
                oldline = list_of_oneliners.pop(line[0] + 1)
                result = bootupseq(list_of_oneliners)

                if type(result) == str:
                    print('Boot successful. Line changed: ', line)

                else:
                    list_of_oneliners.inster(line[0], oldline)
                    list_of_oneliners.pop(line[0] + 1)
                    pass
            else:
                pass

#function combining splitfile and bootupseq
def partone(textfile):
    list_of_oneliners = splitfile(textfile)
    result = bootupseq(list_of_oneliners)
    print(result)

#function combining splitfile and findcorruption
def parttwo(bootupfile, sequencefile):
    list_of_onelines = splitfile(bootupfile)
    result = findcorruption(sequencefile, list_of_oneliners)
    print(result)

'firstsequence.txt'
