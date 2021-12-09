# Set day to targetday - 1 (e.g. if you want the result for 80 days, set 79)
def first_step(txtfile):
  input_file = open(txtfile, "r")
  input_string = input_file.read()
  school = input_string.split(",")
  school_set = set(school)

  zero = 0
  one = 0
  two = 0
  three = 0
  four = 0
  five = 0
  six = 0
  seven = 0
  eight = 0
  
  for fish in school_set:
    temp = school.count(fish)
    
    if fish == "0":
      zero += temp
    elif fish == "1":
      one += temp
    elif fish == "2":
      two += temp
    elif fish == "3":
      three += temp
    elif fish == "4":
      four += temp
    elif fish == "5":
      five += temp
    elif fish == "6":
      six += temp
    elif fish == "7":
      seven += temp
    elif fish == "8":
      eight += temp
  school_list = [zero, one, two, three, four, five, six, seven, eight]
  return school_list

def lanternfish(school_list, days):
  zero = school_list[1]
  one = school_list[2]
  two = school_list[3]
  three = school_list[4]
  four = school_list[5]
  five = school_list[6]
  six = school_list[7] + school_list[0]
  seven = school_list[8]
  eight = school_list[0]
  new_school_list = [zero, one, two, three, four, five, six, seven, eight]

  if days > 0:
    new_days = days - 1
    print("Day: ", new_days)
    return lanternfish(new_school_list, new_days)
  else:
    how_many = sum(new_school_list)
    print(how_many)
    return how_many
  
somelist = first_step("input.txt")
lanternfish(somelist, 79)
