import get_input

def change_lines(lines):
    ruchy = lines[0][:-1]
    print(ruchy)
    nodes = {}
    for i in range(2,len(lines)):
        line = lines[i].split(" ")
        print(line)
        nodes[line[0]] = (line[2][1:-1],line[3][:-2])
    pointer = 'AAA'
    licznik = 0
    while pointer != 'ZZZ':
        for i in range(len(ruchy)):
            licznik += 1
            if ruchy[i] == 'L':
                pointer = nodes.get(pointer)[0]
            else:
                pointer = nodes.get(pointer)[1]
            if pointer == 'ZZZ':
                break
    return licznik

lines = get_input.download_input(8)
# file = open("example_8.txt")
# lines = file.readlines()
print(change_lines(lines))