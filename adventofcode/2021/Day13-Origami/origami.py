def stringsplitter(txtfile):
	input_file = open(txtfile, "r")
	input_string = input_file.read()
	temp_lst = input_string.split("\n\n")
  list_of_coordinates = temp_lst[0].split("\n")
  temp_list_of_instructions = temp_lst[1].split("\n")
  for instruction in temp_list_of_instructions:
    temp_instruction = re.match(x=[0-9]{1,}|y=[0-9]{1,})
    

  
def fold_action(coordinate_lst, fold_instructions):
    newcoordinate_lst = []
    
    if fold_instructions[0][0] == "x":
        for coordinate in coordinate_lst:
            if int(coordinate[0]) < int(fold_instructions[0][1]):
                newcoordinate_lst.append(coordinate)
            else:
                difference = abs(int(coordinate[0]) - int(fold_instructions[0][1]))
                newx = int(fold_instructions[0][1]) - difference
                newcoordinate = [str(newx), coordinate[1]]
                if newcoordinate not in newcoordinate_lst:
                    newcoordinate_lst.append(newcoordinate)
    elif fold_instructions[0][0] == "y":
        for coordinate in coordinate_lst:
            if int(coordinate[1]) < (fold_instructions[0][1]):
                newcoordinate_lst.append(coordinate)
            else:
                difference = abs(int(coordinate[1]) - int(fold_instructions[0][1]))
                newy = int(fold_instructions[0][1]) - difference
                newcoordinate = [coordinate[0], - str(newy)]
                if newcoordinate not in newcoordinate_lst:
                    newcoordinate_lst.append(newcoordinate)
    newfold_instructions = fold_instructions[1::]
    print(len(newcoordinate_lst))
    return fold_action(newfold_instructions,newcoordinate_lst)
