
def change_lines(lines):
    sum = 0
    dish = [[lines[i][j] for j in range(len(lines[0])-1)] for i in range(len(lines))]

    def push(x, y):
        nonlocal sum
        while x-1 >= 0 and dish[x-1][y] == ".":
            dish[x][y]="."
            x-=1
            dish[x][y] = "O"
        sum += len(dish)-x
        return

    for i in range(len(dish)):
        for j in range(len(dish[0])):
            if dish[i][j] == "O":
                push(i,j)
    return sum

file = open("example_14.txt")
lines = file.readlines()
print(change_lines(lines))