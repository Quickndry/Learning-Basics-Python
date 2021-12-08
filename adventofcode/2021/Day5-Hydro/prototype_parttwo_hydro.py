def hydro(txtfile):
  # read file and create list of coordinate strings e.g. 
  # ["0,1 -> 2,1", etc.] = coordinate_strings
  input_file = open(txtfile, "r")
  input_string = input_file.read()
  coordinate_strings = input_string.split("\n")
  input_file.close()

  hydrovents = []
  counter = 0
  
  # loop through strings and split into pairs e.g.
  # ["0,1", "2,1"] = pairs
  for coordinate_pairs in coordinate_strings:
    pairs = coordinate_pairs.split(" -> ")
    
    temp_storage = []
    
    # loop through pairs and split into coordinates e.g.
    # [["0", "1"], ["2", "1"]] = temp_storage
    for pair in pairs:
      coordinates = pair.split(",")
      temp_storage.append(coordinates)
    
    x_difference = abs(int(temp_storage[0][0]) - int(temp_storage[1][0]))
    y_difference = abs(int(temp_storage[0][1]) - int(temp_storage[1][1]))
    x_one = int(temp_storage[0][0])
    x_two = int(temp_storage[1][0])
    y_one = int(temp_storage[0][1])
    y_two = int(temp_storage[1][1])
    
    # Case Diagonal
    if x_difference == y_difference:
      if x_one < x_two and y_one < y_two:
        x_temp = x_one
        y_temp = y_one
        initial_coordinate = str(x_temp) + "," + str(y_temp)
        hydrovents.append(initial_coordinate)
        for i in range(x_difference):
          x_temp += 1
          y_temp += 1
          coordinate_temp = str(x_temp) + "," + str(y_temp)
          hydrovents.append(coordinate_temp)

      if x_two < x_one and y_two < y_one:
        x_temp = x_two
        y_temp = y_two
        initial_coordinate = str(x_temp) + "," + str(y_temp)
        hydrovents.append(initial_coordinate)
        for i in range(x_difference):
          x_temp += 1
          y_temp += 1
          coordinate_temp = str(x_temp) + "," + str(y_temp)
          hydrovents.append(coordinate_temp)
          
      if x_one < x_two and y_two < y_one:
        x_temp = x_one
        y_temp = y_one
        initial_coordinate = str(x_temp) + "," + str(y_temp)
        hydrovents.append(initial_coordinate)
        for i in range(x_difference):
          x_temp += 1
          y_temp -= 1
          coordinate_temp = str(x_temp) + "," + str(y_temp)
          hydrovents.append(coordinate_temp)

      if x_two < x_one and y_one < y_two:
        x_temp = x_two
        y_temp = y_two
        initial_coordinate = str(x_temp) + "," + str(y_temp)
        hydrovents.append(initial_coordinate)
        for i in range(x_difference):
          x_temp += 1
          y_temp -= 1
          coordinate_temp = str(x_temp) + "," + str(y_temp)
          hydrovents.append(coordinate_temp)

    # Case Vertical/Horizontal
    if x_difference == 0:
      if y_one < y_two:
        y_temp = y_one
        initial_coordinate = str(x_one) + "," + str(y_temp)
        hydrovents.append(initial_coordinate)
        for i in range(y_difference):
          y_temp += 1
          coordinate_temp = str(x_one) + "," + str(y_temp)
          hydrovents.append(coordinate_temp)
          
      if y_two < y_one:
        y_temp = y_two
        initial_coordinate = str(x_one) + "," + str(y_temp)
        hydrovents.append(initial_coordinate)
        for i in range(y_difference):
          y_temp += 1
          coordinate_temp = str(x_one) + "," + str(y_temp)
          hydrovents.append(coordinate_temp)

    if y_difference == 0:
      if x_one < x_two:
        x_temp = x_one
        initial_coordinate = str(x_temp) + "," + str(y_one)
        hydrovents.append(initial_coordinate)
        for i in range(x_difference):
          x_temp += 1
          coordinate_temp = str(x_temp) + "," + str(y_one)
          hydrovents.append(coordinate_temp)
          
      if x_two < x_one:
        x_temp = x_two
        initial_coordinate = str(x_temp) + "," + str(y_one)
        hydrovents.append(initial_coordinate)
        for i in range(x_difference):
          x_temp += 1
          coordinate_temp = str(x_temp) + "," + str(y_one)
          hydrovents.append(coordinate_temp)
  
  hydrovents_set = set(hydrovents)
  
  for vents in hydrovents_set:
    if hydrovents.count(vents) > 1:
      counter += 1
  
  print(counter)
  return counter

hydro("input.txt")
