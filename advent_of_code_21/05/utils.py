def readFile(fileName):
	with open(fileName, "r") as fileObj:
		words = fileObj.read().splitlines()
	# words = [int(i) for i in words] #transform to int list
	return words