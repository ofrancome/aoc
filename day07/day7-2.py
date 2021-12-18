import statistics

from utils.utils import readfile

# lines = readfile("sample.txt")
lines = readfile("input.txt")

positions = list(map(int, lines[0].split(',')))
mean = round(statistics.mean(positions))
lower_mean_fuel = 0
higher_mean_fuel = 0
for position in positions:
    lower_steps = abs(position - mean)
    lower_mean_fuel += lower_steps * (lower_steps + 1) / 2
    higher_steps = abs(position - mean + 1)
    higher_mean_fuel += higher_steps * (higher_steps + 1) / 2
print(lower_mean_fuel, higher_mean_fuel)
print(min(lower_mean_fuel, higher_mean_fuel))
