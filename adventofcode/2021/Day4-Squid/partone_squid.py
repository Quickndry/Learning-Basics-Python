def american_bingo(txtfile):
  input_file = open(txtfile, "r")
  input_string = input_file.read()
  input_list = input_string.split("\n\n")
  input_file.close()
  
  numbers_drawn = input_list.pop(0)
  participants = len(input_list)
  bingo_dictionary = {}
  
  for i in enumerate(participants):
    bingo_dictionary[i] = []
  
  print("Bingo Dict: ", bingo_dictionary)
  
  


  for i, bingo_grid in enumerate(input_list):
    row_list = bingo_grid.split("\n")
    
    first_column = []
    second_column = []
    third_column = []
    fourth_column = []
    fifth_column = []
    diagonal_row = []
    
    for x, row in enumerate(row_list):
      row_elements_list = row.split(" ")
      bingo_dictionary[i].append(row_elements_list)
      
      first_column.append(row_elements_list[0])
      second_column.append(row_elements_list[1])
      third_column.append(row_elements_list[2])
      fourth_column.append(row_elements_list[3])
      fifth_column.append(row_elements_list[4])
    
      da
      
  




 
