import Input_helper

def parse(data):
    data = [[r.replace("\n", "").split(" ") for r in line.split(": ")] for line in data]
    return data


def check_if_possible(result, numbers, num_now):
    if len(numbers) == 0:
        if result == num_now:
            return 1
        else:
            return 0
    return max(
        check_if_possible(result, numbers[1:], num_now + numbers[0]),
        check_if_possible(result, numbers[1:], num_now * numbers[0]),
        check_if_possible(result, numbers[1:], num_now*(10**len(str(numbers[0]))) + numbers[0]),
    )

def check_equations(data):
    sum = 0
    for line in data:
        result, numbers = line
        result = int(result[0])
        numbers = list(map(int, numbers))
        if check_if_possible(result, numbers[1:], numbers[0]):
            sum += result
    return sum


def main():
    get_input.get_input(7)
    file = open("input_day_7", "r")
    lines = file.readlines()
    data = parse(lines)
    return check_equations(data)



if __name__ == "__main__":
    print(main())