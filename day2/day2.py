from utils.utils import readfile

lines = readfile("input.txt")
# lines = readfile("sample.txt")
hor = 0
depth = 0

for line in lines:
    direction = line.split()[0]
    if direction == "forward":
        hor += int(line.split()[1])

    elif direction == "up":
        depth -= int(line.split()[1])

    elif direction == "down":
        depth += int(line.split()[1])

print("hor: " + str(hor) + " - depth: " + str(depth))
print(hor * depth)
