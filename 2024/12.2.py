from math import log10

from Input_helper import get_input


def parse(data):
    return [[d for d in line.replace("\n", "")] for line in data]


def find_regions(data):
    def in_table(i,j):
        return 0 <= i < x_len and 0 <= j < y_len

    def check_neighbours(x_now, y_now, i, j, sym):
        return not (in_table(x_now + i, y_now + j) and data[x_now + i][y_now + j] == sym)


    def count_cost(x_now, y_now, sym, area = 0, sides = 0, sides_dict=None):
        area += 1
        visited[x_now][y_now] = True

        for x_plus, y_plus in steps:
            x_new = x_now + x_plus
            y_new = y_now + y_plus
            if in_table(x_new, y_new) and data[x_new][y_new] == sym and not visited[x_new][y_new]:
                a, s = count_cost(x_new, y_new, sym)
                area += a
                sides += s
            elif not (in_table(x_new, y_new) and data[x_new][y_new] == sym):
                a = neighbours.index((x_plus, y_plus))
                x1 = neighbours[(a-1) % len(neighbours)]
                x2 = neighbours[(a-2) % len(neighbours)]
                x3 = neighbours[(a+1) % len(neighbours)]
                x4 =  neighbours[(a+2) % len(neighbours)]

                check_x1 = check_neighbours(x_now,y_now, x1[0], x1[1], sym)
                check_x2 = check_neighbours(x_now,y_now, x2[0], x2[1], sym)
                check_x3 = check_neighbours(x_now,y_now, x3[0], x3[1], sym)
                check_x4 = check_neighbours(x_now,y_now, x4[0], x4[1], sym)

                if check_x1 == check_x2 or check_x2:
                    sides += 1/2
                if check_x3 == check_x4 or check_x4:
                    sides += 1/2
        return area, sides


    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighbours = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
    x_len = len(data)
    y_len = len(data[0])

    visited = [[False for _ in range(y_len)] for _ in range(x_len)]

    sum = 0
    for x in range(x_len):
        for y in range(y_len):
            if not visited[x][y]:
                area, sides = count_cost(x,y,data[x][y])
                sum += area * (sides)
    return int(sum)



def main():
    get_input(12)
    file = open("input_day_12", "r")
    lines = file.readlines()
    data = parse(lines)
    return find_regions(data)



if __name__ == "__main__":
    print(main())