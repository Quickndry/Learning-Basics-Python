def slightlyMoreComplicatedDive(txtfile):
  instructionFile = open(txtfile, "r")
  instructions = instructionFile.read()
  instructionsList = instructions.split("\n")
  instructionFile.close()
  
  aim = 0
  depth = 0
  distance = 0
  
  for instruction in instructionsList:
    if len(instruction) == 9:
      distance += int(instruction[-1])
      depth += aim * int(instruction[-1])
    elif len(instruction) == 6:
      aim += int(instruction[-1])
    else:
      aim -= int(instruction[-1])
  
  finalPosition = depth * distance
  
  return finalPosition
