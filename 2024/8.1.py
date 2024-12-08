from adventofcode import get_input


def parse(data):
    return [[l for l in line.replace('\n', '')] for line in data]

def find_antinode(a1, a2):
    r1, r2 = (a2[0]-a1[0], a2[1]-a1[1])
    a4 = (a2[0] + r1, a2[1] + r2)
    a3 = (a1[0] - r1, a1[1] - r2)
    return a3, a4

def in_board(x_len, y_len, a):
    return 0 <= a[0] < x_len and 0 <= a[1] < y_len

def find_anthenas(data):
    x_len = len(data)
    y_len = len(data[0])
    dict = {}
    for i in range(x_len):
        for j in range(y_len):
            sym = data[i][j]
            if sym != ".":
                if dict.get(sym) is None:
                    dict[sym] = [(i, j)]
                else:
                    dict[sym] = dict.get(sym) + [(i, j)]

    antinodes = set()
    for sym in dict.keys():
        anthens = dict[sym]
        for i in range(len(anthens)-1):
            for j in range(i+1,len(anthens)):
                for node in find_antinode(anthens[i], anthens[j]):
                    if in_board(x_len, y_len, node):
                        antinodes.add(node)
    print(*antinodes, sep="\n")
    return len(antinodes)




def main():
    get_input.get_input(8)
    file = open("input_day_8", "r")
    lines = file.readlines()
    data = parse(lines)
    return find_anthenas(data)


if __name__ == "__main__":
    print(main())