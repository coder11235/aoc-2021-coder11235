data = open('data.txt').read()

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
        # return if in box
        if minx <= x <= maxx and miny <= y <= maxy:
            return True

        # return if not possible at all
        if y <= miny and yv <= 0:
            return False
        if x <= minx and xv <= 0:
            return False
        if x >= maxx and xv >= 0:
            return False

ans = 0

for xv in range(maxx*2):
    for yv in range(-400, 400):
        success = simulate(xv, yv)
        if success:
            ans += 1

print(ans)