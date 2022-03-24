from json import load

inp_type = 'data'

data: dict = load(open(f'data/scanner_abs_pos_{inp_type}.json'))

def subtract(b, a):
    """
    subtracts b from a (a-b)
    """
    return [s_axis_val - b[s_axis_index] for s_axis_index, s_axis_val in enumerate(a)]

highest = 0

for i in data.values():
    for j in data.values():
        dist = sum([abs(a) for a in subtract(i, j)])
        if dist > highest:
            highest = dist

print(highest)