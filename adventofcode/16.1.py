from enum import Enum
import sys

sys.setrecursionlimit(10000)

class Tile:
    def __init__(self, x, y, sym):
        self.sym = sym
        self.y = y
        self.x = x
        self.energized = 0
        self.last_dir = None

    def becomenergized(self):
        self.energized = 1


class Direction(Enum):
    DW = 0
    L = 1
    UW = 2
    R = 3


    def is_horizontally(self):
        return self == Direction.L or self == Direction.R

    def is_vertically(self):
        return self == Direction.DW or self == Direction.UW

    def left(self):
        return Direction((self.value - 1) % 4)

    def right(self):
        return Direction((self.value + 1) % 4)

    def to_unit_vector(self):
        if self == Direction.DW:
            return 1, 0
        elif self == Direction.UW:
            return -1, 0
        elif self == Direction.R:
            return 0, 1
        else:
            return 0, -1

def where_next(tile, direction, table):

    def move_light(tile, new_direction, table):
        x, y = new_direction.to_unit_vector()
        nx = tile.x + x
        ny = tile.y + y
        if nx < 0 or ny < 0 or nx >= len(table) or ny >= len(table[0]):
            return
        new_tile = table[nx][ny]
        return where_next(new_tile, new_direction, table)


    tile.becomenergized()
    if tile.last_dir != None and tile.last_dir == direction:
        return
    tile.last_dir = direction
    if (tile.sym == "/" and direction.is_horizontally()) or (tile.sym == "\\" and direction.is_vertically()):
        new_direction = direction.left()
        move_light(tile, new_direction, table)

    elif (tile.sym == "/" and direction.is_vertically()) or (tile.sym == "\\" and direction.is_horizontally()):
        new_direction = direction.right()
        move_light(tile, new_direction, table)

    elif (tile.sym == "|" and direction.is_horizontally()) or (tile.sym == "-" and direction.is_vertically()):
        new_direction1 = direction.right()
        move_light(tile, new_direction1, table)

        new_direction2 = direction.left()
        move_light(tile, new_direction2, table)

    else:
        move_light(tile,direction,table)
    return

def create(lines):
    table = [[ Tile(i,j,lines[i][j]) for j in range(len(lines[0])-1)] for i in range(len(lines))]
    where_next(table[0][0], Direction.R, table)
    result = 0
    for i in range(len(table)):
        for j in range(len(table)):
            result += table[i][j].energized
    # new_table = [[table[i][j].last_dir.value + 1 if table[i][j].energized != 0 else 0  for j in range(len(table[0]))] for i in range(len(table))]
    # print(*new_table, sep="\n")
    return result


file = open("example_16.txt")
lines = file.readlines()
print(create(lines))


