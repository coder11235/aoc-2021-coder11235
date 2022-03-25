import math
from typing_extensions import Self


inp = open('sample.txt').read()

def parse(inp: str):
    inp = inp.splitlines()[2:4]
    hallway = ['#']*11
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

class States:
    states = []

    def hasher(rows, hallway):
        return tuple([tuple(row) for row in rows]), tuple(hallway)
    
    def add_state(self, rows, hallway):
        hashed = self.hasher(rows, hallway)
        if hashed in self.states:
            return hashed
        else:
            self.states[hashed] = float("inf")

    def update_state(self, rows, hallway, cost_to_goal):
        hashed = self.hasher(rows, hallway)
        self.states[hashed] = cost_to_goal

dpr(rows, hallway)

AMPHIPODS = ['A', 'B', 'C', 'D']

states = States()

row_to_hallway = lambda x: x*2

cost_for_amphi = lambda a: pow(10, AMPHIPODS.index(a))

copy_row = lambda rows: [row.copy() for row in rows]
    

def move(rows: list[list], hallway: list, cost_so_far: int):
    state_res = states.add_state(rows, hallway)
    if state_res is not None:
        return state_res

    costs = []

    # move the amphipods in the hallway
    for pos, amphipod in enumerate(hallway):
        if amphipod != '#':
            row_index = AMPHIPODS.index(amphipod)
            target_pos = row_to_hallway(row_index)
            path: list = []
            if target_pos > pos:
                path = hallway[pos+1:target_pos+1]
            else:
                path = hallway[target_pos:pos]
            if all([x == '#' for x in path]):
                if rows[1][row_index] == '#' and rows[0][row_index] == '#':
                    rt = copy_row(rows)
                    ht = hallway.copy()
                    ht[pos] = '#'
                    rt[1][row_index] = amphipod
                    added_cost = cost_so_far + cost_for_amphi(len(path)+2)
                    move(rt, ht, added_cost)
                elif rows[1][row_index] == amphipod and rows[0][row_index] == '#':
                    rt = copy_row(rows)
                    ht = hallway.copy()
                    ht[pos] = '#'
                    rt[0][row_index] = amphipod
                    added_cost = cost_so_far + cost_for_amphi(len(path)+1)
                    move(rt, ht, added_cost)
    
    # move the amphipods in the top row
    for pos, amp in enumerate(rows[0]):
        if amp != '#' and (amp != AMPHIPODS[pos] or rows[1][pos] != AMPHIPODS[pos]):
            hallway_equiv = row_to_hallway(pos)
            