inp = open('sample.txt').read().splitlines()
p1 = int(inp[0].split(': ')[1])
p2 = int(inp[1].split(': ')[1])

scp1 = 0
scp2 = 0

c1 = 0
c2 = 0

def play2(p1,p2, scp1, scp2, mv):
    global c1, c2
    p2 += mv
    if p2 > 10:
        p2 = p2%10
    if p2 == 0:
        p2 = 10
    scp2 += p2

    if scp2 >= 21:
        c2 += 1
        print(c1,c2)
        return

    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                play1(p1, p2, scp1, scp2, i+j+k)

def play1(p1,p2, scp1, scp2, mv):
    global c1, c2
    p1 += mv
    if p1 > 10:
        p1 = p1%10
    if p1 == 0:
        p1 = 10
    scp1 += p1

    if scp1 >= 21:
        c1 += 1
        print(c1,c2)
        return

    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                play2(p1, p2, scp1, scp2, i+j+k)

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            play1(p1, p2, scp1, scp2, i+j+k)

print(c1,c2)