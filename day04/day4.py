import numpy as np
from utils.utils import readfile


def calc_score(board, current_pick, already_picked):
    sum_of_unmarked = 0
    for iy, ix in np.ndindex(board.shape):
        if board[iy][ix] not in already_picked and board[iy][ix] != current_pick:
            sum_of_unmarked += int(board[iy][ix])
    return sum_of_unmarked * int(current_pick)


# lines = readfile("sample.txt")
lines = readfile("input.txt")

picks = lines[0]
board_lines = lines[1:]
boards = []
boards_picks = []
for x in range(1, len(lines), 6):
    board = np.array([
        lines[x+1].split(),
        lines[x+2].split(),
        lines[x+3].split(),
        lines[x+4].split(),
        lines[x+5].split(),
    ])
    boards.append(board)
    board_pick = np.zeros(10)
    boards_picks.append(board_pick)

already_picked = []
for pick in picks.split(','):
    marked_for_deletion = []
    for i in range(len(boards)):
        X, Y = np.where(boards[i] == pick)
        for j in range(len(X)):
            boards_picks[i][X[j]] += 1
            boards_picks[i][5 + Y[j]] += 1
            if boards_picks[i][X[j]] == 5 or boards_picks[i][5 + Y[j]] == 5:
                if len(boards) == 1:
                    print(calc_score(boards[i], pick, already_picked))
                    exit(0)
                else:
                    marked_for_deletion.append(i)
    for index in reversed(marked_for_deletion):
        boards.pop(index)
        boards_picks.pop(index)
    already_picked.append(pick)
