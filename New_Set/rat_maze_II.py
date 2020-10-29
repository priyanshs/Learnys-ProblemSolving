from copy import deepcopy
SIZE = 5

maze = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

lens = list()

def solvemaze(r, c, solution, length):
    if (r == SIZE-1) and (c == SIZE-1):
        
        solution[r][c] = 1
        temp = deepcopy(solution)
        lens.append([length, temp])

        return 

    if r < 0 or c < 0 or r >= SIZE or c >= SIZE or solution[r][c] == 1 or maze[r][c] == 1:
        return

    solution[r][c] = 1
    solvemaze(r+1, c, solution, length+1)
    # Go right
    solvemaze(r, c+1, solution, length+1)
    # Go up
    solvemaze(r-1, c, solution, length+1)
    # Go left
    solvemaze(r, c-1, solution, length+1)
    solution[r][c] = 0
    length -= 1

sols = [[0]*SIZE for _ in range(SIZE)]
solvemaze(0,0, sols, 0)
print(min(lens))