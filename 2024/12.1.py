from math import log10

from Input_helper import get_input


def parse(data):
    return [[d for d in line.replace("\n", "")] for line in data]



def find_regions(data):
    def in_table(i,j):
        return 0 <= i < x_len and 0 <= j < y_len

    def count_cost(x_now, y_now, sym, area = 0, perimeter = 0):
        area += 1
        visited[x_now][y_now] = True

        for x_plus, y_plus in steps:
            x_new = x_now + x_plus
            y_new = y_now + y_plus
            if in_table(x_new, y_new) and data[x_new][y_new] == sym and not visited[x_new][y_new]:
                a, p = count_cost(x_new, y_new, sym)
                area += a
                perimeter += p
            elif not (in_table(x_new, y_new) and data[x_new][y_new] == sym):
                perimeter += 1
        return area, perimeter


    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    x_len = len(data)
    y_len = len(data[0])

    visited = [[False for _ in range(y_len)] for _ in range(x_len)]

    sum = 0
    for x in range(x_len):
        for y in range(y_len):
            if not visited[x][y]:
                area, perimeter = count_cost(x,y,data[x][y])
                sum += area * perimeter
    return sum



def main():
    get_input(12)
    file = open("input_day_12", "r")
    lines = file.readlines()
    data = parse(lines)
    return find_regions(data)



if __name__ == "__main__":
    print(main())