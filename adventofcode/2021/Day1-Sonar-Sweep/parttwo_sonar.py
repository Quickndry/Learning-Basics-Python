def secondsonarsweep(txtfile):
	depths = open(txtfile, "r")
	content = depths.read()
	depthsList = content.split("\n")
	depths.close()

	placeholder = 0
	increased = 0
	decreased = 0
	lowerBoundary = 0
	upperBoundary = 2
	numberOfIterations = len(depthsList) - 2

	for i in range(numberOfIterations):
		currentSum = int(depthsList[lowerBoundary]) + int(depthsList[lowerBoundary + 1]) + int(depthsList[upperBoundary])

		if currentSum > int(placeholder):
			increased += 1
		elif currentSum < int(placeholder):
			decreased += 1
		else:
			pass
		placeholder = currentSum
		lowerBoundary += 1
		upperBoundary += 1
		
	increased -= 1
	print(increased)

secondsonarsweep("depths.txt")
