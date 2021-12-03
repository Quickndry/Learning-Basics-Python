def binary_diagnostics(txtfile):
  binarycodes_file = open(txtfile, "r")
  binarycodes = binarycodes_file.read()
  binarycodes_list = binarycodes.split("\n")
  binarycodes_file.close()
  
  # generate two new binary numbers to represent epsilon
  # and gamma rates
  ones = 0
  zeroes = 0
  temporary_code = []
  other_temporary_code = []
  
  for i in range(len(binarycodes_list[0])):
    for code in binarycodes_list:
      if code[i] == "1":
        ones += 1
      else:
        zeroes += 1
     
    if ones > zeroes:
      temporary_code.append("1")
    else:
      temporary_code.append("0")
    
    ones = 0
    zeroes = 0
  
  
  for digit in temporary_code:
    if int(digit) == 1:
      other_temporary_code.append("0")
    else:
      other_temporary_code.append("1")
  
  epsilon_code = ''.join(temporary_code)
  gamma_code = ''.join(other_temporary_code)
  
  power_consumption = int(epsilon_code, 2) * int(gamma_code, 2)
  
  print(power_consumption)
  return power_consumption

binary_diagnostics("input.txt")
