# Conditions to test validity of passport components

def birthyear(x):
	return 2002 >= int(x) >= 1920

def issueyear(x):
	return 2020 >= int(x) >= 2010

def expyear(x):
	return 2030 >= int(x) >= 2020

def height(x):
	try:
		if str(x[-1]) == 'm':
			return 193 >= int(x[0:3]) >= 150
		elif str(x[-1]) == 'n':
			return 76 >= int(x[0:2]) >= 59
		else:
			return False
	except:
		return False

def haircolour(x):
	return len(x) == 7 and x[0] == '#'

def eyecolour(x):
	return x == 'amb' or x == 'blu' or x == 'brn' or x == 'gry' or x == 'grn' or x == 'hzl' or x == 'oth'

def passportid(x):
	return len(str(x)) == 9

#Main code
validpassport = 0
truecount = 0

#Open file and convert to dictionary
with open('inp.txt', encoding='utf-8') as file:

	contents = file.read()
	list_of_passports = contents.split('\n\n')

	for passport in list_of_passports:
		passone = passport.replace(' ', ';')
		passtwo = passone.replace('\n', ';')
		finalpass = passtwo.replace(':', '=')

		passport_dictionary = dict(map(lambda x: x.split('='), finalpass.split(';')))

		#Check dictionary items for validity
		for k, v in passport_dictionary.items():

			if k == 'pid':
				if passportid(v):
					truecount +=1

			if k == 'hcl':
				if haircolour(v):
					truecount +=1

			if k == 'byr':
				if birthyear(v):
					truecount +=1

			if k == 'hgt':
				if height(v):
					truecount +=1

			if k == 'ecl':
				if eyecolour(v):
					truecount +=1

			if k == 'iyr':
				if issueyear(v):
					truecount +=1

			if k == 'eyr':
				if expyear(v):
					truecount +=1

			print(truecount)
		if truecount == 7:
			validpassport += 1
		truecount = 0


print(validpassport)
