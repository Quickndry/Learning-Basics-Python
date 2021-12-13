def basin(list_of_strings, list_of_coordinates, list_of_dupes, size):
	if len(list_of_coordinates) == 0:
		return size + 1
	else:
		new_list_coordinates = []
		new_size = size
		for i in range(len(list_of_coordinates)):
			coordinates = list_of_coordinates[i]
			list_of_dupes.append(coordinates)
			above_id = [coordinates[0] - 1, coordinates[1]]
			if above_id in list_of_dupes:
				pass
			else:
				if above_id[0] == -1:
					list_of_dupes.append(above_id)
				else:
					above = list_of_strings[coordinates[0] - 1][coordinates[1]]
					if above == "9":
						list_of_dupes.append(above_id)
					else:
						new_size += 1
						list_of_dupes.append(above_id)
						new_list_coordinates.append(above_id)

			below_id = [coordinates[0] + 1, coordinates[1]]
			if below_id in list_of_dupes:
				pass
			else:
				if below_id[0] >= len(list_of_strings):
					list_of_dupes.append(below_id)
				else:
					below = list_of_strings[coordinates[0] + 1][coordinates[1]]
					if below == "9":
						pass
					else:
						new_size += 1
						list_of_dupes.append(below_id)
						new_list_coordinates.append(below_id)

			prior_id = [coordinates[0], coordinates[1] - 1]
			if prior_id in list_of_dupes:
				pass
			else:
				if prior_id[1] == -1:
					list_of_dupes.append(prior_id)
				else:
					prior = list_of_strings[coordinates[0]][coordinates[1] - 1]
					if prior == "9":
						pass
					else:
						new_size += 1
						list_of_dupes.append(prior_id)
						new_list_coordinates.append(prior_id)

			after_id = [coordinates[0], coordinates[1] + 1]
			if after_id in list_of_dupes:
				pass
			else:	
				if after_id[1] >= len(list_of_strings[coordinates[0]]):
					list_of_dupes.append(after_id)
				else:
					after = list_of_strings[coordinates[0]][coordinates[1] + 1]
					if after == "9":
						pass
					else:
						new_size += 1
						list_of_dupes.append(after_id)
						new_list_coordinates.append(after_id)


		return basin(list_of_strings, new_list_coordinates, list_of_dupes, new_size)

	
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
						character_index = i
						lowcoordinates = [[string_index, character_index]]
						low_coordinates.append(lowcoordinates)
						duplicates = []
						size = 0
						basin_size = basin(string_list, lowcoordinates, duplicates, size)
						basin_sizes.append(basin_size)
				except IndexError:
					try:
						if int(digit) < int(string[i+1]) and int(digit) < int(next_string[i]):
							string_index = string_list.index(string)
							character_index = i
							lowcoordinates = [[string_index, character_index]]
							duplicates = []
							size = 0
							basin_size = basin(string_list, lowcoordinates, duplicates, size)
							basin_sizes.append(basin_size)
					except IndexError:
						try:
							if int(digit) < int(string[i-1]) and int(digit) < int(next_string[i]):
								string_index = string_list.index(string)
								character_index = i
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
						character_index = i
						lowcoordinates = [[string_index, character_index]]
						duplicates = []
						size = 0
						basin_size = basin(string_list, lowcoordinates, duplicates, size)
						basin_sizes.append(basin_size)
				except IndexError:
					try:
						if int(digit) < int(previous_string[i]) and int(digit) < int(string[i+1]):
							string_index = string_list.index(string)
							character_index = i
							lowcoordinates = [[string_index, character_index]]
							low_coordinates.append(lowcoordinates)
							duplicates = []
							size = 0
							basin_size = basin(string_list, lowcoordinates, duplicates, size)
							basin_sizes.append(basin_size)
					except IndexError:
						try:
							if int(digit) < int(previous_string[i]) and int(digit) < int(string[i-1]):
								string_index = string_list.index(string)
								character_index = i
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
						character_index = i
						lowcoordinates = [[string_index, character_index]]
						duplicates = []
						size = 0
						basin_size = basin(string_list, lowcoordinates, duplicates, size)
						basin_sizes.append(basin_size)
				except IndexError:
					try:
						if int(digit) < int(previous_string[i]) and int(digit) < int(string[i+1]) and int(digit) < int(next_string[i]):
							string_index = string_list.index(string)
							character_index = i
							lowcoordinates = [[string_index, character_index]]
							duplicates = []
							size = 0
							basin_size = basin(string_list, lowcoordinates, duplicates, size)
							basin_sizes.append(basin_size)
					except IndexError:
						try:
							if int(digit) < int(previous_string[i]) and int(digit) < int(string[i-1]) and int(digit) < int(next_string[i]):
								string_index = string_list.index(string)
								character_index = i
								lowcoordinates = [[string_index, character_index]]
								duplicates = []
								size = 0
								basin_size = basin(string_list, lowcoordinates, duplicates, size)
								basin_sizes.append(basin_size)
						except IndexError:
							pass
	contains_duplicates = any(low_coordinates.count(element) > 1 for element in low_coordinates)
	basin_sizes.sort(reverse=True)
	final_output = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
	print("Lowpoints ordered: ", sorted(low_coordinates), "\nBasin Sizes: ", basin_sizes, "\nFinal Output", final_output)
	return final_output

smoke("input.txt")
