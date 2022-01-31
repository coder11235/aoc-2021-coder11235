inp = open('sample.txt').read()

def parse(inp: str):
    inp = inp.splitlines()[2:4]
    hallway = [[' ']*11]
    rows = []
    for i in inp:
        row = []
        for j in i:
            if j.isalpha():
                row.append(j)
        rows.append(row)
    return rows, hallway

rows, hallway = parse(inp)
def dpr(rows, hallway):
    for i in hallway:
        print(i, end='')
    for i in rows[1:]:
        print()
        print('  ', end='')
        for el in i:
            print(el, end=' ')

dpr(rows, hallway)

def check_row(rows, index):
    if rows[0][index] == rows[1][index] and rows[1] != ' ':
        return True
    return False

def play(hallway, rows, in_frnt=False, frm_lft=False, pos=0):
    hallway = hallway.copy()
    rows = [row.copy() for row in rows]
    if in_frnt:

        #move across thw hallway
        if frm_lft:
            if pos < (len(hallway)-1) and hallway[pos+1] == ' ':
                hallway[pos+1] = hallway[pos]
                hallway[pos] = ' '
                play(hallway, rows)
                hallway[pos] = hallway[pos+1]
                hallway[pos+1] = ' '
        else:
            if pos > 0 and hallway[pos-1] == ' ':
                hallway[pos-1] = hallway[pos]
                hallway[pos] = ' '
                play(hallway, rows)
                hallway[pos] = hallway[pos-1]
                hallway[pos-1] = ' '

        #move into the room
        entrance_num = pos/2
        cloned_rows = rows.copy()
        if cloned_rows[0][entrance_num] == ' ':
            cloned_rows[0][entrance_num] = hallway[pos]
            if check_row(cloned_rows):
                rows = cloned_rows
                hallway[pos] = ' '
                play()

    # if any room has one in the upper but none in the lower
    for i in range(4):
        if rows[1][i] == ' ' and rows[0][i] != ' ':
            rows[1][i] == 

    for i in range(4):
        if rows[0][i] == rows[1][i]:
            continue