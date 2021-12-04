file = open('datat.txt', 'r')

boards = file.read()
boards = boards.split('\n\n')

# parse input
numbers = boards.pop(0)
boards = [board.split('\n') for board in boards]
boards:list[list] = [[row.strip().replace('  ', ' ').split(' ') for row in board] for board in boards]

boardcheckedarray = []
for i in range(0, len(boards)):
    markedarr = []
    for i in range(0, 6):
        marked = [False]*5
        markedarr.append(marked)
    boardcheckedarray.append(markedarr)

def checkforhorizontalwin(boardarray):
    for i in boardarray:
        val = i[0]
        if val == False:
            continue
        won = True
        for j in i:
            if val != j:
                won = False
        if won == True:
            return True
    return False

def checkforverticalwin(boardarray):
    for i in range(0, 5):
        val = boardarray[0][i]
        won = True
        if val == False:
            continue
        for j in range(0, 5):
            if boardarray[j][i] != val:
                won = False
        if won == True:
            return True
    return False

def checkoff(boardarray: list[list], number, marked: list[list]):
    indexi = None
    indexj = None
    for i in range(0,5):
        for j in range(0,5):
            if boardarray[i][j] == number:
                indexi = i
                indexj = j
    if indexi is not None:
        marked[indexi][indexj] = True

def summify(board: list[list[str]], marked: list[list[str]], number):
    sum = 0
    for i in range(0, 5):
        for j in range(0,5):
            if marked[i][j] == False:
                sum += int(board[i][j])
    return sum * int(number)


numbers = numbers.split(',')
for number in numbers:
    for boardnum in range(0, len(boards)):
        checkoff(boards[boardnum], number, boardcheckedarray[boardnum])
        haswon = checkforhorizontalwin(boardcheckedarray[boardnum]) or checkforverticalwin(boardcheckedarray[boardnum])
        if haswon:
            print(summify(boards[boardnum], boardcheckedarray[boardnum], number))
            exit()