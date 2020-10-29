SIZE = 5

maze = [
    [0,0,0,1,1],
    [1,0,0,0,0],
    [1,0,1,0,1],
    [0,0,0,0,1],
    [1,0,1,0,0]
]

solution = [[0]*SIZE for _ in range(SIZE)]

def solvemaze(r, c, solution):
    if (r == SIZE-1) and (c == SIZE-1):
        solution[r][c] = 1
        print()
        for i in solution:
            print (i)
        return 
    
    if r < 0 or c < 0 or r >= SIZE or c >= SIZE or solution[r][c] == 1 or maze[r][c] == 1:
        return

    solution[r][c] = 1
    solvemaze(r+1, c, solution)
    # Go right
    solvemaze(r, c+1, solution)
    # Go up
    solvemaze(r-1, c, solution)
    # Go left
    solvemaze(r, c-1, solution)
    solution[r][c] = 0

solvemaze(0,0, solution)