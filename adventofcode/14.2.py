
def change_lines(lines):
    sum = 0
    dish = [[lines[i][j] for j in range(len(lines[0])-1)] for i in range(len(lines))]

    def push(x, y, direction):
        x1, y1 = direction
        while len(dish) > x+x1 >= 0 and len(dish[0]) > y+y1 >= 0 and dish[x+x1][y+y1] == ".":
            dish[x][y]="."
            x += x1
            y += y1
            dish[x][y] = "O"
        return

    def find_the_result(index,c):
        r = 1000000000 - index - 1
        cycle_len = c-index
        print(cycle_len)
        return cycles[index + (r%cycle_len)]


    cycles=[]

    for cycle in range(1000):
        for i in range(len(dish)):
            for j in range(len(dish[0])):
                if dish[i][j] == "O":
                    push(i,j,(-1,0))
        for i in range(len(dish)):
            for j in range(len(dish[0])):
                if dish[i][j] == "O":
                    push(i,j,(0,-1))
        for i in range(len(dish)-1,-1,-1):
            for j in range(len(dish[0])):
                if dish[i][j] == "O":
                    push(i,j,(1,0))
        for i in range(len(dish)):
            for j in range(len(dish[0])-1,-1,-1):
                if dish[i][j] == "O":
                    push(i,j,(0,1))
        sum = 0
        for i in range(len(dish)):
            for j in range(len(dish[0])):
                if dish[i][j] == "O":
                    sum += len(dish)-i
        #trying to find cycle
        if sum in cycles and cycles[cycles.index(sum)-1] == cycles[-1] and cycles[cycles.index(sum)-2] == cycles[-2]:
            return find_the_result(cycles.index(sum),cycle)
        cycles.append(sum)

    return sum

file = open("example_14.txt")
lines = file.readlines()
print(change_lines(lines))