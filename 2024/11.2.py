from Input_helper import get_input


def parse(data):
    return [ int(d) for d in data[0].replace("\n", "").split(" ")]


def add_to_dict(key, dict,val=1):
    if dict.get(key) is None:
        dict[key] = val
    else:
        dict[key] += val
    return dict


def blink_step(table):
    new_table = {}
    for stone in table.keys():
        count = table.get(stone)

        if stone == 0:
            add_to_dict(1, new_table, count)
        elif len(str(stone)) % 2 == 0:
            middle = len(str(stone)) // 2
            add_to_dict(int(str(stone)[:middle]), new_table, count)
            add_to_dict(int(str(stone)[middle:]), new_table, count)
        else:
            add_to_dict(stone*2024, new_table, count)
    return new_table


def create_dict(data):
    dict = {}
    for a in data:
        dict = add_to_dict(a, dict)
    return dict


def loop_blinks(data, blinks):
    new_table = create_dict(data)
    for _ in range(blinks):
        new_table = blink_step(new_table)
    return  sum(new_table.values())


def main():
    get_input(11)
    file = open("input_day_11", "r")
    lines = file.readlines()
    data = parse(lines)
    return loop_blinks(data, blinks=75)


if __name__ == "__main__":
    print(main())