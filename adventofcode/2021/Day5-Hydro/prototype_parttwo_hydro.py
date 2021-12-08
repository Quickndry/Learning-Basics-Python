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
    
    difference_x = abs(int(temp_storage[0][0]) - int(temp_storage[1][0]))
    difference_y = abs(int(temp_storage[0][1]) - int(temp_storage[1][1]))
    
    # Case Diagonal
    
    
    # Case Vertical/Horizontal
    
    
