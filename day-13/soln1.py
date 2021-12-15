data = open('data.txt', 'r').read()

from termcolor import colored

coords = []
instruc = []

def parse(coords, instruc):
    c, i = data.split('\n\n')
    coords = [tuple([int(k) for k in j.split(',')]) for j in c.splitlines()]
    for j in i.splitlines():
        mn = j.split(' ')[2]
        instruc.append(tuple(mn.split('=')))
    return coords, instruc

coords, instruc = parse(coords, instruc)

mx = 0
my = 0
for i in coords:
    if i[0] > mx:
        mx = i[0]
    if i[1] > my:
        my = i[1]

sheet = [[False for _ in range(mx+1)] for _ in range(my+1)]

def printsheet(sheet):
    for i in sheet:
        for j in i:
            print(colored('# ', 'blue') if j else '# ', end="")
        print()
    print()

def foldvert(sheet, ax):
    top = sheet[:ax]
    bottom = list(reversed(sheet[ax+1:]))
    return [[(top[i][j] or bottom[i][j]) if (i < len(bottom)) else True for j in range(len(top[0]))] for i in range(len(top))]

def foldhor(sheet, ax):
    left = [row[:ax] for row in sheet]
    right = [row[ax+1:] for row in sheet]
    left = [row[::-1] for row in left]
    return [row[::-1] for row in [[(left[i][j] or right[i][j]) if (i < len(right)) else True for j in range(len(right[0]))] for i in range(len(left))]]


for i in coords:
    sheet[i[1]][i[0]] = True

ins = instruc[0]
if ins[0] == 'y':
    sheet = foldvert(sheet, int(ins[1]))
else:
    sheet = foldhor(sheet, int(ins[1]))

print(ins)

count = sum([sum(row) for row in sheet])

print(count)