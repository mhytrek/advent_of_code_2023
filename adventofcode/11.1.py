import get_input

def shortest_path(vector1, vector2):
    x = abs(vector1[0]-vector2[0])
    y = abs(vector1[1]-vector2[1])
    return x+y

def expanded(space):
    new_rows_space = []
    for row in range(len(space)):
        if len(set(space[row])) == 1:
            new_rows_space.append([space[row][j] for j in range(len(space[row]))])
        new_rows_space.append([space[row][j] for j in range(len(space[row]))])
    new_all_space = [[] for _ in range(len(new_rows_space))]
    for col in range(len(new_rows_space[0])):
        flag = True
        for i in range(len(new_rows_space)):
            new_all_space[i].append(new_rows_space[i][col])
            if new_rows_space[i][col] != ".":
                flag = False
        if flag:
            print(col)
            for j in range(len(new_rows_space)):
                new_all_space[j].append(new_rows_space[j][col])
    return new_all_space


def change_input(lines):
    galaxies={}
    space=[[lines[i][j] for j in range(len(lines[0])-1) ]for i in range(len(lines))]
    space = expanded(space)
    print(*space, sep="\n")
    index = 0
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] == '#':
                index += 1
                space[i][j] = index
                galaxies[index]=(i,j)
    sum = 0
    for galaxy1 in range(1,index):
        for galaxy2 in range(galaxy1+1,index+1):
            sum += shortest_path(galaxies[galaxy1], galaxies[galaxy2])
    return sum

# lines=get_input.download_input(11)
file = open("example_11.txt")
lines = file.readlines()
print(change_input(lines))



