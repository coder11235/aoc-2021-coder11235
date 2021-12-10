from collections import deque
from typing import cast

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

def calcinc(stack: deque):
    lc = 0
    while(len(stack) != 0):
        lc = lc * 5 + getscore(stack.pop())
    sc.append(lc)

for line in data:
    latest = deque()
    arr = list(line)
    iscor = False
    for ch in arr:
        if ch == "(" or ch == "{" or ch == "[" or ch == "<":
            latest.append(ch)
        else:
            lt = latest.pop()
            if not (lt == "(" and ch == ")" or lt == "{" and ch == "}" or lt == "<" and ch == ">" or lt == "[" and ch == "]"):
                iscor = True
                break
    if iscor:
        continue
    calcinc(latest)

sc.sort()

median = sc[int((len(sc))/2)]

print(median)