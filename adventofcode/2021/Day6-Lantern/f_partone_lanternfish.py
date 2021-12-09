def txt_to_string(txtfile):
  input_file = open(txtfile, "r")
  input_string = input_file.read()
  input_strng = input_string.split(",")
  return input_strng

def lanternfish(list_of_fish, days):
  temp_placeholder = []
  
  for fish in list_of_fish:
    if int(fish) > 0:
      temp_placeholder.append('6')
      temp_placeholder.append('8')
    else:
      temp_fish = int(fish) - 1
      temp_placeholder.append(temp_fish)
  if days > 0:
    new_days = days - 1
    print("Day: ", new_days, "\nFishes: ", len(temp_placeholder))
    return lanternfish(temp_placeholder, new_days)
  else:
    how_many = len(temp_placeholder)
    print(how_many)
    return how_many
  
inputstring = txt_to_string("input.txt")
lanternfish(inputstring, 80)
