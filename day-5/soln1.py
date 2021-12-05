file = open('data.txt', 'r')
data = file.read().split('\n')

points = []

for i in data:
    left, right = i.split('->')
    left = left.strip()
    right = right.strip()
    lx, ly = left.split(',')
    lx = int(lx)
    ly = int(ly)
    rx, ry = right.split(',')
    rx = int(rx)
    ry = int(ry)
    temppoints = []
    if lx == rx:
        if ly <= ry:
            for i in range(ly, ry + 1):
                temppoints.append([rx, i])
        elif ly >= ry:
            for i in range(ry, ly + 1):
                temppoints.append([rx, i])
        else:
            temppoints.append([rx, ry])
    elif ly == ry:
        if lx <= rx:
            for i in range(lx, rx + 1):
                temppoints.append([i, ry])
        elif lx >= rx:
            for i in range(rx, lx + 1):
                temppoints.append([i, ry])
        else:
            temppoints.append([rx, ry])
    points += temppoints

print(points)

firstencountered = []
count = 0
for i in points:
    if firstencountered.count(i) == 1:
        count += 1
        print(count)
    firstencountered.append(i)

print(count)