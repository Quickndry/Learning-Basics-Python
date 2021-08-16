# Remove comments from a string using markers:
# Use regex to identify index position of comment markers
# Remove the comments and recombine into new string
# Split appart to remove trailing whitespaces and last newline
# Combine and output

import re

def solution(string,markers):
	
	comments = []

	adaptedString = string + "\n"

	for marker in markers:
		adaptedMarker = "\\" + marker
		pattern = re.compile(rf"{re.escape(marker)}(.*)")

		matches = pattern.finditer(adaptedString)
		
		for match in matches:
			comments.append(adaptedString[match.start():match.end()])

	tempString = re.sub(r'|'.join(map(re.escape, comments)), '', adaptedString)

	tempStringList = tempString.split("\n")
	newStringList= []
	for temporary in tempStringList:
		newStringList.append(temporary.rstrip())
	newString = "\n".join(newStringList)
	outputString = newString[0:-1]

  return outputString

	

