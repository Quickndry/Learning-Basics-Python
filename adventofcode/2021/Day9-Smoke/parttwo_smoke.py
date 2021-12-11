def basin(list_of_strings, list_of_coordinates, list_of_dupes, size):
	if len(list_of_coordinates) == 0:
		return size
	else:
		new_list_coordinates = []
		for i in range(len(list_of_coordinates)):
			coordinates = list_of_coordinates[i]
			above = list_of_strings[coordinates[0] - 1][coordinates[1]]
			below = list_of_strings[coordinates[0] + 1][coordinates[1]]
			prior = list_of_strings[coordinates[0]][coordinates[1] - 1]
			after = list_of_strings[coordinates[0]][coordinates[1] + 1]
			
			if above in list_of_dupes:
				pass
			else:
				if above == 9:
					pass
				else:
					size += 1
					str_index = coordinates[0] - 1
					char_index = coordinates[1]
					coordinate = [str_index, char_index]
					list_of_dupes.append(coordinate)
					new_list_coordinates.append(coordinate)
			
			if below in list_of_dupes:
				pass
			else:	
				if below == 9:
					pass
				else:
					size += 1
					str_index = coordinates[0] + 1
					char_index = coordinates[1]
					coordinate = [str_index, char_index]
					list_of_dupes.append(coordinate)
					new_list_coordinates.append(coordinate)

			if prior in list_of_dupes:
				pass
			else:	
				if prior == 9:
					pass
				else:
					size += 1
					str_index = coordinates[0]
					char_index = coordinates[1] - 1
					coordinate = [str_index, char_index]
					list_of_dupes.append(coordinate)
					new_list_coordinates.append(coordinate)

			if after in list_of_dupes:
				pass
			else:	
				if after == 9:
					pass
				else:
					size += 1
					str_index = coordinates[0]
					char_index = coordinates[1] + 1
					coordinate = [str_index, char_index]
					list_of_dupes.append(coordinate)
					new_list_coordinates.append(coordinate)
		
		return basin(list_of_strings, new_list_coordinates, list_of_dupes, size)
	
def smoke(txtfile):
	input_file = open(txtfile, "r")
	input_strings = input_file.read()
	string_list = input_strings.split("\n")
	number_of_strings = len(string_list)
	basin_sizes = []

	for string in string_list:
		previous_id = string_list.index(string) - 1
		next_id = string_list.index(string) + 1

		if previous_id == -1:
			next_string = string_list[next_id]
			for i, digit in enumerate(string):
				try:
					if int(digit) < int(string[i-1]) and int(digit) < int(string[i+1]) and int(digit) < int(next_string[i]):
						string_index = string_list.index(string)
						character_index = string.index(digit)
						lowcoordinates = [[string_index, character_index]]
						duplicates = []
						size = 0
						basin_size = basin(string_list, lowcoordinates, duplicates, size)
						basin_sizes.append(basin_size)
				except IndexError:
					try:
						if int(digit) < int(string[i+1]) and int(digit) < int(next_string[i]):
							string_index = string_list.index(string)
							character_index = string.index(digit)
							lowcoordinates = [[string_index, character_index]]
							duplicates = []
							size = 0
							basin_size = basin(string_list, lowcoordinates, duplicates, size)
							basin_sizes.append(basin_size)
					except IndexError:
						try:
							if int(digit) < int(string[i-1]) and int(digit) < int(next_string[i]):
								string_index = string_list.index(string)
								character_index = string.index(digit)
								lowcoordinates = [[string_index, character_index]]
								duplicates = []
								size = 0
								basin_size = basin(string_list, lowcoordinates, duplicates, size)
								basin_sizes.append(basin_size)
						except IndexError:
							pass

		elif next_id >= number_of_strings:
			previous_string = string_list[previous_id]
			for i, digit in enumerate(string):
				try:
					if int(digit) < int(previous_string[i]) and int(digit) < int(string[i-1]) and int(digit) < int(string[i+1]):
						string_index = string_list.index(string)
						character_index = string.index(digit)
						lowcoordinates = [[string_index, character_index]]
						duplicates = []
						size = 0
						basin_size = basin(string_list, lowcoordinates, duplicates, size)
						basin_sizes.append(basin_size)
				except IndexError:
					try:
						if int(digit) < int(previous_string[i]) and int(digit) < int(string[i+1]):
							string_index = string_list.index(string)
							character_index = string.index(digit)
							lowcoordinates = [[string_index, character_index]]
							duplicates = []
							size = 0
							basin_size = basin(string_list, lowcoordinates, duplicates, size)
							basin_sizes.append(basin_size)
					except IndexError:
						try:
							if int(digit) < int(previous_string[i]) and int(digit) < int(string[i-1]):
								string_index = string_list.index(string)
								character_index = string.index(digit)
								lowcoordinates = [[string_index, character_index]]
								duplicates = []
								size = 0
								basin_size = basin(string_list, lowcoordinates, duplicates, size)
								basin_sizes.append(basin_size)
						except IndexError:
							pass
		
		else:
			next_string = string_list[next_id]
			previous_string = string_list[previous_id]
			for i, digit in enumerate(string):
				try:
					if int(digit) < int(previous_string[i]) and int(digit) < int(string[i-1]) and int(digit) < int(string[i+1]) and int(digit) < int(next_string[i]):
						string_index = string_list.index(string)
						character_index = string.index(digit)
						lowcoordinates = [[string_index, character_index]]
						duplicates = []
						size = 0
						basin_size = basin(string_list, lowcoordinates, duplicates, size)
						basin_sizes.append(basin_size)
				except IndexError:
					try:
						if int(digit) < int(previous_string[i]) and int(digit) < int(string[i+1]) and int(digit) < int(next_string[i]):
							string_index = string_list.index(string)
							character_index = string.index(digit)
							lowcoordinates = [[string_index, character_index]]
							duplicates = []
							size = 0
							basin_size = basin(string_list, lowcoordinates, duplicates, size)
							basin_sizes.append(basin_size)
					except IndexError:
						try:
							if int(digit) < int(previous_string[i]) and int(digit) < int(string[i-1]) and int(digit) < int(next_string[i]):
								string_index = string_list.index(string)
								character_index = string.index(digit)
								lowcoordinates = [[string_index, character_index]]
								duplicates = []
								size = 0
								basin_size = basin(string_list, lowcoordinates, duplicates, size)
								basin_sizes.append(basin_size)
						except IndexError:
							pass
	print("Basin Sizes: ", basin_sizes)
	return basin_sizes

smoke("input.txt")
