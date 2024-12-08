def check_rows(pattern):
    if len(pattern) % 2 == 0:
        half = len(pattern)//2
        for i in range(len(pattern[0])):
            for j in range(0,half):
                if pattern[j][i] != pattern[-j-1][i]:
                    return 0
        return half
    return 0

def check_cols(pattern):
    if len(pattern[0]) % 2 == 0:
        half = len(pattern[0])//2
        for i in range(len(pattern)):
            for j in range(0,half):
                if pattern[i][j] != pattern[i][-j-1]:
                    return 0
        return half
    return 0

def reflections(pattern):
    r = check_rows(pattern)
    if r > 0:
        return r*100
    for i in range(1,len(pattern)-1):
        r = check_rows(pattern[i:])
        if r > 0:
            return (r+i) * 100
        r = check_rows(pattern[:-i])
        if r > 0:
            return r * 100
    r = check_cols(pattern)
    if r > 0:
        return r
    for i in range(1, len(pattern[0]) - 1):
        r = check_cols([pattern[j][i:] for j in range(len(pattern))])
        if r > 0:
            return r + i
        r = check_cols([pattern[j][:-i] for j in range(len(pattern))])
        if r > 0:
            return r
    return 0

def split_patterns(lines):
    sum = 0
    pattern = []
    for line in lines:
        if line == "\n":
            sum += reflections(pattern)
            print(sum)
            pattern = []
        else:
            pattern.append([line[i] for i in range(len(line)-1)])
    sum += reflections(pattern)
    print(sum)
    return sum

file = open("example_13.txt")
lines = file.readlines()
print(split_patterns(lines))
