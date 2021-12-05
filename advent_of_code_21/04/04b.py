import utils
from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

input = utils.readFile(r"...\advent_of_code_21\04\input.txt")

numbers = [37,60,87,13,34,72,45,49,61,27,97,88,50,30,76,40,63,9,38,67,82,6,59,90,99,54,11,66,98,23,64,14,18,4,10,89,46,32,19,5,1,53,25,96,2,12,86,58,41,68,95,8,7,3,85,70,35,55,77,44,36,51,15,52,56,57,91,16,71,92,84,17,33,29,47,75,80,39,83,74,73,65,78,69,21,42,31,93,22,62,24,48,81,0,26,43,20,28,94,79]

lst_temp = [i for i in input if i != ""]
final_list = [lst_temp[x:x+5] for x in range(0, len(lst_temp), 5)]
final_list2 = [lst_temp[x:x+5] for x in range(0, len(lst_temp), 5)]

# format data in 5x5 lists
for i in range(len(final_list)):
    for y in range(len(final_list[i])):
        final_list[i][y] = (final_list[i][y].split())

# calculate the value of the ramaining cells in the board
def calc_remaining_board_value(board):
    score = 0
    for i in board:
        for num in i:
            if num != "X":
                score += int(num)
    return score

def find_last_winning_board(final_list, numbers):
    bu_lst = final_list
    winning_board = []
    last_added = []
    for number in numbers:
        if(len(winning_board) == len(bu_lst)):
            return calc_remaining_board_value(last_added * numbers[(numbers.index(number)-1)])
        for i in range(len(final_list)):
            for y in range(len(final_list[i])):
                row_counter = 0
                if all_equal(final_list[i][y]) and final_list[i] not in winning_board:
                    winning_board.append(final_list[i])
                    last_added = bu_lst[i]
                for z in range(len(final_list[i][y])):
                    if final_list[i][y][z] == str(number):
                        final_list[i][y][z] = "X"
                    if final_list[i][z][y] == "X":
                        row_counter+=1
                    if row_counter == 5 and final_list[i] not in winning_board:
                        winning_board.append(final_list[i])
                        last_added = bu_lst[i]
                       
print(find_last_winning_board(final_list, numbers))