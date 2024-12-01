from adventofcode import get_input

def get_data(lines):
    data = [list(map(int, a.replace("\n", "").split("   "))) for a in lines]
    data1 = [d[0] for d in data]
    data2 = [d[1] for d in data]
    return data1, data2

def get_distance(data1, data2):
    dis = 0
    data1.sort()
    data2.sort()
    for i in range(len(data1)):
        dis += abs(data1[i] - data2[i])
    return dis

def get_similarity(data1, data2):
    similarity = 0
    for a in data1:
        similarity += a * data2.count(a)
    return similarity

def main():
    file = open("input_day_1", "r")
    lines = file.readlines()
    data1, data2 = get_data(lines)
    print(get_distance(data1, data2))
    print(get_similarity(data1, data2))

if __name__ == "__main__":
    print(get_input.get_input(1))
    print(get_input.get_example(1))

