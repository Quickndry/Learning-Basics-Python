import re
holder = []
multipleholder =[]
formula = ''
target = ['shiny gold']
# print(rules, '\n') #test purpose


def newbagcalc(afile, targetlist):
  global holder
  global multipleholder
  global formula

  newbags = []
  addedthisround = 0

  with open(afile, encoding='utf-8') as file:
    contents = file.read()
    rules = contents.replace(',', '').replace('.', '').split('\n')

    for targ in targetlist:
        for rule in rules:
            parentpattern = '^(.*?) bags contain (.*?)$'
            childpattern = '(\d+) (\w+, \w+) bag'

            bagsearch = re.search(parentpattern, rule)

            rulesentence = rule.replace(' bags contain', '').replace(' bags', '').replace(' bag', '').replace(',', '').replace('.', '')

            dpattern = re.compile(' [1-9] ')
            spattern = re.compile(' [a-z] ')

            rulecomponents = re.split(dpattern, rulesentence)
            rulemultiples = re.split(spattern, rulesentence)

            if rulecomponents[0] == targ:
                addedthisround += 1
                print("Target found: ", rulecomponents[0])

                for component in rulecomponents[1::]:
                    newbags.append(component)
                    holder.append(component)

                for multiple in rulemultiples:
                    multipleholder.append(multiple)

            else:
                pass

  if addedthisround == 0:
#    counterresult = len(set(holder))
    print(holder)
#    return counterresult

  else:
      target = newbags
      print(target, '\n')
      newbagcalc(afile, target)

newbagcalc('rules.txt', target)
