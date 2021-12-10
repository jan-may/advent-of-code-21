from collections import deque
from statistics import median_low

def open_file(file_name):
    with open(file_name) as f:
        return f.read().split()

input = open_file('input.txt')
closing_chars = [")", "}", "]", ">"]

################################ Task 1 ################################
def find_corupted_lines(input, closing_chars):
    wrong_chars = []
    
    for i in input:
        stack=deque()
        for j in i:
            if j not in closing_chars:
                stack.append(j)
            elif j == ")" and stack[-1] == "(":
                stack.pop()
            elif j == "}" and stack[-1] == "{":
                stack.pop()
            elif j == "]" and stack[-1] == "[":
                stack.pop()
            elif j == ">" and stack[-1] == "<":
                stack.pop()
            else:
                wrong_chars.append(j)
                stack.clear()
                break

        if len(stack) > 0:
            incomplete_lines.append(stack)
    return wrong_chars

def calculate_score(lst):
    sum = 0
    for char in lst:
        if char == ")":
            sum += 3
        elif char == "]":
            sum += 57
        elif char == "}":
            sum += 1197
        elif char == ">":
            sum += 25137
    return sum


################################ Task 2 ################################
incomplete_lines = []

def task2_score():
    score_lst = []
    find_corupted_lines(input, closing_chars)
    for line in list(incomplete_lines):
        score = 0 
        for i in range(len(line)-1, -1, -1):
            if line[i] == "(":
                score *= 5
                score += 1
            elif line[i] == "[":
                score *= 5
                score += 2
            elif line[i] == "{":
                score *= 5
                score += 3
            elif line[i] == "<":
                score *= 5
                score += 4
        score_lst.append(score)
    return median_low(score_lst)

print(calculate_score(find_corupted_lines(input, closing_chars)))
print(task2_score())

