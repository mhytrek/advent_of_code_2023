from Input_helper import get_input


def parse(data):
    return list(map(int, list(data[0].replace("\n", ""))))

def file_compacting(data):
    compacted = []
    start = 0
    end = len(data)-1
    if end % 2 == 1:
        end -= 1
    rest = data[end]
    while start <= end + 1:
        if start % 2 == 0:
            if start == end:
                compacted = compacted + [start // 2 for _ in range(rest)]
            else:
                compacted = compacted + [start//2 for _ in range(data[start])]
        else:
            if start >= end:
                break
            free_space = data[start]
            while free_space != 0:
                id = end // 2
                if rest == 0:
                    end -= 2
                    rest = data[end]
                elif rest >= free_space:
                    compacted = compacted + [id for _ in range(free_space)]
                    rest -= free_space
                    free_space = 0
                else:
                    compacted = compacted + [id for _ in range(rest)]
                    free_space -= rest
                    data[end] = 0
                    end -= 2
                    rest = data[end]
        start += 1

    sum = 0
    for i in range(len(compacted)):
        sum += i * compacted[i]
    return sum




def main():
    get_input(9)
    file = open("input_day_9", "r")
    lines = file.readlines()
    data = parse(lines)
    data = file_compacting(data)
    print(data)



if __name__ == "__main__":
    print(main())