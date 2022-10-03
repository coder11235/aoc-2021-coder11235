import functools

raw = open("data.txt").read()

def process_inp(raw_inp):
    raw_inp = raw_inp.splitlines()
    rows = []
    for i in raw_inp[2:4]:
        cur_row = []
        for chr in i:
            if chr.isalpha():
                cur_row.append(chr)
        rows.append(cur_row)
    return rows, ['.' for _ in range(11)]

rows, hallway = process_inp(raw)

# numerical check if you can move into this spot on the hallway
def check_if_available(num):
    if num == 0 or num == 10:
        return True
    else:
        return num%2!=0

# maps amphipods to their cost of movement
AMPHIPODS_COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

AMPHIPODS_HOME = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
AMPHIPODS_HOME_ROW = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

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

def hashify(rows, hallway):
    if rows[0] is not tuple:
        hashed_rows: tuple[tuple[str]] = tuple(tuple(row) for row in rows)
    else:
        hashed_rows = rows
    return hashed_rows, tuple(hallway)

def check_if_done(rows):
    for row in rows:
        for loc, amp in enumerate(row):
            if amp == '.' or AMPHIPODS_HOME_ROW[amp] != loc:
                return False
    return True

def check_path_empty(hallway, home_hallway_spot,loc):
    # setup a path range to check if any other apmhipods are there
    path_range = []
    if loc > home_hallway_spot:
        path_range = list(range(home_hallway_spot, loc))
    else:
        path_range = list(range(loc+1, home_hallway_spot))
    for i in path_range:
        if hallway[i] != '.':
            return False
    return True

def duplicate_data(hallway, rows):
    # just clones rows and hallway
    if rows is not list:
        new_rows = [list(row) for row in rows]
    else:
        print(rows)
        new_rows = [row.copy() for row in rows]
    return hallway.copy() if hallway is list else list(hallway), new_rows

@functools.cache
def move_amp(rows, hallway, cost_so_far):
    # check if everything is okay
    if check_if_done(rows):
        return cost_so_far

    cost_to_finals = [(float("inf"))]

    #split rows to make life easier
    upper_row = rows[0]
    lower_row = rows[1]

    # move all amphipods in the hallway to their place
    for loc, amp in enumerate(hallway):
        if amp.isalpha():

            # safety measures
            home_hallway_spot = AMPHIPODS_HOME[amp]
            if not check_path_empty(hallway, home_hallway_spot, loc):
                continue
            home_row_spot = hallway_to_row(home_hallway_spot)
            if upper_row[home_row_spot] != '.':
                continue
            if not (lower_row[home_row_spot] == amp or lower_row[home_row_spot] == '.'):
                continue

            # move the amphipods
            dup_hallway, dup_rows = duplicate_data(hallway, rows)
            extra_cost = 0
            if lower_row[home_row_spot] == '.':
                dup_rows[1][home_row_spot] = amp
                extra_cost = (abs(home_hallway_spot-loc)+2)*AMPHIPODS_COST[amp]
            else:
                dup_rows[0][home_row_spot] = amp
                extra_cost = (abs(home_hallway_spot-loc)+1)*AMPHIPODS_COST[amp]
            dup_hallway[loc] = '.'
            hashed_rows, hashed_hall = hashify(dup_rows, dup_hallway)
            cost_to_finals.append(move_amp(hashed_rows, hashed_hall, cost_so_far+extra_cost))

    # do the rows

    # upper row movement
    for loc, amp in enumerate(upper_row):
        # safety
        if amp == '.': continue
        amp_home_row = hallway_to_row(AMPHIPODS_HOME[amp])
        if amp_home_row == loc and lower_row[loc] == amp:
            continue

        opp_hallway_pos = row_to_hallway(loc)
        # move
        for i in range(2):
            path_ranges = None
            if i == 0:
                path_ranges = range(opp_hallway_pos, 11)
            else:
                path_ranges = range(0, opp_hallway_pos)
            for cur_pos in path_ranges:
                # safety
                if not check_if_available(cur_pos):
                    continue
                if hallway[cur_pos] != '.':
                    break

                dup_hallway, dup_rows = duplicate_data(hallway, rows)
                dup_hallway[cur_pos] = amp
                dup_rows[0][loc] = '.'
                extra_cost = (abs(opp_hallway_pos-cur_pos)+1)*AMPHIPODS_COST[amp]
                hashed_rows, hashed_hall = hashify(dup_rows, dup_hallway)
                cost_to_finals.append(move_amp(hashed_rows, hashed_hall, cost_so_far+extra_cost))

    # lower row movement
    for loc,amp in enumerate(lower_row):
        #safety
        if amp == '.': continue
        amp_home_row = hallway_to_row(AMPHIPODS_HOME[amp])
        if amp_home_row == loc or upper_row[loc] != '.': continue

        opp_hallway_pos = row_to_hallway(loc)
        # move
        for i in range(2):
            path_ranges = None
            if i == 0:
                path_ranges = range(opp_hallway_pos, 11)
            else:
                path_ranges = reversed(range(0, opp_hallway_pos))
            for cur_pos in path_ranges:
                # safety
                if not check_if_available(cur_pos):
                    continue
                if hallway[cur_pos] != '.':
                    break

                dup_hallway, dup_rows = duplicate_data(hallway, rows)
                dup_hallway[cur_pos] = amp
                dup_rows[1][loc] = '.'
                extra_cost = (abs(opp_hallway_pos-cur_pos)+2)*AMPHIPODS_COST[amp]
                hashed_rows, hashed_hall = hashify(dup_rows, dup_hallway)
                cost_to_finals.append(move_amp(hashed_rows, hashed_hall, cost_so_far+extra_cost))

    return min(cost_to_finals)

hashed_rows, hashed_hall = hashify(rows, hallway)

cost = move_amp(hashed_rows, hashed_hall, 0) 

print(cost)
