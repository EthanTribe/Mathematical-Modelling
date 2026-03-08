grid = [0] * 11
grid[5] = 1

#       000001010011100101110111
rules = [0, 1, 1, 0, 1, 1, 0, 0]

for t in range (50): # or edges are reached

    print(grid)
    newGrid = grid.copy()

    for i in range(len(grid) - 2):
        ruleIndex = grid[i-1] * 4 + grid[i] * 2 + grid[i+1]
        newGrid[i] = rules[ruleIndex]
    
    grid = newGrid.copy()
