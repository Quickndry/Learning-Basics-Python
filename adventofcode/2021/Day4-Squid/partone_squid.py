def american_bingo(txtfile):
  # read file and create list containing the numbers drawn as well
  # as the bingo grids  input_file = open(txtfile, "r")
  input_file = open(txtfile, "r")
  input_string = input_file.read()
  input_list = input_string.split("\n\n")
  input_file.close()

  # seperate numbers drawn into own list find out number of participants
  # create an empty dictionary for later storage
  numbers_drawn = input_list.pop(0)
  participants = len(input_list)
  bingo_dictionary = {}
  
  # fill dictionary with integers as keys and empty lists as values
  for i in range(participants):
    bingo_dictionary[i] = []
  
  print("Bingo Dict: ", bingo_dictionary)
  
  # loop over bingo grids and split them into rows, columns and diagonal
  # row and add these to the corresponding empty list in the dictionary
  for i, bingo_grid in enumerate(input_list):
    row_list = bingo_grid.split("\n")
    
    first_column = []
    second_column = []
    third_column = []
    fourth_column = []
    fifth_column = []
    diagonal_row = []
    
    for x, row in enumerate(row_list):
      row_temporary_list = row.split(" ")
      row_elements_list = []
      for element in row_temporary_list:
        if element == "":
          pass
        else:
          row_elements_list.append(element)
      
      bingo_dictionary[i].append(row_elements_list)
      
      first_column.append(row_elements_list[0])
      second_column.append(row_elements_list[1])
      third_column.append(row_elements_list[2])
      fourth_column.append(row_elements_list[3])
      fifth_column.append(row_elements_list[4])
      diagonal_row.append(row_elements_list[x])
    
    bingo_dictionary[i].append(first_column)
    bingo_dictionary[i].append(second_column)
    bingo_dictionary[i].append(third_column)
    bingo_dictionary[i].append(fourth_column)
    bingo_dictionary[i].append(fifth_column)
    bingo_dictionary[i].append(diagonal_row)
    
  print("Bingo Dict Ex: ", bingo_dictionary[0])
  
  # convert numbers drawn into list of individual elements
  numbers_drawn_list = numbers_drawn.split(",")
  
  # loop through numbers and dictionary, removing each drawn
  # number from its list and checking if the list is empty,
  # if it is, it takes the first 5 lists inside the currently
  # looped through dictionary value and recombine them to get
  # the grid of he leftover digits. These are then converted 
  # into the final score
  for numbers in numbers_drawn_list:
    for i in range(participants):
      for x in range(11):
        for number in bingo_dictionary[i][x]:
          if number == numbers:
            bingo_dictionary[i][x].remove(number)
            if len(bingo_dictionary[i][x]) == 0:
              leftover_grid = bingo_dictionary[i][0] + bingo_dictionary[i][1] + bingo_dictionary[i][2] + bingo_dictionary[i][3] + bingo_dictionary[i][4]
              
              leftover_grid_integer = [int(leftover) for leftover in leftover_grid]
              
              leftover_sum = sum(leftover_grid_integer)
              
              final_score = leftover_sum * int(numbers)
              print(final_score)
              return final_score
            
  
  
    
american_bingo("input.txt")
