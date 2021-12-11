# PLS DO NOT LOOK AT THIS IM JUST HAPPY IT WORKS

data = open('data.txt').read().split('\n')

# from termcolor import colored

def parse(data):
    arr = []
    for i in data:
        a = []
        for j in list(i):
            a.append(int(j))
        arr.append(a)
    return arr

def getadj(i, j):
    #array storing adjacent points
    adj = []
    if i < len(data) - 1:
        adj.append((i+1, j))
    if i > 0:
        adj.append((i-1, j))
    if j < len(data[0]) - 1:
        adj.append((i, j+1))
        if i < len(data) - 1:
            adj.append((i+1, j+1))
        if i > 0:
            adj.append((i-1, j+1))
    if j > 0:
        adj.append((i, j-1))
        if i < len(data) - 1:
            adj.append((i+1, j-1))
        if i > 0:
            adj.append((i-1, j-1))
    return adj

count = [0]
data = parse(data)

def dfs(vis, i, j, ct):
    vis[i][j] = True
    data[i][j] = 0
    count[0] += 1
    adj = getadj(i, j)
    adj = list(filter(
        lambda p: not vis[p[0]][p[1]]
    , adj))
    for (x, y) in adj:
        data[x][y] += 1
    for (x, y) in adj:
        if data[x][y] > 9:
            dfs(vis, x, y, ct)

print(getadj(5,5))

hasnotfinished = True
cnt = 0

while hasnotfinished:
    vis = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
    for i in range(len(data)):
        for j, el in enumerate(data[i]):
            data[i][j] += 1
            if el == 9:
                dfs(vis, i, j, count)
    finished = True
    for i in range(len(data)):
        for j in range(len(data[0])):
            if vis[i][j]:
                data[i][j] = 0
            else:
                finished = False
    cnt += 1
    hasnotfinished = not finished
    
print(cnt)