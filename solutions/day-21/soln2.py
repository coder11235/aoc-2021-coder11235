inp = open("data.txt").read().splitlines()
position_p1 = int(inp[0].split(': ')[1])
position_p2 = int(inp[1].split(': ')[1])

win_score = 21

memo = {}

def split_and_play(position_p1,position_p2, score_p1, score_p2, fn_to_run):
    if (position_p1,position_p2,score_p1, score_p2, fn_to_run) in memo:
        return memo.get((position_p1,position_p2,score_p1, score_p2, fn_to_run))
    total_sub_uni_win_count = [0,0]
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                sub_uni_win_count = fn_to_run(position_p1,position_p2,score_p1, score_p2, i+j+k)
                for index in range(2):
                    total_sub_uni_win_count[index] += sub_uni_win_count[index]
    memo.update({(position_p1,position_p2,score_p1, score_p2, fn_to_run): total_sub_uni_win_count})
    return total_sub_uni_win_count

def p1_play(position_p1,position_p2,score_p1, score_p2, mv):
    global win_score
    position_p1 += mv
    if position_p1 > 10:
        position_p1 -= 10
    score_p1 += position_p1
    if score_p1 >= win_score:
        return [1,0]
    return split_and_play(position_p1,position_p2,score_p1, score_p2, p2_play)

def p2_play(position_p1,position_p2,score_p1, score_p2, mv):
    global win_score
    position_p2 += mv
    if position_p2 > 10:
        position_p2 -= 10
    score_p2 += position_p2
    if score_p2 >= win_score:
        return[0,1]
    return split_and_play(position_p1,position_p2,score_p1, score_p2, p1_play)

total_uni_win_count = split_and_play(position_p1,position_p2, 0, 0, p1_play)

print(max(total_uni_win_count))