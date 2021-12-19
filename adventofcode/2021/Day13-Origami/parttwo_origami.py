def stringsplitter(txtfile):
  input_file = open(txtfile, "r")
  input_string = input_file.read()
  temp_lst = input_string.split("\n\n")

  temp_list_of_coordinates = temp_lst[0].split("\n")
  list_of_coordinates = [x.split(",") for x in temp_list_of_coordinates]
  list_of_coordinates_int = []
  for element in list_of_coordinates:
    coordinate_integer = [int(x) for x in element]
    list_of_coordinates_int.append(coordinate_integer)

  temp_list_of_instructions = temp_lst[1].split("\n")
  list_of_instructions = [inst[11:].split("=") for inst in temp_list_of_instructions]

  coordinates_and_instructions = []
  coordinates_and_instructions.append(list_of_coordinates_int)
  coordinates_and_instructions.append(list_of_instructions)
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
           newcoordinate = [int(newx), int(coordinate[1])]
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
          newcoordinate = [int(coordinate[0]), int(newy)]
          if newcoordinate not in newcoordinate_lst:
            newcoordinate_lst.append(newcoordinate)
  
    newfold_instructions = fold_instructions[1:]
    return fold_action(newcoordinate_lst, newfold_instructions)

  else:
    return coordinate_lst

def final_origami(final_coordinates):
  reverse_coordinates = [x[::-1] for x in final_coordinates]
  final_coordinates.sort(reverse=True)
  reverse_coordinates.sort(reverse=True)
  length_of_string = int(final_coordinates[0][0]) + 1
  number_of_strings = int(reverse_coordinates[0][0]) + 1

  field = []
  finalfield = []

  for i in range(number_of_strings):
    newstring = ". " * length_of_string
    newstring_as_lst = newstring.split(" ")
    field.append(newstring_as_lst)
  
  for coordinates in final_coordinates:
    field[int(coordinates[1])][int(coordinates[0])] = "X"

  for lines in field:
    line = "".join(lines)
    finalfield.append(line)
  
  finalfield_str = "\n".join(finalfield)
  
  text_file = open("output.txt", "w")
  n = text_file.write(finalfield_str)
  text_file.close()
  


workinglist = stringsplitter("input.txt")
point_coordinates = fold_action(workinglist[0], workinglist[1])
final_origami(point_coordinates)
