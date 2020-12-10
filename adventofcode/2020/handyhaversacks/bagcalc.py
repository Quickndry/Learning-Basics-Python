import re
holder = []
target = ['shiny gold']
# print(rules, '\n') #test purpose


def checkbags(afile, targetlist):
  global holder
  newbags = []
  addedthisround = 0

  with open(afile, encoding='utf-8') as file:
    contents = file.read()
    rules = contents.replace(',', '').replace('.', '').split('\n')

  for targ in targetlist:
    for rule in rules:
      rulesentence = rule.replace(' bags contain', '').replace(' bags', '').replace(' bag', '').replace(',', '').replace('.', '')

      pattern = re.compile(' [1-9] ')

      rulecomponents = re.split(pattern, rulesentence)

      for component in rulecomponents[1::]:
          if component == targ:
              addedthisround += 1
              print("Target found: ", targ, " in: ", rulecomponents[0])
              newbags.append(rulecomponents[0])
              holder.append(rulecomponents[0])

          else:
              pass

  print(newbags, '\n')

  if addedthisround == 0:
    counterresult = len(set(holder))
    print(counterresult)
    return counterresult

  else:
      target = newbags
      print(target, '\n')
      checkbags(afile, target)

checkbags('rules.txt', target)
