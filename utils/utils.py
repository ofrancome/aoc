def readfile(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return lines
