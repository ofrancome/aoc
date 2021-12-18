import operator
from functools import reduce
import numpy as np
from utils.utils import readfile


def keep_basin_going(field, x, y, basin):
    if (x, y) not in basin:
        if field[x][y] != 9:
            basin.add((x, y))
            if x > 0:
                keep_basin_going(field, x - 1, y, basin)
            if y > 0:
                keep_basin_going(field, x, y - 1, basin)
            if x < rows - 1:
                keep_basin_going(field, x + 1, y, basin)
            if y < columns - 1:
                keep_basin_going(field, x, y + 1, basin)


def get_max_values(basins_sizes, N):
    b = basins_sizes[:]
    max_values = []
    minimum = min(b) - 1
    for _ in range(N):
        max_index = b.index(max(b))
        max_values.append(b[max_index])
        b[max_index] = minimum
    return max_values


# lines = readfile("sample.txt")
lines = readfile("input.txt")
rows = len(lines)
columns = len(lines[0])
field = np.zeros((rows, columns))
sum_of_risk_levels = 0
for i in range(rows):
    for j in range(columns):
        field[i][j] = lines[i][j]

low_points_x = []
low_points_y = []
for k in range(rows):
    for m in range(columns):
        if (k > 0 and field[k][m] >= field[k - 1][m]) or \
                (m > 0 and field[k][m] >= field[k][m - 1]) or \
                (k < rows - 1 and field[k][m] >= field[k + 1][m]) or \
                (m < columns - 1 and field[k][m] >= field[k][m + 1]):
            continue
        low_points_x.append(k)
        low_points_y.append(m)
        sum_of_risk_levels += 1 + field[k][m]

basins_sizes = []
for o in range(len(low_points_x)):
    basin = set()
    keep_basin_going(field, low_points_x[o], low_points_y[o], basin)
    basins_sizes.append(len(basin))

max_values = get_max_values(basins_sizes, 3)
print(reduce(operator.mul, max_values, 1))
