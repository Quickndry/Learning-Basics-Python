# Find time it takes to sell and
# buy car as well as how much 
# money is left over

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentlostperMonth):
	
	monthCounter = 0
	savedUp = 0
	checker = 0
	
	while checker == 0:
		totalInv = startPriceOld + savedUp
		
		print("Oldprice new: ",int(startPriceOld), "Saved up: ", savedUp)

		print("Month: ", monthCounter, ", Investment: ", int(totalInv))
		
		leftOver = totalInv - startPriceNew
		
		print("Missing: ", leftOver)

		if totalInv >= startPriceNew:
			print(monthCounter, int(leftOver))
			return(monthCounter, leftOver)

		monthCounter += 1

		savedUp = savedUp + savingperMonth

		if monthCounter % 2 == 0:
			percentlostperMonth += 0.5
			
		print("Percentage lost: ", percentlostperMonth, "\n")
		
		oldPriceLost = startPriceOld * ( percentlostperMonth * 0.01)

		startPriceOld = startPriceOld - oldPriceLost
		
		newPricelost = startPriceNew * (percentlostperMonth * 0.01)
		
		startPriceNew = startPriceNew - newPricelost
	
