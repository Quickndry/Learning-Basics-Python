def smoke(txtfile):
	input_file = open(txtfile, "r")
	input_strings = input_file.read()
	string_list = input_strings.split("\n")
	number_of_strings = len(string_list)
	risk_level = 0

	for string in string_list:
		previous_id = string_list.index(string) - 1
		next_id = string_list.index(string) + 1

		if previous_id == -1:
			next_string = string_list[next_id]
			for i, digit in enumerate(string):
				try:
					if int(digit) < int(string[i-1]) and int(digit) < int(string[i+1]) and int(digit) < int(next_string[i]):
						risk_level += int(digit) + 1
				except IndexError:
					try:
						if int(digit) < int(string[i+1]) and int(digit) < int(next_string[i]):
							risk_level += int(digit) + 1
					except IndexError:
						try:
							if int(digit) < int(string[i-1]) and int(digit) < int(next_string[i]):
								risk_level += int(digit) + 1
						except IndexError:
							pass

		elif next_id >= number_of_strings:
			previous_string = string_list[previous_id]
			for i, digit in enumerate(string):
				try:
					if int(digit) < int(previous_string[i]) and int(digit) < int(string[i-1]) and int(digit) < int(string[i+1]):
						risk_level += int(digit) + 1
				except IndexError:
					try:
						if int(digit) < int(previous_string[i]) and int(digit) < int(string[i+1]):
							risk_level += int(digit) + 1
					except IndexError:
						try:
							if int(digit) < int(previous_string[i]) and int(digit) < int(string[i-1]):
								risk_level += int(digit) + 1
						except IndexError:
							pass
		
		else:
			next_string = string_list[next_id]
			previous_string = string_list[previous_id]
			for i, digit in enumerate(string):
				try:
					if int(digit) < int(previous_string[i]) and int(digit) < int(string[i-1]) and int(digit) < int(string[i+1]) and int(digit) < int(next_string[i]):
						risk_level += int(digit) + 1
				except IndexError:
					try:
						if int(digit) < int(previous_string[i]) and int(digit) < int(string[i+1]) and int(digit) < int(next_string[i]):
							risk_level += int(digit) + 1
					except IndexError:
						try:
							if int(digit) < int(previous_string[i]) and int(digit) < int(string[i-1]) and int(digit) < int(next_string[i]):
								risk_level += int(digit) + 1
						except IndexError:
							pass
	print("Risk level: ", risk_level)
	return risk_level

smoke("input.txt")
