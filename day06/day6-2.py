from collections import Counter
from utils.utils import readfile

# lines = readfile("sample.txt")
lines = readfile("input.txt")

fishes = list(map(int, lines[0].split(",")))
nb_fish = Counter(fishes)
print(nb_fish)
for i in range(256):
    fishes_born = nb_fish[0]
    nb_fish[0] = nb_fish[1]
    nb_fish[1] = nb_fish[2]
    nb_fish[2] = nb_fish[3]
    nb_fish[3] = nb_fish[4]
    nb_fish[4] = nb_fish[5]
    nb_fish[5] = nb_fish[6]
    nb_fish[6] = nb_fish[7]
    nb_fish[7] = nb_fish[8]
    nb_fish[6] += fishes_born
    nb_fish[8] = fishes_born

print(sum(nb_fish.values()))

