indexposition = 0
accumulator = 0


def splitfile(textfile):
    with open(textfile) as document:
        lines = document.readlines()
        list_of_lines = [x.strip() for x in lines]

        print(list_of_lines)

    return(list_of_lines)

def split_by_pattern(oneline):
    oneline_string = oneline[:5] + ' ' + oneline[5:]
    oneline_list = split(oneline_string, ' ')
    return(oneline_list)

def splitlist(list_of_lines):
    for i in list_of_lines:
        split_by_pattern(i)

def bootupseq(list):
    global indexposition


    if oneline_list[0] == 'acc':
        accumulator += str(oneline_list[2])
        indexposition += 1

    elsif oneline_list[0] == 'jmp':
        indexposition += oneline_list[2]

    else:
        indexposition += 1

    bootupseq(s)



    #regex oneline
    if

    pass
