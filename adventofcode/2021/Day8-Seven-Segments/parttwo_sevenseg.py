def myFunc(e):
  return len(e)

def sevenseg(txtfile):
  input_file = open(txtfile, "r")
  input_strings = input_file.read()
  string_list = input_strings.split("\n")
  partone = []
  parttwo = []
  
  for string in string_list:
    split_string = string.split("|")
    partone.append(split_string[0].split(" "))
    parttwo.append(split_string[1].split(" "))
    print("Part one: ", partone, "\nParttwo: ", parttwo)

  translator_dict = {
    "1": ["c", "f"],
    "2": ["a", "c", "d", "e", "g"],
    "3": ["a", "c", "d", "f", "g"],
    "4": ["b", "c", "d", "f"],
    "5": ["a", "b", "d", "f", "g"],
    "6": ["a", "b", "d", "e", "f", "g"],
    "7": ["a", "c", "f"],
    "8": ["a", "b", "c", "d", "e", "f", "g"],
    "9": ["a", "b", "c", "e", "f", "g"],
    "0": ["a", "b", "c", "e", "f", "g"],
  }
  
  length_dict = {
    "2": ["1"],
    "3": ["7"],
    "4": ["4"],
    "5": ["2", "3", "5"],
    "6": ["0", "9", "6"],
    "7": ["8"],
  }
    
  code_dict = {}
  
  for digit_code in partone:
    print("\nDigit code: ", digit_code)
    digit_code.sort(key=myFunc)
    print("\nDigit code sorted: ", digit_code)
    for digit in digit_code[:2]:
      print("\nDigit: ", digit)
      if len(digit) == 2:
        for i in range(2):
          dictionary_entry = {digit[i]:translator_dict["1"]}
          code_dict.update(dictionary_entry)
      elif len(digit) == 3:
        dictionary_entry = {digit[0]:translator_dict["7"]}
        code_dict.update(dictionary_entry)
      elif len(digit) == 4:
        dictionary_entry = {digit[0]:translator_dict["4"]}
        code_dict.update(dictionary_entry)
        

        
sevenseg("input.txt")
