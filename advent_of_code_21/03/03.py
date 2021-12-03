import util

filepath = r"C:\Users\jan_m\Documents\Code\python_projects\advent_of_code_21\03\input.txt"
input = util.readFile(filepath)

binary_one = ""
binary_zero = ""
binary_one_count = 0
binary_zero_count = 0
max_lengths = len(input[0])

for counter in range(max_lengths):
    for i in range(len(input)):
        if input[i][counter] == "1":
            binary_one_count += 1
        elif input[i][counter] == "0":
            binary_zero_count += 1
    if binary_one_count > binary_zero_count:
        binary_one += "1"
        binary_zero += "0"
    else:
        binary_one += "0"
        binary_zero += "1"
    binary_one_count = 0
    binary_zero_count = 0

# binary to decimal
print(int(binary_one, 2) * int(binary_zero, 2))





    
    


