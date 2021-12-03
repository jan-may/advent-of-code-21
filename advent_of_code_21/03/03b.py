import util

filepath = r"C:\Users\jan_m\Documents\Code\python_projects\advent_of_code_21\03\input.txt"
input = util.readFile(filepath)

#oxygen
input_oxygen = input
for i in range(len(input[0])):
    lst0 = filter(lambda x: x[i] == "0", input_oxygen)
    lst1 = filter(lambda x: x[i] == "1", input_oxygen)
    lst0 = list(lst0)
    lst1 = list(lst1)
    if len(lst1) <= 1 or len(lst0) <= 1:
        input_oxygen = lst1 if len(lst1) > len(lst0) else lst0
        break
    input_oxygen = lst1 if len(lst1) >= len(lst0) else lst0
oxygen_binary = input_oxygen[0]

#co2
input_co2 = input
for i in range(len(input[0])):
    lst0 = filter(lambda x: x[i] == "0", input_co2)
    lst1 = filter(lambda x: x[i] == "1", input_co2)
    lst0 = list(lst0)
    lst1 = list(lst1)
    if len(lst1) <= 1 or len(lst0) <= 1:
        input_co2 = lst1 if len(lst1) < len(lst0) else lst0
        break
    input_co2 = lst1 if len(lst1) <= len(lst0) else lst0
co2_binary = input_co2[0]

#multiply binary strings to dezimal
print(int(co2_binary, 2) * int(oxygen_binary, 2))











    
    


