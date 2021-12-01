def sonarsweep(txtfile):
  depths = open(txtfile, "r")
  content = depths.read()
  content_list = content.split("\n")
  depths.close()

  increased = 0
  decreased = 0
  placeholder = 0
  
  for i in content_list:
    print("i", i, "placeholder", placeholder)
    if int(i) > int(placeholder):
      increased += 1
      print("increased", increased)
    elif int(i) < int(placeholder):
      decreased += 1
      print("decreased", decreased)
    else:
      pass
    placeholder = i
    
  increased -= 1
  print(increased)

sonarsweep("depths.txt")
