from Input_helper import get_input
import re

def parse(d):
    parsed = []
    for line in d:
        num = re.findall(r'-?\d+', line)
        parsed.append(list(map(int,num)))
    return parsed


def find_safety(data, wide=101, tall=103, mul=100):

    def add_to_q(x1, y1):
        i = 0
        if x1 == wide //2 or y1 == tall//2:
            return 4
        if x1 > wide //2:
            i += 1
        if y1 > tall //2:
            i += 2
        return i


    q = [0,0,0,0,0] # q1, q2, q3, q4, no_count
    for px, py, vx, vy in data:
        x = (px + (mul * vx) ) % wide
        y = (py + (mul * vy) ) % tall
        i = add_to_q(x, y)
        q[i] += 1

    safety = 1
    for val in q[:-1]:
        safety *= val

    return safety


def main():
    get_input(14)
    file = open("input_day_14", "r")
    lines = file.readlines()
    data = parse(lines)
    return find_safety(data, 101, 103)


if __name__ == "__main__":
    print(main())
