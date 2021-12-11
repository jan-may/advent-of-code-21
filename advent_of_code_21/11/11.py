def readInput(filename):
    with open(filename) as f:
        input = [[int(i) for i in row] for row in f.read().splitlines()]
    return input
        
matrix = readInput('input.txt')

# get adjacent cells to a cell
def getadjcells(arr, i , j):
    possible_adjcells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    adj_cells = []
    for tuple in possible_adjcells:
        if 0 <= i + tuple[0] <= len(arr) -1 and 0 <= j + tuple[1] <= len(arr[0]) -1:
            adj_cells.append((i + tuple[0], j + tuple[1]))
    return(adj_cells)

# increment all cells by 1 if cell == 0 append to coordinates to flashing
# return matrix & flashing coordinates
def incrementby1(arr):
    flashing_octopi = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = (arr[i][j] + 1)%10
            if arr[i][j] == 0:
                flashing_octopi.append((i,j))
    return(arr, flashing_octopi)

# find neighbors of flashing octopi & check if they are flashing
def flashes(arr, flashing):
    for flash in flashing:
        neighbors = getadjcells(arr, flash[0], flash[1])
        for x , y in neighbors:
            if arr[x][y] != 0:
                arr[x][y] = (arr[x][y]+1)%10
                if arr[x][y] == 0:
                    flashing.append((x,y))
            else:
                arr[x][y] = 0
    return(arr)

steps = 0
num_zeros = 0

# find steps until all cells have just flashed
while num_zeros != 100:
    matrix, flashing_octopi = incrementby1(matrix)
    matrix = flashes(matrix, flashing_octopi)
    num_zeros = sum(sum(True for i in row if not i) for row in matrix)
    steps += 1

print(steps)





