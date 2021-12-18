import statistics

from utils.utils import readfile

# lines = readfile("sample.txt")
lines = readfile("input.txt")

positions = list(map(int, lines[0].split(',')))
print(positions)
median = statistics.median(positions)
fuel = 0
for position in positions:
    fuel += abs(position - median)
print(fuel)
