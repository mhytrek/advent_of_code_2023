import get_input
import math

def all_Z(keys):
    for key in keys:
        if key[-1] != 'Z':
            return False
    return True
def change_lines(lines):
    ruchy = lines[0][:-1]
    nodes = {}
    pointers = []
    for i in range(2,len(lines)):
        line = lines[i].split(" ")
        nodes[line[0]] = (line[2][1:-1],line[3][:-2])
        if line[0][-1] == 'A':
            pointers.append(line[0])
    t = 0
    for p in pointers:
        pointer = p
        licznik = 0
        while pointer[-1] != 'Z':
            for i in range(len(ruchy)):
                licznik += 1
                # for p in range(len(pointers)):
                #     if ruchy[i] == 'L':
                #         pointers[p] = nodes.get(pointers[p])[0]
                #     else:
                #         pointers[p] = nodes.get(pointers[p])[1]
                if ruchy[i] == 'L':
                    pointer = nodes.get(pointer)[0]
                else:
                    pointer = nodes.get(pointer)[1]
                # if all_Z(pointers):
                #     return licznik
                if pointer[-1] == 'Z':
                    if t == 0:
                        t = licznik
                    else:
                        t = math.lcm(t,licznik)
                    break
    return t

# lines = get_input.download_input(8)
file = open("input_day_8")
lines = file.readlines()
print(change_lines(lines))