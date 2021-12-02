filepath = r"...\advent_of_code_21\02\input.txt"

def readFile(fileName):
	with open(fileName, "r") as fileObj:
		words = fileObj.read().splitlines()
	return words

input = readFile(filepath)

# task1
horizontal = 0
depth = 0

for i in input:
	i = i.split()
	position = i[0]
	value = int(i[1])
	if position == "down":
		depth += value
	elif position == "up":
		depth -= value
	elif position == "forward":
		horizontal += value
erg = horizontal * depth
print(erg)

# Task 2
aim = 0
depth = 0
horizontal = 0

for i in input:
	i = i.split()
	position = i[0]
	value = int(i[1])
	if position == "down":
		aim += value
	elif position == "up":
		aim -= value
	elif position == "forward":
		if aim > 0:
		    depth += aim * value
		horizontal += value

erg = horizontal * depth
print(erg)


