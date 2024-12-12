from math import log10

from Input_helper import get_input


def parse(data):
    return [ int(d) for d in data[0].replace("\n", "").split(" ")]

def blink_step(table):
    new_table = []
    for stone in table:
        if stone == 0:
            new_table.append(1)
        elif len(str(stone)) % 2 == 0:
            middle = len(str(stone)) // 2
            new_table.append(int(str(stone)[:middle]))
            new_table.append(int(str(stone)[middle:]))
        else:
            new_table.append(stone*2024)
    print(len(new_table))
    return new_table


def loop_blinks(data, blinks):
    new_table = data
    for _ in range(blinks):
        new_table = blink_step(new_table)
    return len(new_table)


def main():
    get_input(11)
    file = open("input_day_11", "r")
    lines = file.readlines()
    data = parse(lines)
    return loop_blinks(data, blinks=10)


if __name__ == "__main__":
    print(main())