from json import load

inp_type = 'data'

scanner_pos = load(open(f'data/scanner_abs_pos_{inp_type}.json'))
scanners = load(open(f"data/sc_reset_{inp_type}.json"))

def add(a, b):
    return [s_axis_val + b[s_axis_index] for s_axis_index, s_axis_val in enumerate(a)]

all_beacons = set()

for index, scanner in enumerate(scanners):
    beacons, _ = scanner
    for beacon in beacons:
        abs_pos = add(beacon, scanner_pos[str(index)])
        all_beacons.add(tuple(abs_pos))

print(len(all_beacons))