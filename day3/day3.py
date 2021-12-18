from utils.utils import readfile, bit_list_to_int

# lines = readfile("sample.txt")
lines = readfile("input.txt")
gamma_bit = [0] * len(lines[0])
for line in lines:
    for i in range(len(line)):
        if line[i] == "1":
            gamma_bit[i] += 1
        elif line[i] == "0":
            gamma_bit[i] -= 1

for x in range(len(gamma_bit)):
    if gamma_bit[x] > 0:
        gamma_bit[x] = 1
    elif gamma_bit[x] < 0:
        gamma_bit[x] = 0

gamma = bit_list_to_int(gamma_bit)
max_value = pow(2, len(gamma_bit)) - 1
epsilon = max_value - gamma
print(gamma)
print(epsilon)
print(gamma * epsilon)
