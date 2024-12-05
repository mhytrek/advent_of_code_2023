from adventofcode import get_input

def parse_data(lines):
    return [line.replace('\n', '') for line in lines]

def count_words(data):
    def in_table(x, y):
        if 0 <= x < x_len and 0<= y < y_len:
            return True
        return False


    def check_if_word_starts(x, y, step):
        for i in range(1, len(word)):
            x = x + step[0]
            y = y + step[1]
            if (not in_table(x,y)) or data[x][y] != word[i]:
                return False
        return True

    steps = [
        (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)
    ]
    word = "XMAS"
    x_len = len(data)
    y_len = len(data[0])
    sum = 0

    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == word[0]:
                for step in steps:
                    sum += check_if_word_starts(x, y, step)
    return sum


def main():
    # get_input.get_input(4)
    file = open("input_day_4", "r")

    lines = file.readlines()
    data = parse_data(lines)
    return count_words(data)


if __name__ == "__main__":
    print(main())