raw = open('sample2.txt').read()
import functools

target_hallway = ('B','A','.','D','.','D','.','.','.','.','A')

target_rows = (('.', '.', '.', '.'),
('D', 'B', 'C', '.'),
('D', 'B', 'C', 'C'),
('A', 'B', 'C', 'A'))

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

# checks if the topmost amhipod needs to be moved in the column. returns row number if yes or None
def check_column_requirement(rows, col_num):
    topmost_amp_row = None
    for row_num, row in enumerate(rows):
        if row[col_num] != '.':
            topmost_amp_row = row_num
            break
    if topmost_amp_row is None:
        return
    correct_amp = AMHIPODS_ORDER[col_num]
    for row_num, row in reversed(list(enumerate(rows))):
        if row[col_num] == '.':
            return
        elif row[col_num] != correct_amp:
            return topmost_amp_row

states = {"banana"}

functools.cache
def move_amp(rows, hallway, cost_so_far):
    if (rows == target_rows) and (hallway == target_hallway):
        pass
    default_state = (
            (),
            (())
    )
    if (rows, hallway) in states:
        return float("inf"), [default_state]
    else:
        states.add((rows, hallway))
    if check_if_done(rows):
        return cost_so_far, [(rows, hallway)]

    finishing_costs = [(float('inf'), [default_state])]
    
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
        hashed_rows, hashed_hall = hashify(dup_rows, dup_hall)
        finishing_costs.append(move_amp(hashed_rows, hashed_hall, cost_so_far + extra_cost))

    # drive the amphipods out of their wrong rows
    for col_num in range(4):
        row_move_num = check_column_requirement(rows, col_num)
        if row_move_num is None:
            continue
        opp_hallway_pos = row_to_hallway(col_num)
        path_ranges = [range(opp_hallway_pos, 11), list(reversed(range(0, opp_hallway_pos)))]
        for path in path_ranges:
            for cur_pos in path:
                if not check_if_available(cur_pos):
                    continue
                if hallway[cur_pos] != '.':
                    break
                moving_amp = rows[row_move_num][col_num] 
                
                # move the amhipod here
                dup_rows, dup_hall = duplicate_data(rows, hallway)
                dup_hall[cur_pos] = moving_amp
                dup_rows[row_move_num][col_num] = '.'
                extra_cost = (abs(opp_hallway_pos-cur_pos)+row_move_num+1)*AMPHIPODS_COST[moving_amp]
                hashed_rows, hashed_hall = hashify(dup_rows, dup_hall)
                finishing_costs.append(move_amp(hashed_rows, hashed_hall, cost_so_far+extra_cost))

    min_cost_in_list = float("inf")
    min_state = []
    for cost, state in finishing_costs:
        if cost <= min_cost_in_list:
            min_cost_in_list = cost
            min_state = state
    min_state.append((rows, hallway))
    return min_cost_in_list, min_state

hashed_rows, hashed_hall = hashify(parsed_rows, parsed_hallway)
cost, res_states = move_amp(hashed_rows, hashed_hall, 0)
print(cost)
for r, h in res_states:
    debug_print(r, h)
