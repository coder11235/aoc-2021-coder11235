raw = open('sample2.txt').read()

def parse(raw_data: str):
    rows = []
    for ln in raw_data.splitlines()[2:6]:
        row = []
        for c in ln:
            if c.isalpha():
                row.append(c)
        rows.append(row)
    return rows, ['.' for _ in range(11)]

parsed_rows, parsed_hallway = parse(raw)

# numerical check if you can move into this spot on the hallway
def check_if_available(num):
    if num == 0 or num == 10:
        return True
    else:
        return num%2!=0

# maps amphipods to their cost of movement
AMPHIPODS_COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

# the home positions of the amphipods
AMPHIPODS_HOME_HALLWAY = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
AMPHIPODS_HOME_ROW = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

# the amphipods in this row or smth
AMHIPODS_ORDER = ['A', 'B', 'C', 'D']

# conveting the index of the row and the pos of the hallway in front of the row
hallway_to_row = lambda x: x//2-1
row_to_hallway = lambda x: (x+1)*2

def debug_print(rows, hallway):
    for i in hallway:
        print(i, end='')
    print('')
    for i in rows:
        print(' #', end='')
        for j in i:
            print(j, end='#')
        print('')
    print('')

# converts the rows and hallways from lists to tuples
def hashify(rows, hallway):
    if rows[0] is not tuple:
        hashed_rows: tuple[tuple[str]] = tuple(tuple(row) for row in rows)
    else:
        hashed_rows = rows
    return hashed_rows, tuple(hallway)

# checks if the amphipods have all reached the correct positions
def check_if_done(rows):
    for row in rows:
        for loc, amp in enumerate(row):
            if amp == '.' or AMPHIPODS_HOME_ROW[amp] != loc:
                return False
    return True


# just clones rows and hallway
def duplicate_data(rows, hallway):
    if rows is not list:
        new_rows = [list(row) for row in rows]
    else:
        print(rows)
        new_rows = [row.copy() for row in rows]
    return new_rows, hallway.copy() if hallway is list else list(hallway)

# check if the home of the amphipod has any other amphipod or is free to move into. returns the free row
def check_home_space(amp, rows):
    amp_home_row = AMPHIPODS_HOME_ROW[amp]
    for index, row in reversed(list(enumerate(rows))):
        if row[amp_home_row] == amp:
            continue
        elif row[amp_home_row] == '.':
            return index
        else:
            return None

# checks if a given path in the hallway is empty
def check_path_empty(hallway, pos, target):
    path = None
    if pos < target:
        path = range(pos+1, target)
    else:
        path = range(target, pos)
    for cur in path:
        if hallway[cur] != '.':
            return False
    return True


def move_amp(rows, hallway, cost_so_far):
    
    # move the amphipods into their rows from the hallway
    for pos, amp in enumerate(hallway):
        if amp == ".":
            continue
        to_move_index = check_home_space(amp, rows)
        if to_move_index is None:
            continue
        amp_hallway_home = AMPHIPODS_HOME_HALLWAY[amp]
        if not check_path_empty(hallway, pos, amp_hallway_home):
            continue
        extra_cost = (abs(pos-amp_hallway_home) + to_move_index + 1)*AMPHIPODS_COST[amp]

        dup_rows, dup_hall = duplicate_data(rows, hallway)
        dup_hall[pos] = '.'
        dup_rows[to_move_index][AMPHIPODS_HOME_ROW[amp]] = amp
        move_amp(dup_rows, dup_hall, cost_so_far + extra_cost)

    # drive the amphipods out of their wrong rows
    for col_num in range(4):
        out_of_order = False
        for row_num, row in reversed(list(enumerate(rows))):
            if row[col_num] == AMHIPODS_ORDER[col_num]:
                continue
            if not out_of_order:
                if row[col_num] == '.':
                    break
            else:
                # the logic for moving the amhipod
                opp_hallway_pos = row_to_hallway(col_num)
                path_ranges = map(
                    lambda r: filter(check_if_available, r), 
                    [range(opp_hallway_pos+1, 11), reversed(range(opp_hallway_pos))]
                )
                for pr in path_ranges:
                    for cur_pos in pr:
                        if hallway[cur_pos] != '.':
                            break
                        else:

            out_of_order = True
