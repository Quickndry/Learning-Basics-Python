
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
            elements = element.split(var2)
#            print(element, '\n', elements, '\n')
            lastlist.append(elements)

#        print(lastlist, '\n')
        print(lastlist[indexposition], '\n', lastlist[indexposition[0]])
        return(lastlist)

def check_boot_step(anotherlist):
    global indexposition
    global accumulator
    global previouspositions

    if anotherlist[indexposition[0]] == acc:
        accumulator += anotherlist[indexposition[1]]
        previouspositions.append(indexposition)
        indexposition += 1

    elif anotherlist[indexposition[0]] == jmp:
        previouspositions.append(indexposition)
        indexposition += anotherlist[indexposition[1]]

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
