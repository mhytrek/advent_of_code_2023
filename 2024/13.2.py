from Input_helper import get_input
import re
import numpy as np


def get_data(sym, sign, data):
    if sign == '+':
        x = re.findall(rf'{sym}\+\d+', data)
    else:
        x = re.findall(rf'{sym}{sign}\d+', data)
    return int(x[0].split(f"{sign}")[1])


def parse(data):
    d = []
    for i in range(0,len(data), 4):
        A_x = get_data("X", "+", data[i])
        A_y = get_data("Y", "+", data[i])

        B_x = get_data("X", "+", data[i+1])
        B_y = get_data("Y", "+", data[i+1])

        P_x = get_data("X", "=", data[i+2])
        P_y = get_data("Y", "=", data[i+2])

        d.append([(A_x,A_y),(B_x,B_y),(P_x,P_y)])
    return d


def count_tokens(data):
    t = 0
    for machine in data:
        a, b, prize = machine
        matrix = np.array([[a[0], b[0]], [a[1], b[1]]])
        result = np.array([prize[0] + 10000000000000, prize[1] + 10000000000000])

        A, B = np.linalg.solve(matrix, result)

        if round(A,4) % 1 == 0 and round(B,4) % 1 == 0:
            print(machine)
            t += 3*A + B

    return t


def main():
    get_input(13)
    file = open("input_day_13", "r")
    lines = file.readlines()
    data = parse(lines)
    return count_tokens(data)


if __name__ == "__main__":
    print(main())
