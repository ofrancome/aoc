import numpy as np

from utils.utils import readfile


def do_flash(octopuses_energy, k, m, octopuses_flashes):
    octopuses_flashes[k][m] = 1
    if k > 0 and m > 0:
        octopuses_energy[k - 1][m - 1] += 1
    if k > 0:
        octopuses_energy[k - 1][m] += 1
    if m > 0:
        octopuses_energy[k][m - 1] += 1
    if k > 0 and m < len(octopuses_energy[0]) - 1:
        octopuses_energy[k - 1][m + 1] += 1
    if k < len(octopuses_energy) - 1 and m > 0:
        octopuses_energy[k + 1][m - 1] += 1
    if k < len(octopuses_energy) - 1 and m < len(octopuses_energy[0]) - 1:
        octopuses_energy[k + 1][m + 1] += 1
    if k < len(octopuses_energy) - 1:
        octopuses_energy[k + 1][m] += 1
    if m < len(octopuses_energy[0]) - 1:
        octopuses_energy[k][m + 1] += 1


# lines = readfile("sample.txt")
lines = readfile("input.txt")
rows = len(lines)
columns = len(lines[0])
octopuses_energy = np.zeros((rows, columns))
for i in range(rows):
    for j in range(columns):
        octopuses_energy[i][j] = int(lines[i][j])

flashes = 0
step = 0
while True:
    step += 1
    step_flashes = 0
    octopuses_flashes = np.zeros((rows, columns))
    octopuses_energy = np.add(octopuses_energy, np.ones((rows, columns)))

    energy_flash = octopuses_energy[octopuses_energy > 9]
    # print(energy_flash)
    flash = len(energy_flash) > 0
    while flash:
        flash = False
        for k in range(rows):
            for m in range(columns):
                if octopuses_energy[k][m] > 9 and octopuses_flashes[k][m] == 0:
                    flash = True
                    step_flashes += 1
                    do_flash(octopuses_energy, k, m, octopuses_flashes)
                    break
            if flash:
                break
    unflashed_octopus = octopuses_flashes[octopuses_flashes == 0]
    if len(unflashed_octopus) == 0:
        print("All octopuses flashed in step ", step)
        break

    for n in range(rows):
        for o in range(columns):
            if octopuses_flashes[n][o] == 1:
                octopuses_energy[n][o] = 0
