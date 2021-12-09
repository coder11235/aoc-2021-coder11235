import math
from termcolor import colored

heightmap = open('sample.txt', 'r').read().split('\n')

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

def dfs(i, j, risk):
    risk.append((i, j))
    cur = heightmap[i][j]
    adj = getadj(i, j)
    adj = list(
        filter(
            lambda i : heightmap[i[0]][i[1]] - cur == 1 and heightmap[i[0]][i[1]] != 9
        , adj)
    )
    if len(adj) == 0:
        return
    for i, j in adj:
        dfs(i, j, risk)

risk = []

for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        if issmallest(i, j):
            risk.append((i, j))

sizes: list = []

inthere = []

for i, j in risk:
    curriskarray = []
    dfs(i, j, curriskarray)
    inthere.append(curriskarray)
    curriskarray = set(curriskarray)
    sizes.append(len(curriskarray))

sizes.sort()

for p in range(len(sizes)):
    for i in range(len(heightmap)):
        for j in range((len(heightmap[0]))):
            if (i, j) in risk:
                print(colored(heightmap[i][j], 'red'), end='')
            elif (i, j) in inthere[p]:
                print(colored(heightmap[i][j], 'blue'), end='')
            else:
                print(heightmap[i][j], end='')
        print()
    print()

print(sizes)
sizes = sizes[-3:]
print(sizes)

print(math.prod(sizes))