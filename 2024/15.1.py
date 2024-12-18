from Input_helper import get_input
import re

def parse(d):
    data = "".join(d)
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
                    self.board[i][j] = "."
                    return i, j
        return None


    def move(self, m):
        x_add, y_add = self.moves[m]
        x, y = self.robot
        robot_xnew = x + x_add
        robot_ynew = y + y_add
        elem = self.board[robot_xnew][robot_ynew]
        if elem == "#":
            return
        elif elem == "O":
            box_xnew, box_ynew = robot_xnew, robot_ynew

            while elem == "O":
                box_xnew, box_ynew = box_xnew + x_add, box_ynew + y_add
                elem = self.board[box_xnew][box_ynew]

            if elem == "#":
                return
            elif elem == ".":
                self.board[box_xnew][box_ynew] = "O"
                self.board[robot_xnew][robot_ynew] = "."
        self.robot = (robot_xnew, robot_ynew)

    def count_gps(self):
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == "O":
                    count += (100 * i) + j
        return count


def symulation(board, moves):
    sym_board = Board(board)
    for move in moves:
        sym_board.move(move)
    return sym_board.count_gps()



def main():
    get_input(15)
    file = open("input_day_15", "r")
    lines = file.readlines()
    board, moves = parse(lines)
    return symulation(board, moves)



if __name__ == "__main__":
    print(main())
