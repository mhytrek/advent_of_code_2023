from Input_helper import get_input
import re

def parse(d):
    index = d.index("\n")
    designs = [design for design in ("".join(d[:index])).replace("\n", "").split(", ")]
    wanted = [design.replace("\n", "") for design in d[index+1:]]
    return designs, wanted


def find_onsen(pattern, set_designs):
    table = [0 for _ in range(len(pattern))]
    for i in range(len(table)):
        j = i - 1
        while j >= -1:
            if j == -1:
                design = pattern[j + 1: i + 1]
                if design in set_designs:
                    table[i] += 1
            elif table[j] != 0:
                design = pattern[j+1:i+1]
                if design in set_designs:
                    table[i] += table[j]
            j -= 1
    return table[-1]


def main():
    get_input(19)
    file = open("input_day_19", "r")
    lines = file.readlines()
    designs, wanted = parse(lines)

    sum = 0
    for w in wanted:
        print(w)
        sum += find_onsen(w, designs)
    return sum





if __name__ == "__main__":
    print(main())
