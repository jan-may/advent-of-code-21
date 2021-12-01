# Advent of Code day 1

filepath = r"...\advent_of_code\01\input.txt"

def readFile(fileName):
	with open(fileName, "r") as fileObj:
		words = fileObj.read().splitlines()
	words = [int(i) for i in words] #transform to int list
	return words

input = readFile(filepath)

# Task 1
count = 0
last_num = 0
for i in input:
	if i > last_num:
		count += 1
	last_num = i

print(count-1)

# Task 2 sliding window
count = 0
last_num = 0
for i in range(len(input) -2):
	if (input[i] + input[i+1] + input[i+2]) > last_num:
		count += 1
	last_num = input[i] + input[i+1] + input[i+2]

print(count-1)

