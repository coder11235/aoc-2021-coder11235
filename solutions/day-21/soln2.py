inp = open("data.txt").read().splitlines()
p1 = int(inp[0].split(': ')[1])
p2 = int(inp[1].split(': ')[1])

win_score = 21

memo = {}

def split_and_play(p1,p2,scp1, scp2, fn):
    if (p1,p2,scp1, scp2, fn) in memo:
        return memo.get((p1,p2,scp1, scp2, fn))
    total_sub_uni_win_count = [0,0]
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                sub_uni_win_count = fn(p1,p2,scp1, scp2, i+j+k)
                for index in range(2):
                    total_sub_uni_win_count[index] += sub_uni_win_count[index]
    memo.update({(p1,p2,scp1, scp2, fn): total_sub_uni_win_count})
    return total_sub_uni_win_count

def play1(p1,p2,scp1, scp2, mv):
    global win_score
    p1 += mv
    if p1 > 10:
        p1 -= 10
    scp1 += p1
    if scp1 >= win_score:
        return [1,0]
    return split_and_play(p1,p2,scp1, scp2, play2)

def play2(p1,p2,scp1, scp2, mv):
    global win_score
    p2 += mv
    if p2 > 10:
        p2 -= 10
    scp2 += p2
    if scp2 >= win_score:
        return[0,1]
    return split_and_play(p1,p2,scp1, scp2, play1)

total_uni_win_count = split_and_play(p1,p2,0, 0, play1)

print(max(total_uni_win_count))