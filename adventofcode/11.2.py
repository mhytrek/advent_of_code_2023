import get_input

def shortest_path(vector1, vector2, exr, exc):
    sum = 0
    x = abs(vector1[0]-vector2[0])
    y = abs(vector1[1]-vector2[1])
    ax = min(vector1[0], vector2[0])
    bx = max(vector1[0], vector2[0])
    ay = min(vector1[1], vector2[1])
    by = max(vector1[1], vector2[1])
    for row in exr:
        if ax < row < bx:
            sum -= 1
            sum += 1000000
    for col in exc:
        if ay < col < by:
            sum -= 1
            sum += 1000000
    return x+y+sum

def expanded(space):
    rows = []
    cols = []
    for row in range(len(space)):
        if len(set(space[row])) == 1:
            rows.append(row)
    for col in range(len(space[0])):
        flag = True
        for i in range(len(space)):
            if space[i][col] != ".":
                flag = False
        if flag:
            cols.append(col)
    return rows,cols


def change_input(lines):
    galaxies={}
    space=[[lines[i][j] for j in range(len(lines[0])-1) ]for i in range(len(lines))]
    expandexrows, expandedcols = expanded(space)
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
            sum += shortest_path(galaxies[galaxy1], galaxies[galaxy2], expandexrows, expandedcols)
    return sum

# lines=get_input.download_input(11)
file = open("example_11.txt")
lines = file.readlines()
print(change_input(lines))



