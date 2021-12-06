def hydro(txtfile):
  # read file and create list of coordinate strings e.g. 
  # ("0,1 -> 2,1")
  input_file = open(txtfile, "r")
  input_string = input_file.read()
  input_list = input_string.split("\n")
  input_file.close()

  hydrovents = []
  counter = 0
  
  # loop through coordinate strings to create coordinate 
  # pairs e.g. ("0,1", "2,1") and then loop through pairs
  # to create temporary coordinate pairs e.g. (["0", "1"], 
  # ["2", "1"]) which are then checked. If X1=X2 or Y1=Y2
  # then coordinates and those inbetween are added to 
  # hydrovents list
  for coordinatestring in input_list:
    pairs = coordinatestring.split(" -> ")
    coordinates = []
    
    for pair in pairs:
      temporary_pairs = pair.split(",")
      coordinates.append(temporary_pairs)

    # most common diagonal case 
    if abs(int(coordinates[0][0]) - int(coordinates[0][1])) == abs(int(coordinates[1][0]) - int(coordinates[1][1])):
      # add special semi double diagonal case e.g. "5,5" & "2,8"
      
      # special double diagonal case
      if abs(int(coordinates[0][0]) - int(coordinates[0][1])) == 0:
        if int(coordinates[0][0]) < int(coordinates[1][0]):
          rangeend= int(coordinates[0][1]) + 1
          for i in range(int(coordinates[0][0]), rangeend):
            temporary_pair = str(i) + "," + str(i)
            hydrovents.append(temporary_pair)
            
        elif int(coordinates[0][0]) > int(coordinates[1][0]):
          rangeend= int(coordinates[0][0]) + 1
          for i in range(int(coordinates[0][1]), rangeend):
            temporary_pair = str(i) + "," + str(i)
            hydrovents.append(temporary_pair)
      
      # special diagonal cases
      elif coordinates[0][0] == coordinates[1][1]: 
        if int(coordinates[0][0]) < int(coordinates[0][1]):
          rangeend= int(coordinates[0][1]) + 1
          x = int(coordinates[0][0])
          y = int(coordinates[0][1])
          for i in range(coordinates[0][0], rangeend):
            temporary_pair = str(x) + "," + str(y)
            x += 1
            y -= 1
            hydrovents.append(temporary_pair)

        elif int(coordinates[0][0]) > int(coordinates[0][1]):
          rangeend= int(coordinates[0][0]) + 1
          x = int(coordinates[0][0])
          y = int(coordinates[0][1])
          for i in range(int(coordinates[0][1]), rangeend):
            temporary_pair = str(x) + "," + str(y)
            x -= 1
            y += 1
            hydrovents.append(temporary_pair)

         # normal diagonal cases
      else:
        if int(coordinates[0][0]) < int(coordinates[1][0]):
          rangeend= abs(int(coordinates[0][0]) - int(coordinates[1][0])) + 1
          x = int(coordinates[0][0])
          y = int(coordinates[0][1])
          for i in range(0, rangeend):
            temporary_pair = str(x) + "," + str(y)
            x += 1
            y += 1
            hydrovents.append(temporary_pair)

        elif int(coordinates[0][0]) > int(coordinates[1][0]):
          rangeend= abs(int(coordinates[0][0]) - int(coordinates[1][0])) + 1
          x = int(coordinates[0][0])
          y = int(coordinates[0][1])
          for i in range(0, rangeend):
            temporary_pair = str(x) + "," + str(y)
            x -= 1
            y -= 1
            hydrovents.append(temporary_pair)
            
    # if horizontal
    elif coordinates[0][0] == coordinates[1][0]:
      if int(coordinates[0][1]) < int(coordinates[1][1]):
        rangeend = int(coordinates[1][1]) + 1
        
        for i in range(int(coordinates[0][1]), rangeend):
          temporary_pair = str(coordinates[0][0]) + "," + str(i)
          hydrovents.append(temporary_pair)

      else:
        rangeend = int(coordinates[0][1]) + 1
        
        for i in range(int(coordinates[1][1]), rangeend):
          temporary_pair = str(coordinates[0][0]) + "," + str(i)
          hydrovents.append(temporary_pair)

    # if vertical
    elif coordinates[0][1] == coordinates[1][1]:
      if int(coordinates[0][0]) < int(coordinates[1][0]):
        rangeend = int(coordinates[1][0]) + 1
        
        for i in range(int(coordinates[0][0]), rangeend):
          temporary_pair = str(i) + "," + str(coordinates[0][1])
          hydrovents.append(temporary_pair)
        
      else:
        rangeend = int(coordinates[0][0]) + 1
        
        for i in range(int(coordinates[1][0]), rangeend):
          temporary_pair = str(i) + "," + str(coordinates[0][1])
          hydrovents.append(temporary_pair)
      
  hydrovents_set = set(hydrovents)
  
  for vent in hydrovents_set:
    how_many = hydrovents.count(vent)
    if how_many > 1:
      counter += 1
  print(counter)
  return counter

hydro("input.txt")
