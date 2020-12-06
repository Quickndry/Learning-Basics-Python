import csv

def howmanytrees(x, y):
	lon = int(x)
	lat = int(y)
	countlon = 0
	treecount = 0

	with open('map.csv', 'r') as f:
		maplist = [row[0] for row in csv.reader(f)]

		for maprow in maplist[lat::lat]:
			countlon += lon

			try:
				if maprow[countlon] == '#':
					treecount += 1

				else:
					pass

			except IndexError:

				countlon = countlon - 31
				print(countlon)

				if maprow[countlon] == '#':
					treecount += 1

				else:
					pass
				pass

	print(treecount)
  return(treecount)

howmanytrees(3, 1)
