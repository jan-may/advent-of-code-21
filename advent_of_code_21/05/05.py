import utils

input = utils.readFile('input.txt')

def format_input(input):
    # split lines into lists
    lst = [input[i].split() for i in range(len(input))]
    # split sublists into 2 lists with x and y coordinates
    for item in lst:
        for k in range(len(item)):
            item[k] = item[k].split(",")
            item[k][0] = int(item[k][0])
            item[k][1] = int(item[k][1])
    return lst

def filter_same_coordinates(lst):
    return [
        item
        for item in lst
        if item[0][0] == item[1][0] or item[0][1] == item[1][1]
    ]

def filter_diff_coordinates(lst):
    return [
        item
        for item in lst
        if item[0][0] != item[1][0] and item[0][1] != item[1][1]
    ]

lst = format_input(input)
final_list = filter_same_coordinates(lst)

# find max x and y coordinates
max_x = max(item[0][0] for item in lst)
max_y = max(item[0][1] for item in lst)

# matrix with zeros
matrix = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]


for i in range(len(final_list)):
    difference = 0
    if final_list[i][0][0] != final_list[i][1][0]:
        if final_list[i][0][0] < final_list[i][1][0]:
            difference += final_list[i][1][0] - final_list[i][0][0]
            for z in range(difference + 1):
                matrix[final_list[i][0][1]][final_list[i][0][0] +z] += 1
        else:
            difference += final_list[i][0][0] - final_list[i][1][0]
            for z in range(difference + 1):
                matrix[final_list[i][0][1]][final_list[i][0][0] -z] += 1
    elif final_list[i][0][1] < final_list[i][1][1]:
        difference += final_list[i][1][1] - final_list[i][0][1]
        for z in range(difference + 1):
            matrix[final_list[i][0][1] +z][final_list[i][0][0]] += 1
    else:
        difference += final_list[i][0][1] - final_list[i][1][1]
        for z in range(difference + 1):
            matrix[final_list[i][0][1] -z][final_list[i][0][0]] += 1

# find every coordinate with value >= 2
counter = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] >= 2:
            counter += 1



