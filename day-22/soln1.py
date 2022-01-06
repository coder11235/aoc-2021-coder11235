inp = open('data.txt', 'r').read().splitlines()

oncubes = [[[False for _ in range(101)] for _ in range(101)] for _ in range(101)]

for i in inp:
    state, dims = i.split(' ')
    state = True if state == 'on' else False
    coords = []
    for i in dims.split(','):
        _, i = i.split('=')
        coords.append(tuple(int(j) for j in i.split('..')))
    x,y,z = coords
    if state:
        for i in range(x[0], x[1]+1):
            if -50 <= i <= 50:
                for j in range(y[0], y[1]+1):
                    if -50 <= j <= 50:
                        for k in range(z[0], z[1]+1):
                            if -50 <= k <= 50:
                                oncubes[i][j][k] = True
    else:
        for i in range(x[0], x[1]+1):
            if -50 <= i <= 50:
                for j in range(y[0], y[1]+1):
                    if -50 <= j <= 50:
                        for k in range(z[0], z[1]+1):
                            if -50 <= k <= 50:
                                oncubes[i][j][k] = False

cnt = 0
for i in oncubes:
    for j in i:
        for k in j:
            if k:
                cnt += 1

print(cnt)