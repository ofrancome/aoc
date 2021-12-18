from utils.utils import readfile


def most_values_in_column(input_array, column):
    count = 0
    for line in input_array:
        if line[column] == "1":
            count += 1
        elif line[column] == "0":
            count -= 1
    if count > 0:
        return "1"
    elif count < 0:
        return "0"
    else:
        return "draw"


def keep_values(input_array, column, value):
    filtered_array = []
    for line in input_array:
        if line[column] == value:
            filtered_array.append(line)
    return filtered_array


def find_rating(input_array, keep_value_if_more_ones, keep_value_if_more_zeros, keep_value_if_draw):
    for x in range(len(input_array[0])):
        most_common = most_values_in_column(input_array, x)
        if most_common == "1":
            input_array = keep_values(input_array, x, keep_value_if_more_ones)
        elif most_common == "0":
            input_array = keep_values(input_array, x, keep_value_if_more_zeros)
        else:
            input_array = keep_values(input_array, x, keep_value_if_draw)
        if len(input_array) == 1:
            return input_array[0]


# lines = readfile("sample.txt")
lines = readfile("input.txt")

o2 = find_rating(lines.copy(), "1", "0", "1")
co2 = find_rating(lines.copy(), "0", "1", "0")

print(int(o2, 2) * int(co2, 2))

