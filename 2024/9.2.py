from Input_helper import get_input


def parse(data):
    return list(map(int, list(data[0].replace("\n", ""))))

def file_compacting(data):
    compacted = []
    used = set()
    start = 0
    end = len(data)-1
    if end % 2 == 1:
        end -= 1
    while start <= end:
        if start % 2 == 0 and start not in used:
                compacted = compacted + [start//2 for _ in range(data[start])]
        else:
            freespace = data[start]
            start_2 = end
            while start_2 > start and freespace != 0:
                if start_2 not in used and data[start_2] <= freespace:
                    compacted = compacted + [start_2//2 for _ in range(data[start_2])]
                    freespace -= data[start_2]
                    used.add(start_2)
                else:
                    start_2 -= 2
            compacted = compacted + [0 for _ in range(freespace)]
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
    print("00992111777.44.333....5555.6666.....8888..")



if __name__ == "__main__":
    print(main())