from utils.utils import readfile

# lines = readfile("sample.txt")
lines = readfile("input.txt")
opening_tags = "([{<"
closing_tags = ")]}>"
illegal_score = [3, 57, 1197, 25137]
closing_score = [1, 2, 3, 4]
scores = []
for line in lines:
    stack = []
    corrupted = False
    for i in range(len(line)):
        if line[i] in opening_tags:
            stack.append(line[i])
        if line[i] in closing_tags:
            opening = stack.pop()
            if opening_tags.index(opening) != closing_tags.index(line[i]):
                corrupted = True
                break
    if not corrupted:
        score = 0
        while len(stack) != 0:
            needs_closing = stack.pop()
            score = score * 5 + closing_score[opening_tags.index(needs_closing)]
        scores.append(score)
sorted_scores = sorted(scores)
middle = int(len(scores) / 2)
print(sorted_scores[middle])
