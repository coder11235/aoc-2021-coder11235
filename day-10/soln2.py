data = open('data.txt', 'r').read().split('\n')

sc = []

def getscore(ch):
    if ch == "(":
        return 1
    elif ch == "[":
        return 2
    elif ch == "{":
        return 3
    else:
        return 4

def calcinc(arr):
    lc = 0
    for i in arr:
        lc *= 5
        lc += getscore(i)
    sc.append(lc)

for line in data:
    latest = []
    arr = list(line)
    iscor = False
    for ch in arr:
        if ch == "(" or ch == "{" or ch == "[" or ch == "<":
            latest.append(ch)
        else:
            lt = latest[-1]
            if lt == "(" and ch == ")" or lt == "{" and ch == "}" or lt == "<" and ch == ">" or lt == "[" and ch == "]":
                latest.pop(-1)
            else:
                iscor = True
                break
    if iscor:
        continue
    latest.reverse()
    calcinc(latest)

sc.sort()

median = sc[int((len(sc))/2)]

print(median)