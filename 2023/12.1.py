from copy import deepcopy

def count(line, expected):
    curr = 0
    for i in range(len(line)):
        if line[i] == "#":
            curr += 1
        elif curr != 0:
            if len(expected) == 0 or expected.pop(0) != curr:
                return 0
            curr = 0
    if curr != 0:
        if len(expected) == 0 or expected.pop(0) != curr:
            return 0
    if len(expected) == 0:
        return 1
    return 0

def change_lines(lines):
    results = []
    springs = []
    for line in lines:
        splited = line[:-1].split(" ")
        results.append(splited[1].split(","))
        springs.append([splited[0][i] for i in range(len(splited[0]))])
    return results, springs

def possible_springs(spring,i):
    for j in range(i,len(spring)):
        if spring[j] == "?":
            new_spring1 = spring[:j] + ["."] + spring[j+1:]
            new_spring2 = spring[:j] + ["#"] + spring[j + 1:]
            return possible_springs(new_spring1,j+1) + possible_springs(new_spring2,j+1)
    return [spring]

def main(lines):
    results, springs = change_lines(lines)
    sum = 0
    for line in range(len(springs)):
        sum1 = 0
        poss = possible_springs(springs[line],0)
        for possibilities in poss:
            copy = [int(results[line][i]) for i in range(len(results[line]))]
            sum1 += count(possibilities,copy)
        sum += sum1
    return sum

file = open("example_12.txt")
lines = file.readlines()
print(main(lines))