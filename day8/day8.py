from utils.utils import readfile

# lines = readfile("sample.txt")
lines = readfile("input.txt")

unique_count = 0
for line in lines:
    signals = line.split('|')[0].strip().split()
    outputs = line.split('|')[1].strip().split()

    # Possibilities:
    #
    #  0000
    # 1    2
    # 1    2
    #  3333
    # 4    5
    # 4    5
    #  6666

    possibilities = ['abcdefg'] * 7
    for signal in signals:
        if len(signal) == 2:  # Case 1
            possibilities[0] = ''.join(filter(lambda char: char not in signal, possibilities[0]))
            possibilities[1] = ''.join(filter(lambda char: char not in signal, possibilities[1]))
            possibilities[2] = ''.join(filter(lambda char: char in signal, possibilities[2]))
            possibilities[3] = ''.join(filter(lambda char: char not in signal, possibilities[3]))
            possibilities[4] = ''.join(filter(lambda char: char not in signal, possibilities[4]))
            possibilities[5] = ''.join(filter(lambda char: char in signal, possibilities[5]))
            possibilities[6] = ''.join(filter(lambda char: char not in signal, possibilities[6]))
        elif len(signal) == 3:  # Case 7
            possibilities[0] = ''.join(filter(lambda char: char in signal, possibilities[0]))
            possibilities[1] = ''.join(filter(lambda char: char not in signal, possibilities[1]))
            possibilities[2] = ''.join(filter(lambda char: char in signal, possibilities[2]))
            possibilities[3] = ''.join(filter(lambda char: char not in signal, possibilities[3]))
            possibilities[4] = ''.join(filter(lambda char: char not in signal, possibilities[4]))
            possibilities[5] = ''.join(filter(lambda char: char in signal, possibilities[5]))
            possibilities[6] = ''.join(filter(lambda char: char not in signal, possibilities[6]))
        elif len(signal) == 4:  # Case 4
            possibilities[0] = ''.join(filter(lambda char: char not in signal, possibilities[0]))
            possibilities[1] = ''.join(filter(lambda char: char in signal, possibilities[1]))
            possibilities[2] = ''.join(filter(lambda char: char in signal, possibilities[2]))
            possibilities[3] = ''.join(filter(lambda char: char in signal, possibilities[3]))
            possibilities[4] = ''.join(filter(lambda char: char not in signal, possibilities[4]))
            possibilities[5] = ''.join(filter(lambda char: char in signal, possibilities[5]))
            possibilities[6] = ''.join(filter(lambda char: char not in signal, possibilities[6]))
        elif len(signal) == 5:  # Case 2 / 3 / 5 -> 0-3-6 always up
            possibilities[0] = ''.join(filter(lambda char: char in signal, possibilities[0]))
            possibilities[3] = ''.join(filter(lambda char: char in signal, possibilities[3]))
            possibilities[6] = ''.join(filter(lambda char: char in signal, possibilities[6]))
        elif len(signal) == 6:  # Case 0 / 6 / 9 -> 0-1-5-6 always up
            possibilities[0] = ''.join(filter(lambda char: char in signal, possibilities[0]))
            possibilities[1] = ''.join(filter(lambda char: char in signal, possibilities[1]))
            possibilities[5] = ''.join(filter(lambda char: char in signal, possibilities[5]))
            possibilities[6] = ''.join(filter(lambda char: char in signal, possibilities[6]))
    for i in range(7):
        if len(possibilities[i]) == 1:
            for j in range(7):
                if possibilities[j] != possibilities[i]:
                    possibilities[j] = ''.join(filter(lambda char: char not in possibilities[i], possibilities[j]))
    output_value_str = ''
    for output in outputs:
        if len(output) == 2:
            output_value_str += '1'
        elif len(output) == 3:
            output_value_str += '7'
        elif len(output) == 4:
            output_value_str += '4'
        elif len(output) == 5:
            if output.find(possibilities[1]) != -1:
                output_value_str += '5'
            elif output.find(possibilities[4]) != -1:
                output_value_str += '2'
            else:
                output_value_str += '3'
        elif len(output) == 6:
            if output.find(possibilities[3]) == -1:
                output_value_str += '0'
            elif output.find(possibilities[2]) == -1:
                output_value_str += '6'
            else:
                output_value_str += '9'
        else:
            output_value_str += '8'
    unique_count += int(output_value_str)
print(unique_count)

