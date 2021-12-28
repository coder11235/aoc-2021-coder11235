# NO IT DOESNT WORK AAAAAAAAAAAAAAAAAA

data = open('sample.txt').read()

def parse(data: str):
    data = data.split(': ')[1]
    coords = data.split(', ')
    target = []
    for i in coords:
        i = i.split('=')[1]
        target.append(tuple([int(i) for i in i.split('..')]))
    return target

(minx, maxx), (miny, maxy) = parse(data)

def simulate(xv, yv):
    x = 0
    y = 0
    my = 0
    global minx, miny, maxx, maxy
    while True:
        # move
        x += xv
        y += yv
        if xv > 0:
            xv -= 1
        elif xv < 0:
            xv += 1
        yv -= 1
        if y > my:
            my = y

        # return if in box
        if minx <= x <= maxx and miny <= y <= maxy:
            return -1, my

        # return if not possible at all
        if y <= miny and yv <= 0:
            return 0, 0
        if x <= minx and xv <= 0:
            return 0, 0
        if x >= maxx and xv >= 0:
            return 1, 0

xv = 0
yv = 0

mmy = 0
while True:
    while True:
        res, my = simulate(xv, yv)
        if res == -1:
            if mmy > my: mmy = my
        elif res == 0: xv += 1
        else:
            break
    yv += 1
    res = simulate(minx, yv)
    if res == 1:
        break