data = open('data.txt', 'r').read().split('\n')

score = 0

def getscore(ch):
    if ch == ")":
        return 3
    elif ch == "]":
        return 57
    elif ch == "}":
        return 1197
    else:
        return 25137

for line in data:
    latest = []
    arr = list(line)
    for ch in arr:
        if ch == "(" or ch == "{" or ch == "[" or ch == "<":
            latest.append(ch)
        else:
            lt = latest[-1]
            if lt == "(" and ch == ")" or lt == "{" and ch == "}" or lt == "<" and ch == ">" or lt == "[" and ch == "]":
                latest.pop(-1)
            else:
                score += getscore(ch)
                break

print(score)