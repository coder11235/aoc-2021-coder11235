from json import load, dump

inp_type = "data"

scanner_relations = load(open(f'data/scan_rel_orient_{inp_type}.json'))

def parse_inp_to_map():
    rel_map = {}
    for i in scanner_relations:
        sc, o = i
        m, s = sc
        rel_map[(m, s)] = o
    return rel_map

scanner_relations = parse_inp_to_map()

# contains the functions u need to reach 0 from that point (orientation is set to 0 cuz thats the default one)
absolute_orientations = {0: [0]}

def check_if_all_found():
    for i in range(30 if inp_type == "data" else 5):
        if i not in absolute_orientations:
            return False
    return True

def find_absolute():
    for i in scanner_relations:
        main, sec = i
        if main not in absolute_orientations and sec in absolute_orientations:
            absolute_orientations[main] = absolute_orientations[sec] + [scanner_relations[(sec, main)]]
    if not check_if_all_found():
        find_absolute()

find_absolute()

## now reset the orientations

scanners_raw = open(f'data/{inp_type}.txt').read()

orientation_reset_scanners = []

transforms = [
  lambda a: [ a[0],  a[1],  a[2]],
  lambda a: [ a[1],  a[2],  a[0]],
  lambda a: [ a[2],  a[0],  a[1]],
  lambda a: [-a[0],  a[2],  a[1]],
  lambda a: [ a[2],  a[1], -a[0]],
  lambda a: [ a[1], -a[0],  a[2]],
  lambda a: [ a[0],  a[2], -a[1]],
  lambda a: [ a[2], -a[1],  a[0]],
  lambda a: [-a[1],  a[0],  a[2]],
  lambda a: [ a[0], -a[2],  a[1]],
  lambda a: [-a[2],  a[1],  a[0]],
  lambda a: [ a[1],  a[0], -a[2]],
  lambda a: [-a[0], -a[1],  a[2]],
  lambda a: [-a[1],  a[2], -a[0]],
  lambda a: [ a[2], -a[0], -a[1]],
  lambda a: [-a[0],  a[1], -a[2]],
  lambda a: [ a[1], -a[2], -a[0]],
  lambda a: [-a[2], -a[0],  a[1]],
  lambda a: [ a[0], -a[1], -a[2]],
  lambda a: [-a[1], -a[2],  a[0]],
  lambda a: [-a[2],  a[0], -a[1]],
  lambda a: [-a[0], -a[2], -a[1]],
  lambda a: [-a[2], -a[1], -a[0]],
  lambda a: [-a[1], -a[0], -a[2]],
]

def find_relative(orig, second):
    """
    finds relative coordinate of second beacon to orig beacon
    """
    return [s_axis_val - orig[s_axis_index] for s_axis_index, s_axis_val in enumerate(second)]

for scanner_num, scanner in enumerate(scanners_raw.split('\n\n')):
    beacon_strs = scanner.splitlines()[1:]
    beacons = [[int(axis) for axis in be.split(',')] for be in beacon_strs]
    for fn in reversed(absolute_orientations[scanner_num]):
        beacons = [transforms[fn](beacon) for beacon in beacons]
    relative_beacons = []
    for main_beacon in beacons:
        relative_to_main = []
        for secondary_beacon in beacons:
            relative_to_main.append(find_relative(main_beacon, secondary_beacon))
        relative_beacons.append(relative_to_main)
    orientation_reset_scanners.append([beacons, relative_beacons])

dump(orientation_reset_scanners, open(f"data/sc_reset_{inp_type}.json", 'w'))