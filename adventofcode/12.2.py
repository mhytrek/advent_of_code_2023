def change_lines(lines):
    results = []
    springs = []
    for line in lines:
        splited = line[:-1].split(" ")
        results.append(splited[1].split(",")*5)
        n = len(splited[0]) + 1
        springs.append([splited[0][i % n] if i % n < n-1 else "?" for i in range(n*5-1)])
    return results, springs


def is_symbol(table,i,j,symbol):
    for k in range(i,j):
        if table[k] == symbol:
            return False
    return True

def main(lines):
    results, springs = change_lines(lines)
    sum = 0
    for line in range(len(springs)):
        result = results[line]
        result = [int(result[i]) for i in range(len(result))]
        spring = springs[line]
        DP = [[0 for _ in range(len(spring))] for _ in range(len(result)+1)]
        DP[0][0] = 1
        for i in range(0,len(DP)):
            for j in range(1,len(DP[0])):
                if i == len(DP)-1:
                    add = 1
                else:
                    add = -1
                if j-1 >= 0 and (spring[j-1] != "#" or (i == len(DP)-1 and spring[j] != "#")):
                    DP[i][j] += DP[i][j-1]
                if i-1 >= 0 and j-result[i-1] + add >= 0 and is_symbol(spring,j-result[i-1]+add,j + add,"."):
                    if not (i != len(DP)-1 and spring[j-1] == "#"):
                        if not (i == len(DP)-1 and  not is_symbol(spring,j+1,len(DP[0]),"#")):
                            DP[i][j] += DP[i-1][j-result[i-1]+add]

        sum += DP[-1][-1]
        # print(*DP,sep="\n")
        # print("\n")
    return sum


file = open("example_12.txt")
lines = file.readlines()
print(main(lines))