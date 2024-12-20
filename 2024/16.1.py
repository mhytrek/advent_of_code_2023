from Input_helper import get_input
from queue import PriorityQueue

def parse(d):
    board = [list(b.replace("\n", "")) for b in d]
    return board

class Graph:
    def __init__(self):
        self.edges = {}

    def index(self, i,j):
        return i,j

    def get_edges(self, board):
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "#":
                    list = []
                    for step in steps:
                        i_new, j_new = i + step[0], j + step[1]
                        if 0 <= i_new < len(board) and 0 <= j_new < len(board[0]) and board[i_new][j_new] != '#':
                            list.append(self.index(i_new, j_new))
                    self.edges[self.index(i, j)] = list


    def find_char(self, char, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == char:
                    return self.index(i, j)
        return None


    @staticmethod
    def get_wage(u, v, last):
        dire = (v[0] - u[0], v[1] - u[1])
        if dire != last:
            return 1001
        return 1


    def dijkstra(self, start, stop, board):
        queue = PriorityQueue()
        queue.put((0, start, (0,1)))
        keys = list(self.edges.keys())
        distance = [float('inf')] * len(self.edges)
        visited = [False] * len(self.edges)
        parents = [None] * len(self.edges)
        distance[keys.index(start)] = 0

        while not queue.empty():
            dist, u, last = queue.get()
            for v in self.edges[u]:
                wage = self.get_wage(u, v, last)
                index_v = keys.index(v)
                if v not in visited and distance[index_v] > dist + wage:
                    distance[index_v] = dist + wage
                    parents[index_v] = u
                    queue.put((dist + wage, v, (v[0] - u[0], v[1] - u[1]) ))
            index_u = keys.index(u)
            visited[index_u] = True
        index_stop = keys.index(stop)

        parent = parents[index_stop]
        while parent is not None:
            x,y = parent
            board[x][y] = "@"
            parent = parents[keys.index(parent)]
        return distance[index_stop]



    def sym(self, board):
        self.get_edges(board)
        start = self.find_char('S', board)
        stop = self.find_char('E', board)
        w = self.dijkstra(start, stop, board)
        return w



def main():
    get_input(16)
    file = open("input_day_16", "r")
    lines = file.readlines()
    data = parse(lines)
    graph = Graph()
    return graph.sym(data)





if __name__ == "__main__":
    print(main())
