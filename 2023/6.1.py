
import get_input

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
    time = []
    distance = []
    line1 = lines[0][:-1].split(" ")
    for i in line1:
        if i.isnumeric():
            time.append(int(i))
    line2 = lines[1][:-1].split(" ")
    for j in line2:
        if j.isnumeric():
            distance.append(int(j))
    sum = 1
    print(time,distance)
    for i in range(len(time)):
        sum *= record(time[i],distance[i])
    return sum

lines = get_input.download_input(6)
# file = open("example_6.txt")
# lines = file.readlines()
print(lin(lines))