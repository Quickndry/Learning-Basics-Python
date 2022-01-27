import math
def is_interesting(number, awesome_phrases):

	# Status
	sta_incremental = True
	sta_decremental = True
	sta_palindrome = True
	sta_allsame = True
	sta_zeroes = True
	sta_specialwords = True

	# Create list for all three miles
	mile_list = [int(x) for x in str(number)]
	next_mile = number + 1
	next_mile_list = [int(x) for x in str(next_mile)]
	snext_mile = number + 2
	snext_mile_list = [int(x) for x in str(snext_mile)]

	for position, digit in enumerate(mile_list):
		try:
			if position == 0:
				if digit == 0:
					sta_incremental = False

			if position > 0:
				if digit != 0:
					sta_zeroes = False

			if digit != mile_list[position + 1]:
				sta_allsame = False

			if digit - mile_list[position + 1] != -1:
				if digit == 9 and mile_list[position + 1] == 0:
					pass
				else:
					sta_incremental = False

			if digit - mile_list[position + 1] != 1:
				sta_decremental = False

		except IndexError:
			pass

	# Palindrome check
	if (len(mile_list) % 2) != 0:
		firstend = math.floor(len(mile_list)/2)
		secondstart = firstend + 1
	else:
		firstend = math.floor(len(mile_list)/2)
		secondstart = firstend
    
	firsthalve = mile_list[0:firstend]
	secondhalve = mile_list[secondstart:]
  
	if firsthalve != secondhalve:
		sta_palindrome = False

	if number not in awesome_phrases:
		sta_specialwords = False

	if sta_incremental == True or sta_decremental == True or sta_palindrome == True or sta_allsame == True or sta_zeroes == True or sta_specialwords == True:
		if len(str(number)) < 3:
			pass
		else:
			return 2

	# Reset Status
	sta_incremental = True
	sta_decremental = True
	sta_palindrome = True
	sta_allsame = True
	sta_zeroes = True
	sta_specialwords = True

	for position, digit in enumerate(next_mile_list):
		try:
			if position == 0:
				if digit == 0:
					sta_incremental = False
					
			if position > 0:
				if digit != 0:
					sta_zeroes = False

			if digit != next_mile_list[position + 1]:
				sta_allsame = False

			if digit - next_mile_list[position + 1] != -1:
				if digit == 9 and next_mile_list[position + 1] == 0:
					pass
				else:
					sta_incremental = False

			if digit - next_mile_list[position + 1] != 1:
				sta_decremental = False

		except IndexError:
			pass

	# Palindrome check
	if (len(mile_list) % 2) != 0:
		firstend = math.floor(len(next_mile_list)/2)
		secondstart = firstend + 1
	else:
		firstend = math.floor(len(next_mile_list)/2)
		secondstart = firstend

	firsthalve = next_mile_list[0:firstend]
	secondhalve = next_mile_list[secondstart:]
  
	if firsthalve != secondhalve:
		sta_palindrome = False

	if next_mile not in awesome_phrases:
		sta_specialwords = False

	if sta_incremental == True or sta_decremental == True or sta_palindrome == True or sta_allsame == True or sta_zeroes == True or sta_specialwords == True:
		if len(str(next_mile)) < 3:
			pass
		else:
			return 1

	# Reset Status
	sta_incremental = True
	sta_decremental = True
	sta_palindrome = True
	sta_allsame = True
	sta_zeroes = True
	sta_specialwords = True

	for position, digit in enumerate(snext_mile_list):
		try:
			if position == 0:
				if digit == 0:
					sta_incremental = False
					
			if position > 0:
				if digit != 0:
					sta_zeroes = False

			if digit != snext_mile_list[position + 1]:
				sta_allsame = False

			if digit - snext_mile_list[position + 1] != -1:
				if digit == 9 and snext_mile_list[position + 1] == 0:
					pass
				else:
					sta_incremental = False

			if digit - snext_mile_list[position + 1] != 1:
				sta_decremental = False

		except IndexError:
			pass

	# Palindrome check
	if (len(snext_mile_list) % 2) != 0:
		firstend = math.floor(len(snext_mile_list)/2)
		secondstart = firstend + 1
	else:
		firstend = math.floor(len(snext_mile_list)/2)
		secondstart = firstend
    
	firsthalve = snext_mile_list[0:firstend]
	secondhalve = snext_mile_list[secondstart:]
  
	if firsthalve != secondhalve:
		sta_palindrome = False

	if snext_mile not in awesome_phrases:
		sta_specialwords = False

	if sta_incremental == True or sta_decremental == True or sta_palindrome == True or sta_allsame == True or sta_zeroes == True or sta_specialwords == True:
		if len(str(snext_mile)) < 3:
			return 0
		else:
			return 1
	else:
		return 0

is_interesting(30, [1337, 256])
