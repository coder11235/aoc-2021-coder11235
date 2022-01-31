inp = open('data.txt').read()

parse = lambda inp : [list(el) for el in inp.splitlines()]

def dpr(arr):
    for i in arr:
        for j in i:
            print(j, end="")
        print()
    print()

def move_east(data: list[list[str]]):
    in_motion = False
    for ini, i in enumerate(data):
        tmp = False
        pf = False
        for inj, j in enumerate(i):
            if tmp:
                tmp = False
                continue
            if j == '>':
                nxt = 0 if inj == (len(data[0])-1) else inj + 1
                if data[ini][nxt] == '.':
                    if inj == (len(data[0])-1) and pf:
                        continue
                    data[ini][inj] = '.'
                    data[ini][nxt] = '>'
                    tmp = True
                    in_motion = True
                    if inj == 0:
                        pf = True
    return in_motion

def move_south(data: list[list[str]]):
    moved = set()
    in_motion = False
    for ini, i in enumerate(data):
        for inj, j in enumerate(i):
            if j == 'v' and not (ini, inj) in moved:
                nxt = 0
                if ini != (len(data)-1):
                    nxt = ini + 1
                if data[nxt][inj] == '.':
                    data[nxt][inj] = 'v'
                    data[ini][inj] = '.'
                    moved.add((nxt, inj))
                    in_motion = True
                    if ini == 0:
                        if data[len(data)-1][inj] != '.':
                            moved.add((len(data)-1, inj))
    return in_motion

count = 0

def move(data: list[list[str]]):
    global count
    a = move_east(data)
    b = move_south(data)
    if a or b:
        count += 1
    else:
        print(count+1)
        # dpr(arr)
        exit()

arr = parse(inp)
while True:
    move(arr)