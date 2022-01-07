import math
from termcolor import colored

heightmap = open('data.txt', 'r').read().split('\n')

def parse(line):
    nl = []
    for i in list(line):
        nl.append(int(i))
    return nl

def getadj(i, j):
    #array storing adjacent points
    adj = []
    if i < len(heightmap) - 1:
        adj.append((i+1, j))
    if i > 0:
        adj.append((i-1, j))
    if j < len(heightmap[0]) - 1:
        adj.append((i, j+1))
    if j > 0:
        adj.append((i, j-1))
    return adj

heightmap = list(map(parse, heightmap))

def issmallest(i, j):
    #current height pos
    ch = heightmap[i][j]
    adj = getadj(i, j)

    for i, j in adj:
        if heightmap[i][j] <= ch:
            return False
    return True

def dfs(i, j, vis: list):
    vis[i][j] = True
    cur = heightmap[i][j]
    adj = getadj(i, j)
    adj = list(
        filter(
            lambda k : heightmap[k[0]][k[1]] != 9 and not vis[k[0]][k[1]]
        , adj)
    )
    if len(adj) == 0:
        return
    for i, j in adj:
        dfs(i, j, vis)

risk = []

for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        if issmallest(i, j):
            risk.append((i, j))

sizes: list = []

for i, j in risk:
    vis = [[False for _ in range(len(heightmap[0]))] for _ in range(len(heightmap))]
    dfs(i, j, vis)
    size = 0
    for a in vis:
        size += sum(a)
    sizes.append(size)

sizes.sort()

print(sizes)
sizes = sizes[-3:]

print(math.prod(sizes))