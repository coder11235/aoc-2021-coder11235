from collections import deque

data = open('data.txt', 'r').read().split('\n')

score = 0
SCORE_MAP = {
	")":3,
	"]":57,
	"}":1197,
	">":25137
}

for line in data:
    latest = deque()
    arr = list(line)
    for ch in arr:
        if ch == "(" or ch == "{" or ch == "[" or ch == "<":
            latest.append(ch)
        else:
            lt = latest.pop()
            if not (lt == "(" and ch == ")" or lt == "{" and ch == "}" or lt == "<" and ch == ">" or lt == "[" and ch == "]"):
                score += SCORE_MAP[ch] 
                break

print(score)
