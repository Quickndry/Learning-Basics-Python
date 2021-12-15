def stringsplitter(txtfile):
  input_file = open(txtfile, "r")
  input_string = input_file.read()
  temp_lst = input_string.split("\n\n")

  temp_list_of_coordinates = temp_lst[0].split("\n")
  list_of_coordinates = [x.split(",") for x in temp_list_of_coordinates]

  temp_list_of_instructions = temp_lst[1].split("\n")
  list_of_instructions = [inst[11:].split("=") for inst in temp_list_of_instructions]

  coordinates_and_instructions = []
  coordinates_and_instructions.append(list_of_coordinates)
  coordinates_and_instructions.append(list_of_instructions)
#  print("Coordinate lst: ", list_of_coordinates, "Instruction lst: ", list_of_instructions)
  return coordinates_and_instructions

def fold_action(coordinate_lst, fold_instructions):
  newcoordinate_lst = []

  if len(fold_instructions) > 0:
		
    if fold_instructions[0][0] == "x":
      for coordinate in coordinate_lst:
         if int(coordinate[0]) < int(fold_instructions[0][1]):
           if coordinate not in newcoordinate_lst:
             newcoordinate_lst.append(coordinate)
         else:
           difference = abs(int(coordinate[0]) - int(fold_instructions[0][1]))
           newx = int(fold_instructions[0][1]) - difference
           newcoordinate = [str(newx), coordinate[1]]
           if newcoordinate not in newcoordinate_lst:
             newcoordinate_lst.append(newcoordinate)
	
    elif fold_instructions[0][0] == "y":
      for coordinate in coordinate_lst:
        if int(coordinate[1]) < int(fold_instructions[0][1]):
           if coordinate not in newcoordinate_lst:
             newcoordinate_lst.append(coordinate)
        else:
          difference = abs(int(coordinate[1]) - int(fold_instructions[0][1]))
          newy = int(fold_instructions[0][1]) - difference
          newcoordinate = [coordinate[0], str(newy)]
          if newcoordinate not in newcoordinate_lst:
            newcoordinate_lst.append(newcoordinate)
  
    newfold_instructions = fold_instructions[1:]
    print("Number of coordinates: ", len(newcoordinate_lst))
    return fold_action(newcoordinate_lst, newfold_instructions)

  else:
    number_of_dots = len(newcoordinate_lst)
    print("Number of coordinates: ", number_of_dots)
    return number_of_dots

workinglist = stringsplitter("input.txt")
fold_action(workinglist[0], workinglist[1])
