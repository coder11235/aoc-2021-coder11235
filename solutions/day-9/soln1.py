heightmap = open('data.txt', 'r').read().split('\n')

def parse(line):
    nl = []
    for i in list(line):
        nl.append(int(i))
    return nl

heightmap = list(map(parse, heightmap))

def issmallest(i, j):
    ch = heightmap[i][j]
    adj = []
    if i < len(heightmap) - 1:
        adj.append(heightmap[i+1][j])
    if i > 0:
        adj.append(heightmap[i-1][j])
    if j < len(heightmap[0]) - 1:
        adj.append(heightmap[i][j+1])
    if j > 0:
        adj.append(heightmap[i][j-1])

    for k in adj:
        if k <= ch:
            return False
    return True

risk = 0

for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        if issmallest(i, j):
            risk += 1 + heightmap[i][j]
