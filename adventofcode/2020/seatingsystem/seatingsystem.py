
# Basic working idea
# Step 1: Turn all empty seats into occupied seats.
# Step 2: Itirate through each row, using the seating rules to determine if
# people would move.
# Step 3: Repeat the process on results of Step 2.
# Step 4: Compare results of Step 3 with the results of Step 2.If the same:
# return number of occupied seats in result. If not the same, repeat Step 3
# with the result of Step 3 and compare both Step 3's first result with it's
# second result etc.

# Convert content to textvariable in which every '\n' is replaced by 'B'
# Find length of row (i.e. start to 'B')
# Use this to iterate through textvariable, replacing everything according to
# the rules.
#
# change input to the example from the readme and print the steps to see where
# it goes wrong
counter = 0

def convert_seats(content_string, row_len):
	placeholder = []
	global counter

	print("Input:\n", content_string)

	for i, element in enumerate(content_string, 1):

		if element == '.':
			placeholder.append('.')

		elif element == 'L':
			try:
				if content_string[i] and content_string[i - 1] and content_string[i + 1] == "L" or "." or "B":
					placeholder.append("#")
				else:
					placeholder.append("L")
			except IndexError:
				try:
					if content_string[i] and content_string[i + 1] == "L" or "." or "B":
						placeholder.append("#")
					else:
						placeholder.append("L")
				except IndexError:
					if content_string[i] and content_string[i - 1] == "L" or "." or "B":
						placeholder.append("#")
					else:
						placeholder.append("L")

		elif element == '#':
			try: # checks all adjacent seats
				sample = []
				sample.extend([content_string[i - 1], content_string[i + 1], content_string[i + row_len], content_string[i - row_len], content_string[i + row_len - 1], content_string[i + row_len + 1], content_string[i - row_len + 1], content_string[i - row_len -1]])
				occupied_seats = sample.count('#')
				if occupied_seats > 3:
					placeholder.append('L')
				else:
					placeholder.append('#')

			except IndexError:
				try: # checks all adjacent seats except those of the row above
					sample = []
					sample.extend([content_string[i + 1], content_string[i - 1], content_string[i + row_len], content_string[i + row_len + 1], content_string[i + row_len - 1]])
					occupied_seats = sample.count('#')
					if occupied_seats > 3:
						placeholder.append('L')
					else:
						placeholder.append('#')

				except IndexError:
					try: # checks all adjacent seats, except those that come before
						sample = []
						sample.extend([content_string[i + 1], content_string[i + row_len], content_string[i + row_len + 1], content_string[i + row_len - 1]])
						occupied_seats = sample.count('#')
						if occupied_seats > 3:
							placeholder.append('L')
						else:
							placeholder.append('#')

					except IndexError:
						try: # checks all adjacent seats except those of the row below
							sample = []
							sample.extend([content_string[i + 1], content_string[i - 1], content_string[i - row_len], content_string[i - row_len + 1], content_string[i - row_len - 1]])
							occupied_seats = sample.count('#')
							if occupied_seats > 3:
								placeholder.append('L')
							else:
								placeholder.append('#')

						except IndexError: # checks all adjacent seats, except the ones that come after
							sample = []
							sample.extend([content_string[i - 1], content_string[i - row_len], content_string[i - row_len - 1], content_string[i - row_len + 1]])
							occupied_seats = sample.count('#')
							if occupied_seats > 3:
								placeholder.append('L')
							else:
								placeholder.append('#')

		elif element == 'B':
			placeholder.append('B')

		else:
			print('Unknown element in plan')

	newstring = ''.join(placeholder)

	if newstring == content_string:
		return(newstring.count('#'))
	else:
		counter += 1
		print("Iteration: ", counter, "\nNew Seat pattern: \n", newstring)
		convert_seats(newstring, row_len)

# converts textfile to string
def file_to_string(textfile):
	with open(textfile, encoding='utf-8') as file:
		content = file.read()
		content_string = content.replace('\n', 'B')
		return(content_string)

# finds rowlength from textfile
def rowlength(textfile):
	with open(textfile, encoding='utf-8') as file:
		content = file.read()
		seating_rows = content.split('\n')
		row_len = len(seating_rows[1]) + 1
		return(row_len)



# Endprocess
input_string = file_to_string('input.txt')
length_of_row = rowlength('input.txt')
number_of_occupied_seats = convert_seats(input_string, length_of_row)
print(number_of_occupied_seats)
