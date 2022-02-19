class Heap:
    def __init__(self):
        self.values = []
    def picklowest(self):
        lowest_value = float("inf")
        lowest_set = None
        for index, val in enumerate(self.values):
            if val[1] < lowest_value:
                lowest_value = val[1]
                lowest_set = val
        return lowest_set
    def insert(self, value):
        self.values.append(value)
    def rm(self, i, j):
        for index, v in enumerate(self.values):
            if v[0] == (i, j):
                self.values.pop(index)
                break

input = [[int(char) for char in list(line)] for line in open('data.txt', 'r').read().splitlines()]


def addhor(mainarr: list[int]):
    newone = []
    for i in range(5):
        modded = [j + i for j in mainarr]
        newone += [j - 9 if j > 9 else j for j in modded]
    return newone

def addvert(mainarr: list[list]):
    newonw = []
    for r in range(5):
        for row in mainarr:
            modded = [j+r for j in row]
            newonw.append(addhor(modded))
    return newonw

input = addvert(input)

def getadjacent(i: int, j: int):
    ls = []
    ls.append((i+1, j))
    ls.append((i-1, j))
    ls.append((i, j+1))
    ls.append((i, j-1))
    ls = list(filter(
        lambda cur: cur[0] < len(input) and cur[0] >= 0 and cur[1] < len(input[0]) and cur[1] >= 0
        , ls)
    )
    return ls

def dijkstra(graph: list[list[int]], i: int, j: int):
    heap = Heap()
    vis = [[False for _ in input[0]] for _ in input]
    lowestarr = [[float("inf") for cell in row] for row in graph]
    lowestarr[i][j] = 0
    heap.insert(((i, j), 0))
    while len(heap.values) != 0:
        index, minvalue = heap.picklowest()
        ni, nj = index
        vis[ni][nj] = True
        for oi, oj in getadjacent(ni, nj):
            if vis[oi][oj]: continue
            nd = lowestarr[ni][nj] + graph[oi][oj]
            if nd < lowestarr[oi][oj]:
                lowestarr[oi][oj] = nd
                heap.insert(((oi, oj), nd))
        heap.rm(ni, nj)
    return lowestarr

ans = dijkstra(input, 0, 0)

print(ans[len(ans) - 1][len(ans[0]) - 1])
