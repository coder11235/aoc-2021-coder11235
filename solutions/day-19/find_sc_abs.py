from json import load, dump

inp_type = "data"

scanners = load(open(f'data/sc_reset_{inp_type}.json'))
connections = load(open(f'data/scan_rel_orient_{inp_type}.json'))

setify = lambda list: set([tuple(x) for x in list])

def subtract(b, a):
    """
    subtracts b from a (a-b)
    """
    return [s_axis_val - b[s_axis_index] for s_axis_index, s_axis_val in enumerate(a)]

def add(a, b):
    return [s_axis_val + b[s_axis_index] for s_axis_index, s_axis_val in enumerate(a)]

def find_matching_beacons(main, secondary):
    for mi, main_beacon in enumerate(main):
        for si, secondary_beacon in enumerate(secondary):
            if len(setify(main_beacon)&setify(secondary_beacon)) >= 12:
                return mi, si

scanner_abs_coordinates = {0: [0,0,0]}

def check_if_all_found():
    for i in range(30 if inp_type == "data" else 5):
        if i not in scanner_abs_coordinates:
            return False
    return True

def find_absolute():
    for i in connections:
        sc, _ = i
        main, secondary = sc
        if (main in scanner_abs_coordinates) ^ (secondary in scanner_abs_coordinates):
            main_beacon_index, sec_beacon_index = find_matching_beacons(scanners[main][1], scanners[secondary][1])
            if main in scanner_abs_coordinates:
                sec_pos_to_main = subtract(scanners[secondary][0][sec_beacon_index], scanners[main][0][main_beacon_index])
                scanner_abs_coordinates[secondary] = add(scanner_abs_coordinates[main], sec_pos_to_main)
    if not check_if_all_found():
        find_absolute()

find_absolute()

dump(scanner_abs_coordinates, open(f'data/scanner_abs_pos_{inp_type}.json', 'w'))