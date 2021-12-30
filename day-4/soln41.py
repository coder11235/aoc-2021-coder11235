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
    for i in range(5):
        marked = [False]*5
        markedarr.append(marked)
    boardcheckedarray.append(markedarr)

def checkforhorizontalwin(boardarray):
    for i in boardarray:
        for j in i:
            if j == False:
                return False
    return True

def checkforverticalwin(boardarray):
    for i in range(5):
        won = True
        for j in range(5):
            if boardarray[j][i] == False:
                won = False
        if won:
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