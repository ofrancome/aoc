import numpy as np
from utils.utils import readfile

# lines = readfile("sample.txt")
lines = readfile("input.txt")

field = np.zeros((1000, 1000))
for line in lines:
    tmp = line.split(" -> ")
    x1 = int(tmp[0].split(',')[0])
    y1 = int(tmp[0].split(',')[1])
    x2 = int(tmp[1].split(',')[0])
    y2 = int(tmp[1].split(',')[1])

    if x1 == x2:
        if y1 < y2:
            for y in range(y1, y2 + 1):
                field[x1][y] += 1
        else:
            for y in range(y2, y1 + 1):
                field[x1][y] += 1
    elif y1 == y2:
        if x1 < x2:
            for x in range(x1, x2 + 1):
                field[x][y1] += 1
        else:
            for x in range(x2, x1 + 1):
                field[x][y1] += 1
    else:
        if x1 < x2:
            if y1 < y2:
                for i in range(0, x2 - x1 + 1):
                    field[x1 + i][y1 + i] += 1
            else:
                for i in range(0, x2 - x1 + 1):
                    field[x1 + i][y1 - i] += 1
        else:
            if y1 < y2:
                for i in range(0, x1 - x2 + 1):
                    field[x1 - i][y1 + i] += 1
            else:
                for i in range(0, x1 - x2 + 1):
                    field[x1 - i][y1 - i] += 1
b = np.where(field > 1)
print(len(b[0]))
