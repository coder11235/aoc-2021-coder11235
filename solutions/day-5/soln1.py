file = open('data.txt', 'r')
data = file.read().split('\n')

points = {}

def ins_point(x, y):
    global points
    if (x,y) in points:
        points[(x,y)] += 1
    else:
        points[(x,y)] = 1

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
                ins_point(rx, i)
        else:
            for i in range(ry, ly + 1):
                ins_point(rx, i)
    elif ly == ry:
        if lx <= rx:
            for i in range(lx, rx + 1):
                ins_point(i, ry)
        else:
            for i in range(rx, lx + 1):
                ins_point(i, ry)

count = 0

for val in points.values():
    if val >= 2:
        count += 1

print(count)