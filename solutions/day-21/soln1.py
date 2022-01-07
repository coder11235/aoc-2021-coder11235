inp = open('data.txt').read().splitlines()
p1 = int(inp[0].split(': ')[1])
p2 = int(inp[1].split(': ')[1])

scp1 = 0
scp2 = 0

die = 1
rl = 0

def getdieval():
    global die, rl
    if die > 100:
        die = die - 100
    val = die
    die += 1
    return val

while scp1 < 21 and scp2 < 21:
    p1sum = sum([getdieval() for _ in range(3)])
    p1 += p1sum
    if p1 > 10:
        p1 = p1%10
    if p1 == 0:
        p1 = 10
    scp1 += p1
    if scp1 >= 1000:
        print(scp2 * rl)
        break
    
    p2sum = sum([getdieval() for _ in range(3)])
    p2 += p2sum
    if p2 > 10:
        p2 = p2%10
    if p2 == 0:
        p2 = 10
    scp2 += p2

print(scp1 * rl)