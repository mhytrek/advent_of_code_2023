import get_input

def possible_games(lines):
    result = 0
    for i in range(len(lines)):
        #getting indexes of the games
        data = lines[i].split(" ")
        index = data[1][:-1]

        data = data[2:]

        #searching for the maximum amount of cubes of each color
        dic = {"red":0, "blue":0, "green":0}
        for j in range(0,len(data),2):
            if data[j+1][-1] in [";", ",", "\n"]:
                color = data[j+1][:-1]
            else:
                color = data[j+1]
            dic[color] = max(dic[color], int(data[j]))

        #counting the power of the set of cubes
        power_cubes = 1
        for c in dic.keys():
            power_cubes *= dic[c]

        result += power_cubes
    return result

if __name__ == '__main__':
    lines = get_input.download_input(2)
    print(possible_games(lines))