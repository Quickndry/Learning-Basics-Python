# Works fine, though instead of creating tempnumbers, so as to
# compare the ID of the elements in numbers, it is also possible
# to compare i and x (the indeces) to ensure they are not the 
# same

def two_sum(numbers, target):
    tempnumbers = [x + 300 for x in numbers]
    for i, ele in enumerate(tempnumbers):
        for x, eletwo in enumerate(tempnumbers):
            if ele is not eletwo:
                if ele + eletwo - 600 == target:
                    return (i, x)