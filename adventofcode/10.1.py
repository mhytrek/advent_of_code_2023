import get_input

directions = {'J': [(-1,0),(0,-1)], 'F':[(1,0),(0,1)], 'L':[(-1,0),(0,1)],
                  '7':[(1,0),(0,-1)], '|':[(1,0),(-1,0)], '-':[(0,1),(0,-1)], '.':[(0,0)]}

def distance(pointer, dist, table, visited):
    global directions
    for x,y in directions[table[pointer[0]][pointer[1]]]:
        x += pointer[0]
        y += pointer[1]
        if not visited[x][y]:
            dist[x][y] = dist[pointer[0]][pointer[1]]+1
            pointer = [x,y]
            return pointer, dist
    return pointer, dist

def find_loop(pointer,table, dist):
    pointers = []
    dir = [(1,0), (-1,0), (0,-1), (0,1)]
    global directions
    for i,j in dir:
        ai = pointer[0] + i
        aj = pointer[1] + j
        for x,y in directions[table[ai][aj]]:
            x += ai
            y += aj
            if x == pointer[0] and y == pointer[1]:
                dist[ai][aj] = 1
                pointers.append([ai,aj])
                break
    return pointers, dist


def read_input(lines):
    global directions
    table = [['.' if i == 0 or i == len(lines)+1 or j == 0 or j == len(lines[0]) else lines[i-1][j-1] for j in range(len(lines[0])+1)] for i in range(len(lines)+2)]
    dist = [[0 for _ in range(len(table[0]))] for _ in range(len(table))]
    visited = [[False for _ in range(len(table[0]))] for _ in range(len(table))]
    # print(*table, sep= "\n")
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 'S':
                zero = [i,j]
    pointers,dist = find_loop(zero,table, dist)
    print(pointers)
    p1,p2 = pointers
    visited[p1[0]][p1[1]] = True
    visited[p2[0]][p2[1]] = True
    visited[zero[0]][zero[1]] = True
    while p1 != p2:
        p1, dist = distance(p1,dist,table, visited)
        p2, dist = distance(p2,dist,table, visited)
        visited[p1[0]][p1[1]] = True
        visited[p2[0]][p2[1]] = True
    print(*dist, sep="\n")
    maxx = 0
    for i in range(len(dist)):
        maxx = max(max(dist[i]), maxx)
    return maxx

# lines = get_input.download_input(10)
file = open("input_day_10")
lines = file.readlines()
print(read_input(lines))