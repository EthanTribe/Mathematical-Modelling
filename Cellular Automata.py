import numpy as np
import matplotlib.pyplot as plt

iterations = 50
gridWidth = 49

grid = np.zeros((iterations, gridWidth))
grid[0, gridWidth//2] = 1

#       000001010011100101110111
rules = [0, 1, 1, 0, 1, 1, 0, 0]

def ApplyRule(row, column):
    ruleIndex = 0
    for n in range(3):
        ruleIndex += 2**n * grid[row, column - n + 1]
    return rules[int(ruleIndex)]

for row in range(iterations - 1): # or edges are reached
    for column in range(1, gridWidth - 1):
        grid[row + 1, column] = ApplyRule(row, column)

fig, ax = plt.subplots()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.matshow(grid, cmap = "binary", origin = "upper")
plt.show()