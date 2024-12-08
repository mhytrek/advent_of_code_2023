import Input_helper
import re


def sum_mul(data):
    sum = 0
    for line in data:
        multiplications = re.findall(r'mul\(\d+,\d+\)', line)
        for mul in multiplications:
            d1, d2 = list(map(int, mul.replace("mul(", "").replace(")", "").split(",")))
            sum += d1 * d2
            print(d1, d2)
    return sum


def sum_mul_2(data):
    data = "".join(data)
    sum = 0
    delimeter = ["do()", "don't()"]
    i = 1
    while len(data.split(delimeter[i], 1)) > 1:
        check, new = data.split(delimeter[i], 1)
        if i == 1:
            sum += sum_mul([check])
        i = (i + 1) % 2
        data = new
    if i == 1:
        sum += sum_mul([new])
    return sum


def main():
    file = open("input_day_3", "r")
    lines = file.readlines()
    sum = sum_mul_2(lines)
    print(sum)


if __name__ == "__main__":
    print(main())