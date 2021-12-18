from utils.utils import readfile

# lines = readfile("sample.txt")
lines = readfile("input.txt")


fishes = list(map(int, lines[0].split(",")))

for i in range(80):
    fishes_born = 0
    for x in range(len(fishes)):
        if fishes[x] == 0:
            fishes_born += 1
            fishes[x] = 6
        else:
            fishes[x] -= 1
    for j in range(fishes_born):
        fishes.append(8)

print(len(fishes))
