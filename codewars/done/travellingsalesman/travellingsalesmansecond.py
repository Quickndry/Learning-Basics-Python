import re

def travel(r, zipcode):
	if len(zipcode) != 8:
		outputString = zipcode + ":/"
		return outputString
		
	adressList = r.split(",")
	targetAdressList = []
	for adress in adressList:
		if zipcode in adress:
			targetAdressList.append(adress[0:-8])
	#split adresses into list, then check if listobject
	#includes zipcode. If it does, add to a new list
	print(targetAdressList)

	streetNameList = []
	streetNumberList = []
	for adress in targetAdressList:
		streetNumber = re.search("([0-9]{1,4})", adress)
		streetNumberList.append(streetNumber.group(0))
		removeFirstCharacters = len(streetNumber.group(0)) + 1
		streetName = adress[removeFirstCharacters:-1]
		streetNameList.append(streetName)
	#extract street number and name from adress and 
	#add to new list
	print(streetNumberList)
	print(streetNameList)

	streetNamesString = ",".join(streetNameList)
	streetNumberString = ",".join(streetNumberList)
	outputString = zipcode + ":" + streetNamesString + "/" + streetNumberString
	#join the individual adress components to output string
	print(outputString)

	return outputString
'AA 45522: Paris St. Abbeville , Paris St. Abbeville /67,670' 
'AA 45522:Paris St. Abbeville,Paris St. Abbeville/67,670'
