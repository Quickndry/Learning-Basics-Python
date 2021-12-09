def whale(txtfile):
	input_file = open(txtfile, "r")
	input_string = input_file.read()
	input_list = input_string.split(",")
	input_integer_list = [int(x) for x in input_list]
	points = []
	endrange = max(input_integer_list) + 1
  
	for i in range(endrange):
		total_fuel = 0
		for figure in input_integer_list:
			fuel = abs(figure - i)

			total_fuel += fuel
		print("Total Fuel: ", total_fuel)
		points.append(total_fuel)

	minpoint = min(points)
	bestpoint = points.index(minpoint)
	print("Best Point: ", bestpoint, "\nFuel Consumed: ", minpoint)
	return bestpoint

whale("input.txt")
