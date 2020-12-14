
accumulator = 0
indexposition = 0
lastlist = []
previouspositions = []

def create_list_in_list(afile, var1, var2):
    global lastlist
    with open(afile, encoding='utf-8') as file:
        filecontent = file.read()
        firstlist = filecontent.split(var1)
#        print(firstlist, '\n')

        for element in firstlist:
            correctelement = element[:1] + ' ' + element[3:]
            elements = correctelement.split(var2)
            lastlist.append(elements)

#        print(lastlist, '\n')
        print(lastlist[indexposition], '\n', type(lastlist[indexposition][1]))
        return(lastlist)

def check_boot_step(anotherlist):
    global indexposition
    global accumulator
    global previouspositions

    if anotherlist[indexposition][0] == 'acc':
        previouspositions.append(indexposition)

        if anotherlist[indexposition][1] == '+':
            accumulator += int(anotherlist[indexposition][2])
        else:
            accumulator -= int(anotherlist[indexposition][2])

        indexposition += 1

    elif anotherlist[indexposition][0] == 'jmp':
        previouspositions.append(indexposition)

        if anotherlist[indexposition][1] == '+':
            indexposition += int(anotherlist[indexposition][2])
        else:
            indexposition -= int(anotherlist[indexposition][2])

    else:
        previouspositions.append(indexposition)
        indexposition += 1
        pass

    for element in previouspositions:
        if element == indexposition:
            print(accumulator)

        else:
            check_boot_step(anotherlist)


create_list_in_list('bootup.txt', '\n', ' ')
check_boot_step(lastlist)
