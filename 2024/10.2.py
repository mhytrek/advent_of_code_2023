from Input_helper import get_input


def parse(data):
    return [list(map(int, list(d.replace("\n", "")))) for d in data]

def find_trailhead(data):
    trailheads = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                trailheads.append((i,j))
    return trailheads

def count_trails(data, head):
    steps = [(1,0), (0,1), (-1,0), (0,-1)]
    x, y = head

    if data[x][y] == 9:
        return 1
    else:
        sum = 0
        for step_x, step_y in steps:
            x_new = x + step_x
            y_new = y + step_y
            if 0 <= x_new < len(data) and 0 <= y_new < len(data[0]) and data[x_new][y_new] == data[x][y]+1:
                sum += count_trails(data, (x_new, y_new))
    return sum




def main():
    get_input(10)
    file = open("input_day_10", "r")
    lines = file.readlines()
    data = parse(lines)
    trailheads = find_trailhead(data)
    sum = 0
    for trailhead in trailheads:
        a = count_trails(data, trailhead)
        sum += a
    return sum



if __name__ == "__main__":
    print(main())