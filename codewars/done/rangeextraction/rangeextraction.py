def solution(somelist):
	newlist = []
	for x,i in enumerate(somelist):
		try:
			if i - somelist[x+1] == 1:
				pass
			else:
				newlist.append([])
		except IndexError:
			pass
	newlist.append([])

	newlist[0].append(somelist[0])

	counter = 0
	for position, element in enumerate(somelist):
		try:
			if element - somelist[position+1] == -1:
				newlist[counter].append(somelist[position+1])
			else:
				counter +=1
				newlist[counter].append(somelist[position+1])
		except IndexError:
			pass
	
	finallist = []
	for sublist in newlist:
		if len(sublist) >= 3:
			newstring = str(sublist[0]) + "-" + str(sublist[-1])
			finallist.append(newstring)
		else:
			for number in sublist:
				finallist.append(str(number))
	
	outputstring = ",".join(finallist)
	return outputstring


