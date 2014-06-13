
















def binarySearch(number, orderedList):
	found = False
	bottom = 0
	top = len(orderedList)-1
	while bottom <= top and not found:
		middle = (bottom + top) // 2
		if orderedList[middle] == number:
			found = True
		elif orderedList[middle] < number:
			bottom = middle+1
		else:
			top = middle-1
	return found





if __name__=="__main__":
	orderedList = [2,3,5,6,7,9,13,14,15,17,20]
	item = int(input("What number are you looking for? "))
 	isFound = binarySearch(item, orderedList)
	if isFound:
		print "The number is found!"
	else:
		print "The number is not found."
