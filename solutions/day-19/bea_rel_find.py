from json import load, dump

inp_type = "sample"

scanners = load(open(f'data/parsed_{inp_type}.json'))

logs = open('data/logs.txt','w')

relative_scanner_orientations = []

def beacon_tupler(beacon):
    return [tuple(rel) for rel in beacon]

def check_if_beacons_match(b1, b2):
    """
    takes 2 beacon sets
    beacon 1:
    [
        relative_beacons:
        [0,0,0]
        [a,b,c]
    ]
    """
    return len(set(beacon_tupler(b1))&set(beacon_tupler(b2)))

def check_if_scanner_match(main, secondary):
    """
    accepts both scanners and check if they match
    scanner = [orientation, beacons]
    returns the orientation of the second scanner if they do or None
    """
    _, main_beacons = main[0]
    for orientation_index, second_beacons in secondary:
        for mi, main_beacon in enumerate(main_beacons):
            for si, second_beacon in enumerate(second_beacons):
                common_relatives = check_if_beacons_match(main_beacon, second_beacon)
                if common_relatives > 2 :
                    logs.write(f"orientation : {orientation_index}\n{mi} -> {si} = {common_relatives}\n")
                    if common_relatives >= 12:
                        return orientation_index

for main_index, main in enumerate(scanners):
    print(main_index)
    logs.write(f"main scanner: {main_index}\n")
    for secondary_index, secondary in enumerate(scanners):
        if main_index == secondary_index: continue
        logs.write(f"secondary scanner: {secondary_index}\n")
        # goal
        check_res = check_if_scanner_match(main, secondary)
        if check_res is not None:
            relative_scanner_orientations.append([[main_index, secondary_index], check_res])

dump(relative_scanner_orientations, open(f'data/scan_rel_orient_{inp_type}.json', 'w'))