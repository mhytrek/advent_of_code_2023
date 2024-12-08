import Input_helper

def parse_data(lines):
    return [line.replace('\n', '') for line in lines]


def count_words(data):
    def in_table(x, y):
        if 0 <= x < x_len and 0<= y < y_len:
            return True
        return False


    def check_if_word_starts(x, y, step):
        sum = 0
        for i in range(2):
            flag = 1
            x_new = x + step[i][0]
            y_new = y + step[i][1]
            if (not in_table(x_new,y_new)) or data[x_new][y_new] != word[0]:
                flag = 0
            x_new = x + step[(i+1)%2][0]
            y_new = y + step[(i+1)%2][1]
            if (not in_table(x_new, y_new)) or data[x_new][y_new] != word[2]:
                flag = 0
            if flag:
                sum = 1
        return sum

    steps = [
        [(-1,-1),(1,1)],
        [(-1,1),(1,-1)],
    ]
    word = "MAS"
    x_len = len(data)
    y_len = len(data[0])
    sum = 0

    for x in range(1,len(data)-1):
        for y in range(1,len(data[x])-1):
            if data[x][y] == word[1]:
                if check_if_word_starts(x, y, steps[0]) and check_if_word_starts(x, y, steps[1]):
                    sum += 1
    return sum


def main():
    # get_input.get_input(4)
    file = open("input_day_4", "r")

    lines = file.readlines()
    data = parse_data(lines)
    return count_words(data)



if __name__ == "__main__":
    print(main())