# Part one hard copy

# The first step of attacking the weakness in the XMAS data is to find the first
# number in the list (after the preamble) which is not the sum of two of the 25
# numbers before it.

globalcounter = 0

def create_list_of_sums(list):
    list_of_sums = []
    for element in list:
        counter = list.index(element)
        for i in list:
            counter += 1
            try:
                sum = int(element) + int(list[counter])
                list_of_sums.append(sum)
            except:
                pass
    return(list_of_sums)

def split_input(textfile):
    with open(textfile, encoding='utf-8') as file:
        contents = file.read()
        input_list = contents.split('\n')
    return(input_list)

def find_encoding_error(textfile):
    global globalcounter

    lowerlimit = 0
    upperlimit = 25

    lowerlimit += globalcounter
    upperlimit += globalcounter
#    print("Globalcounter: ", globalcounter, "Upperlimit: ", upperlimit)

    input_list = split_input(textfile)

    control_group = input_list[lowerlimit:upperlimit]
#    print("Control group: ", control_group)

    list_of_sums = create_list_of_sums(control_group)
#    print("List of Sums: ", list_of_sums)

    if int(input_list[upperlimit]) in list_of_sums:
        globalcounter += 1
        find_encoding_error(textfile)

    else:
        print(input_list[upperlimit])


# create a dictionary with indexnumber of element in list as key and the sums of
# the previous pairs of numbers as list as variable.

find_encoding_error("input.txt")
