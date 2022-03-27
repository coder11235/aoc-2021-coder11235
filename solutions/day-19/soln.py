inp_type = "data"

data = open(f'data/{inp_type}.txt').read()


# list of all orientation transforms
transforms = [
  lambda a: ( a[0],  a[1],  a[2]),
  lambda a: ( a[1],  a[2],  a[0]),
  lambda a: ( a[2],  a[0],  a[1]),
  lambda a: (-a[0],  a[2],  a[1]),
  lambda a: ( a[2],  a[1], -a[0]),
  lambda a: ( a[1], -a[0],  a[2]),
  lambda a: ( a[0],  a[2], -a[1]),
  lambda a: ( a[2], -a[1],  a[0]),
  lambda a: (-a[1],  a[0],  a[2]),
  lambda a: ( a[0], -a[2],  a[1]),
  lambda a: (-a[2],  a[1],  a[0]),
  lambda a: ( a[1],  a[0], -a[2]),
  lambda a: (-a[0], -a[1],  a[2]),
  lambda a: (-a[1],  a[2], -a[0]),
  lambda a: ( a[2], -a[0], -a[1]),
  lambda a: (-a[0],  a[1], -a[2]),
  lambda a: ( a[1], -a[2], -a[0]),
  lambda a: (-a[2], -a[0],  a[1]),
  lambda a: ( a[0], -a[1], -a[2]),
  lambda a: (-a[1], -a[2],  a[0]),
  lambda a: (-a[2],  a[0], -a[1]),
  lambda a: (-a[0], -a[2], -a[1]),
  lambda a: (-a[2], -a[1], -a[0]),
  lambda a: (-a[1], -a[0], -a[2]),
]

reverse_trans = [0,2,1,3,10,8,9,7,5,6,4,11,12,17,19,15,20,13,18,14,16,21,22,23]


def subtract(a, b):
    """subtracts b from a in coordinate format"""
    return tuple([s_axis_val - b[s_axis_index] for s_axis_index, s_axis_val in enumerate(a)])

def add(a, b):
    """adds b to a in coordinate format"""
    return tuple([s_axis_val + b[s_axis_index] for s_axis_index, s_axis_val in enumerate(a)])

# converts from list[list] to set(tuple) for comparision purposes
setify = lambda list: set([tuple(x) for x in list])


def parse(data):
    """
    accepts: raw input scanner data (data)
    returns: simple data parsed to ints and complex data with beacons relative to each other
    """
    scanners = []
    scanners_beacon_to_beacon_rel = []

    for scanner in data.split('\n\n'):
        beacon_strs = scanner.splitlines()[1:]
        beacon_orig_proc = [tuple([int(axis) for axis in be.split(',')]) for be in beacon_strs]
        scanners.append(beacon_orig_proc)

        orientations = []
        for orientation_index in range(24):
            beacon_trans = [transforms[orientation_index](beacon) for beacon in beacon_orig_proc] 

            main_beacons_proc = []
            for main_beacon in beacon_trans[:len(beacon_trans)-11]:
                relative_beacons = set([subtract(second_beacon, main_beacon) for second_beacon in beacon_trans])
                main_beacons_proc.append(relative_beacons)
            orientations.append((orientation_index, main_beacons_proc))

        scanners_beacon_to_beacon_rel.append(orientations)

    return scanners, scanners_beacon_to_beacon_rel

def find_connections(scanners: list):
    """
    accepts: complex scanner data
    returns: connections each scanner has with one another under which orientation
    """
    relative_scanner_orientations = {}

    def check_if_scanner_match(main, secondary):
        _, main_beacons = main[0]
        for orientation_index, second_beacons in secondary:
            for main_beacon in main_beacons:
                for second_beacon in second_beacons:
                    common_relatives = main_beacon&second_beacon
                    if len(common_relatives) >= 12:
                        return orientation_index

    for main_index, main in enumerate(scanners):
        for secondary_index, secondary in enumerate(scanners[:main_index]):
            if main_index == secondary_index: continue
            # goal
            check_res = check_if_scanner_match(main, secondary)
            if check_res is not None:
                relative_scanner_orientations[(main_index, secondary_index)] = check_res
                relative_scanner_orientations[(secondary_index, main_index)] = reverse_trans[check_res]

    return relative_scanner_orientations


def find_abs_orientations(connections):
    """
    accepts: the relations of scanners
    returns: the functions applied from end to start to set a scanner to 0th position
    """
    absolute_orientations = {0: [0]}

    def check_if_all_found():
        for i in range(30 if inp_type == "data" else 5):
            if i not in absolute_orientations:
                return False
        return True

    def find_absolute():
        for i in connections:
            main, sec = i
            if main not in absolute_orientations and sec in absolute_orientations:
                absolute_orientations[main] = absolute_orientations[sec] + [connections[(sec, main)]]
        
        if not check_if_all_found():
            find_absolute()

    find_absolute()
    return absolute_orientations


def reset_orientation(abs_orientations_functions, scanners):
    """
    accepts: the absolute orientation functions, simple scanner data
    returns: [simple scanner data, complex scanner data] with the right orientations
    """
    orientation_reset_scanners = []
    for scanner_num, beacons in enumerate(scanners):
        for fn in reversed(abs_orientations_functions[scanner_num]):
            beacons = [transforms[fn](beacon) for beacon in beacons]
        relative_beacons = []
        for main_beacon in beacons[:len(beacons)-11]:
            relative_to_main = []
            for secondary_beacon in beacons:
                relative_to_main.append(subtract(secondary_beacon, main_beacon))
            relative_beacons.append(relative_to_main)
        orientation_reset_scanners.append([beacons, relative_beacons])
    return orientation_reset_scanners


def find_scanner_pos(connections, scanners):
    """
    accepts: connections, complex scanner data
    returns: positions of all scanners relative to scanner 0
    """
    def find_matching_beacons(main, secondary):
        for mi, main_beacon in enumerate(main):
            for si, secondary_beacon in enumerate(secondary):
                if len(set(main_beacon)&set(secondary_beacon)) >= 12:
                    return mi, si

    scanner_abs_coordinates = {0: [0,0,0]}

    def check_if_all_found():
        for i in range(30 if inp_type == "data" else 5):
            if i not in scanner_abs_coordinates:
                return False
        return True

    def find_absolute():
        for i in connections:
            main, secondary = i
            if main in scanner_abs_coordinates and secondary not in scanner_abs_coordinates:
                main_beacon_index, sec_beacon_index = find_matching_beacons(scanners[main][1], scanners[secondary][1])
                sec_pos_to_main = subtract(scanners[main][0][main_beacon_index], scanners[secondary][0][sec_beacon_index])
                scanner_abs_coordinates[secondary] = add(scanner_abs_coordinates[main], sec_pos_to_main)
        if not check_if_all_found():
            find_absolute()

    find_absolute()
    return scanner_abs_coordinates


def solve_1(scanner_pos, scanners):
    """
    accepts: positions of all scanners, simple scanner data
    returns: the number of beacons
    """
    all_beacons = set()
    for index, scanner in enumerate(scanners):
        beacons, _ = scanner
        for beacon in beacons:
            abs_pos = add(beacon, scanner_pos[index])
            all_beacons.add(tuple(abs_pos))

    return len(all_beacons)

def solve_2(scanner_pos):
    """
    accepts: positions of all scanners
    returns: greatest manhattan distance
    """
    highest = 0
    for i in scanner_pos.values():
        for j in scanner_pos.values():
            dist = sum([abs(a) for a in subtract(i, j)])
            if dist > highest:
                highest = dist
    return highest


mixed_o_simple_scanners, mixed_o_complex_scanners = parse(data)
connections = find_connections(mixed_o_complex_scanners)
abs_orientation_functions = find_abs_orientations(connections)
resetted_scanners = reset_orientation(abs_orientation_functions, mixed_o_simple_scanners)
scanner_abs_pos = find_scanner_pos(connections, resetted_scanners)
print("solution 1 :", solve_1(scanner_abs_pos, resetted_scanners))
print("solution 2 :", solve_2(scanner_abs_pos))