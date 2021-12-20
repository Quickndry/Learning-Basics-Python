def smoke(txtfile):
  input_file = open(txtfile, "r")
  input_strings = input_file.read()
  string_list = input_strings.split("\n")
  final_output_values = []
  for string in string_list:
    split_string = string.split("|")
    output_values = split_string[1].split(" ")
    for output in output_values:
      final_output_values.append(output)
  
  counter = 0
  for output in final_output_values:
    if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7:
      counter += 1
  
  print("Number of specific digits: ", counter)
  
smoke("input.txt")
