def change(sym, sum):
    sum += ord(sym)
    sum *= 17
    sum = sum % 256
    return sum

def bokk_hash(line):
    input = line[0][:-1].split(",")
    result = 0
    for string in input:
        sum = 0
        for char in string:
            sum = change(char,sum)
        result += sum
    return result

file = open("example_15.txt")
lines = file.readlines()
print(bokk_hash(lines))