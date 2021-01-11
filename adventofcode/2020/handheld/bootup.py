indexposition = 0
accumulator = 0

#function that bootup txt file into a list of lists containing each line as an
#element
def splitfile(textfile):
    list_of_oneliners = []
    with open(textfile) as document:
        lines = document.readlines()
        list_of_lines = [x.strip() for x in lines]
        for oneline in list_of_lines:
            oneline_string = oneline[:5] + ' ' + oneline[5:]
            list_of_oneliners.append(oneline_string.split(' '))
    return(list_of_oneliners)

#function that checks the accumulator value after running through the bootup
#sequence
def bootupseq(list_of_oneliners):
    global indexposition
    global accumulator

    #reads the line given by the global indexposition
    oneline = list_of_oneliners[indexposition]
    oneline.insert(0, str(indexposition))
#    print(oneline)

    #checks if list element oneline contains marker that shows it has been
    #looped through previously (i.e. now would be its second iteration)
    if len(oneline) > 4:
        print('Broke off at second iteration. Accumulator: ', accumulator)
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

        elif oneline[1] == 'nop':
            indexposition += 1
            oneline.append('marker')

        else:
            message = 'Boot up complete'
            print('Boot up complete. Accumulator: ', accumulator)
            return(message)

        #re-run the sequence until either bootup is completed or second
        #iteration is reached
        bootupseq(list_of_oneliners)

#function to find error in bootup sequence, after finding that it moves into an
#endless loop
def findcorruption(sequencefile, list_of_oneliners):
    #read sequencefile obtained through previous iteration
    list_of_list_sequence = []
    with open(sequencefile) as document:
        lines = document.readlines()
        list_of_sequence = [x.strip() for x in lines]
        for line in list_of_sequence:
            adapted_line = line[2:-2]
            list_of_elements = adapted_line.split('\', \'')
            list_of_list_sequence.append(list_of_elements)
#        print(type(list_of_list_sequence[0]))
        #loop through the sequence to search for any jmp/not and replace them
        #with the other. If found, change the item in the list of oneliners and
        #run the bootup function to test if corruptio is fixed. If not, return
        #list of oneliners to its original state and loop through to the next
        #element in the sequence.
        for line in list_of_list_sequence:

            if line[1] == 'jmp':
                modifiedline = []
                for element in list_of_oneliners[int(line[0])]:
                    modifiedline.append(element.replace("jmp", "nop"))
#                print(modifiedline)

                list_of_oneliners.insert(int(line[0]), modifiedline)
                oldline = list_of_oneliners.pop(int(line[0]) + 1)
                # print(oldline)
#                if list_of_oneliners[int(line[0])] == modifiedline:
#                    print("Conversion successful")

                result = bootupseq(list_of_oneliners)
#                print(result)

                if type(result) == str:
                    print('Boot successful. Line changed: ', line)
                    print(list_of_oneliners)
                    return(list_of_oneliners)

                else:
                    list_of_oneliners.insert(int(line[0]), oldline)
                    list_of_oneliners.pop(int(line[0]) + 1)
                    pass

            elif line[1] == 'nop':
                modifiedline = []
                for element in list_of_oneliners[int(line[0])]:
                    modifiedline.append(element.replace("nop", "jmp"))
#                print(modifiedline)

                list_of_oneliners.insert(int(line[0]), modifiedline)
                oldline = list_of_oneliners.pop(int(line[0]) + 1)
#                print(oldline)

                result = bootupseq(list_of_oneliners)
#                print(result)

                if type(result) == str:
                    print('Boot successful. Line changed: ', line)
                    print(list_of_oneliners)
                    return(list_of_oneliners)

                else:
                    list_of_oneliners.insert(int(line[0]), oldline)
                    list_of_oneliners.pop(int(line[0]) + 1)
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
    result = findcorruption(sequencefile, list_of_onelines)
    print(result)

#partone('bootup.txt')
parttwo('bootup.txt', 'firstsequence.txt')
