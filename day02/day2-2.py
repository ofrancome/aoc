from utils.utils import readfile

lines = readfile("input.txt")
# lines = readfile("sample.txt")
hor = 0
depth = 0
aim = 0

for line in lines:
    direction = line.split()[0]
    value = int(line.split()[1])
    if direction == "forward":
        hor += value
        depth += aim * value

    elif direction == "up":
        aim -= value

    elif direction == "down":
        aim += value

print("hor: " + str(hor) + " - depth: " + str(depth))
print(hor * depth)
