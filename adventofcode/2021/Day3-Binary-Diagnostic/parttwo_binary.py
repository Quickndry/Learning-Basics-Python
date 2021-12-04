def file_to_list(txtfile):
  binarycodes_file = open(txtfile, "r")
  binarycodes = binarycodes_file.read()
  binarycodes_list = binarycodes.split("\n")
  binarycodes_file.close()
  
  return binarycodes_list

def oxygen_generator_rating(codelist, indexposition):
  ones = 0
  zeroes = 0
  temporary_codelist_a = []
  temporary_codelist_b = []

  
  for code in codelist:
    if code[indexposition] == "1":
      ones += 1
      temporary_codelist_a.append(code)
    else:
      zeroes += 1
      temporary_codelist_b.append(code)

  if ones >= zeroes:
    if len(temporary_codelist_a) > 1:
      return oxygen_generator_rating(temporary_codelist_a, indexposition + 1)
    else:
      print("Oxygen Generator: ", int(temporary_codelist_a[0], 2))
      return int(temporary_codelist_a[0], 2)
    
  else:
    if len(temporary_codelist_b) > 1:
      return oxygen_generator_rating(temporary_codelist_b, indexposition + 1)
    else:
      print("Oxygen Generator: ", int(temporary_codelist_b[0], 2))
      return int(temporary_codelist_b[0], 2)


def oxygen_scrubber_rating(codelist, indexposition):
  ones = 0
  zeroes = 0
  temporary_codelist_a = []
  temporary_codelist_b = []

  
  for code in codelist:
    if code[indexposition] == "1":
      ones += 1
      temporary_codelist_a.append(code)
    else:
      zeroes += 1
      temporary_codelist_b.append(code)

  if ones < zeroes:
    if len(temporary_codelist_a) > 1:
      return oxygen_scrubber_rating(temporary_codelist_a, indexposition + 1)
    else:
      print("Oxygen Scrubber: ", int(temporary_codelist_a[0], 2))
      return int(temporary_codelist_a[0], 2)
    
  else:
    if len(temporary_codelist_b) > 1:
      return oxygen_scrubber_rating(temporary_codelist_b, indexposition + 1)
    else:
      print("Oxygen Scrubber: ", int(temporary_codelist_b[0], 2))
      return int(temporary_codelist_b[0], 2)
 
bcode_list = file_to_list("input.txt")
scrubber = oxygen_scrubber_rating(bcode_list, 0)
generator = oxygen_generator_rating(bcode_list, 0)
lifesupport = int(scrubber) * int(generator)
print("Lifesupport rating: ", lifesupport)
