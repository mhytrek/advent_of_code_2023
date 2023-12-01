#Day 1 - ADVENT OF CODE 2023
import get_input


def calibration_value(line: str) -> int:
    first = 0
    last = len(line)-1
    while not line[first].isnumeric():
        first += 1
    while not line[last].isnumeric():
        last -= 1
    return (int(line[first])*10) + int(line[last])


def find_all_values(input: list) -> int:
    sum = 0
    for i in range(len(input)):
        sum += calibration_value(input[i])
    return sum


if __name__ == '__main__':
    input = get_input.download_input(1)
    print(find_all_values(input))