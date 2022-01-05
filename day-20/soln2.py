inp = open('data.txt', 'r').read()

def parse(inp: str):
    alg, img = inp.split('\n\n')
    alg = [True if i == '#' else False for i in alg]
    imgarr = [[True if i == '#' else False for i in ln] for ln in img.splitlines()]
    return alg, imgarr

def debug_prnt_img(inpimg):
    for i in inpimg:
        for j in i:
            print('# ' if j else '. ', end='')
        print()

def append_on_all_sides(inpimp):
    for ri in range(len(inpimg)):
        inpimg[ri].insert(0, False)
        inpimg[ri].append(False)
    inpimg.insert(0, [False]*len(inpimg[0]))
    inpimg.append([False]*len(inpimg[0]))

def get_index(coord, inpimg):
    adj = ""
    for a in [-1,0,1]:
        for b in [-1,0,1]:
            adj += '1' if inpimg[coord[0]+a][coord[1]+b] else '0'
    return int(adj, 2)

alg, inpimg = parse(inp)

for i in range(100):
    append_on_all_sides(inpimg)

for _ in range(50):
    newimg = []
    for i in range(1, len(inpimg)-1):
        newrow = []
        for j in range(1, len(inpimg[0])-1):
            algin = get_index((i, j), inpimg)
            newrow.append(alg[algin])
        newimg.append(newrow)
    inpimg = newimg

print(sum([sum(row) for row in inpimg]))