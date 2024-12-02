from adventofcode import get_input

def parse_data(lines):
    data = [list(map(int,line.replace("\n", "").split(" "))) for line in lines]
    return data

def sign(a):
    if a < 0:
        return -1
    else:
        return 1


def check_line(line, sym):
    for a in line:
        if not (0 < abs(a) <= 3 and sign(a) == sym):
            return False
    return True


def check_diff(data):
    safe = 0
    for line in data:
        diff = [line[i] - line[i-1] for i in range(1, len(line))]
        sym = sign(diff[-1])
        if check_line(diff, sym):
            safe += 1
    return safe


def check_diff_2(data):
    safe = 0
    for line in data:
        count = 0
        for i in range(len(line)):
            new_line = line[0:i] + line[i+1:]
            diff = [new_line[i] - new_line[i-1] for i in range(1, len(new_line))]
            sym = sign(diff[-1])
            if check_line(diff, sym):
                count += 1
        if count > 0:
            safe += 1
    return safe



def main():
    file = open("input_day_2", "r")
    lines = file.readlines()
    data = parse_data(lines)
    return check_diff_2(data)


if __name__ == "__main__":
    get_input.get_input(2)
    print(main())