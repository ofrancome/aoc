import sys


def increases(given_measures, offset):
    count = 0

    for x in range(0, len(given_measures) - offset):
        if given_measures[x] < given_measures[x + offset]:
            count += 1
    return count


print(sys.argv)
with open("input.txt") as f:
# with open("sample.txt") as f:
    lines = f.read().splitlines()

measures = [int(depth) for depth in lines]

print(increases(measures, 1))
print(increases(measures, 3))

