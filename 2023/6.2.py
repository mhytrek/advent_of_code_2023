
import get_input
import math

def record(t,d):
    r = {}
    s=0
    for i in range(1,t):
        if i*(t-i)>d:
            if r.get(i) == None:
                r[i]=1
                s += 1
    return s

def lin(lines):
    time = ""
    distance = ""
    line1 = lines[0][:-1].split(" ")
    for i in line1:
        if i.isnumeric():
            time += i
    line2 = lines[1][:-1].split(" ")
    for j in line2:
        if j.isnumeric():
            distance += j
    return record(int(time),int(distance))


# lines = get_input.download_input(6)
file = open("input_day_6")
lines = file.readlines()
print(lin(lines))