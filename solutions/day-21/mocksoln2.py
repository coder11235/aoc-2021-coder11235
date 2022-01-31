inp = """Player 1 starting position: 4
Player 2 starting position: 8""".splitlines()
p1 = int(inp[0].split(': ')[1])
p2 = int(inp[1].split(': ')[1])

scp1 = 0
scp2 = 0 

c1 = 0
c2 = 0

winscr = 2

def play1(p1,p2,scp1, scp2, mv):
    global c1, winscr
    p1 += mv
    if p1 > 10:
        p1 -= 10
    scp1 += p1
    print("p1", p1,p2,scp1,scp2,c1,c2)
    if scp1 >= winscr:
        c1 += 1
        return
    for i in range(3, 10):
        play2(p1,p2,scp1, scp2, i)

def play2(p1,p2,scp1, scp2, mv):
    global c2, winscr
    p2 += mv
    if p2 > 10:
        p2 -= 10
    scp2 += p2
    print("p2", p1,p2,scp1,scp2,c1,c2)
    if scp2 >= winscr:
        c2 += 1
        return
    for i in range(3, 10):
        play1(p1,p2,scp1, scp2, i)

for i in range(3,10):
    play1(p1,p2,scp1, scp2, i)

print(c1, c2)