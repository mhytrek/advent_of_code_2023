import get_input

def change_to_int(l):
    for i in range(len(l)):
        l[i]=int(l[i])
    return l
def proces(line,seeds, cch):
    for i in range(len(seeds)):
        if cch[i]:
            r = seeds[i] - line[1]
            if r >= 0 and r < line[2]:
                seeds[i]=line[0]+r
                cch[i]=False
    return seeds,cch


def change(lines):
    seeds = lines[0][:-1].split(" ")[1:]
    can_change = [True for _ in range(len(seeds))]
    seeds = change_to_int(seeds)
    for line in lines[1:]:
        line = line[:-1]
        line = line.split(" ")
        if len(line)==2:
            print(seeds)
            can_change = [True for _ in range(len(seeds))]
        elif len(line)==1 or len(line)==0:
            can_change = [True for _ in range(len(seeds))]
            continue
        else:
            line = change_to_int(line)
            seeds, can_change = proces(line,seeds, can_change)
    return min(seeds)

lines = get_input.download_input(5)
# file = open("example_5.txt")
# lines = file.readlines()
print(change(lines))