import matplotlib.pyplot as pl

data = open('sample.txt').read()

def parse(data: str):
    data = data.split(': ')[1]
    coords = data.split(', ')
    target = []
    for i in coords:
        i = i.split('=')[1]
        target.append(tuple([int(i) for i in i.split('..')]))
    return target

target = parse(data)
print(target)
x = 0
y = 0

xv = 6
yv = 9

arr = [[0,0]]
while not (target[0][0] <= x <= target[0][1] and target[1][0] <= y <= target[1][1]):
    x += xv
    y += yv
    if xv > 0:
        xv -= 1
    elif xv < 0:
        xv += 1
    yv -= 1
    print(x, y)
    arr.append([x, y])

print(arr)

xp = []
yp = []
for i in arr:
    xp.append(i[0])
    yp.append(i[1])

pl.plot(xp, yp)

pl.plot(
    target[0] + tuple(reversed(target[0]))
    ,target[1]  + target[1]
    )
pl.show()