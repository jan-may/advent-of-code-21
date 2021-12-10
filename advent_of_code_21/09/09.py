def readInput(input):
    with open(input) as f:
        string = f.read().strip()
        # transform string into int matrix
        return [list((line)) for line in string.split('\n')]

input = readInput('input.txt')


# killed the code from part1 while trying to figure out task 2... no time to fix it 😔
# at least got 1 star 🎉

def task1(matrix):
    sum = 0
    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            if i == 0:
                if y == 0 and matrix[i][y] < matrix[i+1][y] and matrix[i][y] < matrix[i][y+1]:
                    sum += int(matrix[i][y]) + 1
                elif y > 0 and y < len(matrix[i]) - 1 and matrix[i][y] < matrix[i+1][y] and matrix[i][y] < matrix[i][y+1] and matrix[i][y] < matrix[i][y-1]:
                    sum += int(matrix[i][y]) + 1
                elif y == len(matrix[i]) - 1 and matrix[i][y] < matrix[i+1][y] and matrix[i][y] < matrix[i][y-1]:
                    sum += int(matrix[i][y]) + 1
            if i > 0 and i < len(matrix) - 1:
                if y == 0 and matrix[i][y] < matrix[i+1][y] and matrix[i][y] < matrix[i-1][y] and matrix[i][y] < matrix[i][y+1]:
                    sum += int(matrix[i][y]) + 1
                elif y > 0 and y < len(matrix[i]) - 1 and matrix[i][y] < matrix[i+1][y] and matrix[i][y] < matrix[i-1][y] and matrix[i][y] < matrix[i][y+1] and matrix[i][y] < matrix[i][y-1]:
                    sum += int(matrix[i][y]) + 1
                elif y == len(matrix[i]) - 1 and matrix[i][y] < matrix[i+1][y] and matrix[i][y] < matrix[i-1][y] and matrix[i][y] < matrix[i][y-1]:
                    sum += int(matrix[i][y]) + 1
            if i == len(matrix) - 1:
                if y == 0 and matrix[i][y] < matrix[i-1][y] and matrix[i][y] < matrix[i][y+1]:
                    sum += int(matrix[i][y]) + 1
                elif y > 0 and y < len(matrix[i]) - 1 and matrix[i][y] < matrix[i-1][y] and matrix[i][y] < matrix[i][y+1] and matrix[i][y] < matrix[i][y-1]:
                    sum += int(matrix[i][y]) + 1
                elif y == len(matrix[i]) - 1 and matrix[i][y] < matrix[i-1][y] and matrix[i][y] < matrix[i][y-1]:
                    sum += int(matrix[i][y]) + 1
    return sum

print(task1(input))