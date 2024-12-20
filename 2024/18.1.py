from Input_helper import get_input
from queue import PriorityQueue

def parse(d):
    failed = [tuple(map(int,b.replace("\n", "").split(",")[-1::-1])) for b in d]
    return failed

class Graph:
    def __init__(self):
        self.edges = {}

    def index(self, i,j):
        return i,j

    def get_edges(self, failed, length):
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(length):
            for j in range(length):
                if (i,j) not in failed :
                    list = []
                    for step in steps:
                        i_new, j_new = i + step[0], j + step[1]
                        if 0 <= i_new < length and 0 <= j_new < length and (i_new, j_new) not in failed:
                            list.append(self.index(i_new, j_new))
                    self.edges[self.index(i, j)] = list



    def dijkstra(self, start, stop, length, failed):
        board = [["." if (i,j) not in failed else "#"  for j in range(length)] for i in range(length)]
        queue = PriorityQueue()
        queue.put((0, start))
        keys = list(self.edges.keys())
        distance = [float('inf')] * len(self.edges)
        visited = [False] * len(self.edges)
        parents = [None] * len(self.edges)
        distance[keys.index(start)] = 0

        while not queue.empty():
            dist, u = queue.get()
            for v in self.edges[u]:
                index_v = keys.index(v)
                if v not in visited and distance[index_v] > dist + 1:
                    distance[index_v] = dist + 1
                    parents[index_v] = u
                    queue.put((dist + 1, v))
            index_u = keys.index(u)
            visited[index_u] = True
        index_stop = keys.index(stop)

        # parent = parents[index_stop]
        # while parent is not None:
        #     x, y = parent
        #     board[x][y] = "@"
        #     parent = parents[keys.index(parent)]
        return distance[index_stop]



    def sym(self, failed, x):
        self.get_edges(failed, x)
        start = (0,0)
        stop = (x-1,x-1)
        w = self.dijkstra(start, stop, x, failed)
        return w



def main():
    get_input(18)
    file = open("input_day_18", "r")
    lines = file.readlines()
    data = parse(lines)[:1024]
    graph = Graph()
    return graph.sym(data, 71)





if __name__ == "__main__":
    print(main())
