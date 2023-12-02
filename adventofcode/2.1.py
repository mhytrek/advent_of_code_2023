import get_input

def possible_games(lines, our_bag):
    result = 0
    for i in range(len(lines)):

        data = lines[i].split(" ")
        index = data[1][:-1]
        result += int(index)

        data = data[2:]

        dic = {"red":0, "blue":0, "green":0}
        for j in range(0,len(data),2):
            if data[j+1][-1] in [";", ",", "\n"]:
                color = data[j+1][:-1]
            else:
                color = data[j+1]
            dic[color] = max(dic[color], int(data[j]))


        for c in dic.keys():
            if dic[c] > our_bag[c]:
                result -= int(index)
                break


    return result

if __name__ == '__main__':
    lines = get_input.download_input(2)
    d = {"red":12, "blue":14, "green":13}
    print(possible_games(lines,d))