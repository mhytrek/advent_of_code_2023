from webbrowser import Error

from Input_helper import get_input
import re

def parse(d):
    replace_sym = {"#": "##", "O": "[]", ".": "..", "@": "@.",}
    data = "".join(d)
    for key in replace_sym.keys():
        data = data.replace(key, replace_sym[key])
    board, moves = data.split("\n\n")
    board = [list(b) for b in board.split("\n")]
    moves = list(moves.replace("\n", ""))
    return board, moves

class Board:
    def __init__(self, board):
        self.board = board
        self.robot = self.find_robot()
        self.moves = {"^": (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)}


    def find_robot(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == '@':
                    return i, j
        return None

    def move_box(self, x1, y1, m, before):
        x_move, y_move = m
        t = {"[": 1, "]": -1}
        if self.board[x1][y1] == ".":
            self.board[x1][y1] = before
            return
        elif t.get(self.board[x1][y1]) is not None:
            sibling = t.get(self.board[x1][y1])
            if x_move == 0:
                self.move_box(x1, y1 + y_move, m, self.board[x1][y1])
                self.board[x1][y1] = before
            else:
                self.move_box(x1 + x_move, y1 + sibling, m, self.board[x1][y1 + sibling])
                self.move_box(x1 + x_move, y1, m, self.board[x1][y1])
                self.board[x1][y1] = before
                self.board[x1][y1+sibling] = "."
            return
        elif self.board[x1][y1] == "#":
            raise Error
        else:
            raise Error


    def move_box_sym(self, x1, y1, m):
        x_move, y_move = m
        t = {"[": 1, "]": -1}
        if self.board[x1][y1] == ".":
            return True
        elif t.get(self.board[x1][y1]) is not None:
            sibling = t.get(self.board[x1][y1])
            if x_move == 0:
                return self.move_box_sym(x1, y1 + y_move, m)
            else:
                return self.move_box_sym(x1+ x_move, y1, m) and self.move_box_sym(x1 + x_move, y1 + sibling , m)
        elif self.board[x1][y1] == "#":
            return False
        else:
            raise Error(f"We find {self.board[x1][y1]}")


    def move_robot(self, m):
        x1, y1 = self.robot
        x_add, y_add = self.moves[m]
        x_new, y_new = x1 + x_add, y1 + y_add
        could_move = self.move_box_sym(x_new, y_new, (x_add, y_add))
        if could_move:
            self.move_box(x_new, y_new, (x_add, y_add), "@")
            self.board[x1][y1] = "."
            self.robot = (x_new, y_new)


    def count_gps(self):
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == "[":
                    count += (100 * i) + j
                    print(i,j, (100 * i) + j)
        return count


def symulation(board, moves):
    sym_board = Board(board)
    for move in moves:
        sym_board.move_robot(move)
    return sym_board.count_gps()



def main():
    get_input(15)
    file = open("input_day_15", "r")
    lines = file.readlines()
    board, moves = parse(lines)
    return symulation(board, moves)



if __name__ == "__main__":
    print(main())
