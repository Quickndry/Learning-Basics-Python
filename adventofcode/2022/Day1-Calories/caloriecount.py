
def calorie_count(inputlst):
    with open(inputlst, 'r') as file:
        file_as_string = file.read()
    
    list_of_sums = []
    list_of_strings = file_as_string.split('\n\n')
    for stringg in list_of_strings:
        temp_list = stringg.split('\n')
        sum = 0
        for number in temp_list:
            sum += int(number)
        list_of_sums.append(sum)
    
    list_of_sums.sort()
    top_three = list_of_sums[-1] + list_of_sums[-2] + list_of_sums[-3]
    return top_three

print(calorie_count("input.txt"))