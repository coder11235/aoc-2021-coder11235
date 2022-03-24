from json import load, dump

inp_type = "data"

scanners = load(open(f'data/parsed_{inp_type}.json'))

relative_scanner_orientations = []

# converts from
# [[x,y,z], [x,y,z]]
# to
# {(x,y,z), (x,y,z)}
# for finding common beacons using set and
setify = lambda list: set([tuple(x) for x in list])

def check_if_scanner_match(main, secondary):
    """
    accepts both scanners and check if they match
    scanner = [orientation, beacons]
    returns the orientation of the second scanner if they do or None
    """
    _, main_beacons, og_main = main[0] # og_main -> scanner's beacons under the first orientation
    # main beacons = all the beacon sets data
    for orientation_index, second_beacons, og_second in secondary: # main scanner's beacons under every first orientation
        for main_beacon in main_beacons:
            for second_beacon in second_beacons:
                common_relatives = setify(main_beacon)&setify(second_beacon)
                if len(common_relatives) >= 12:
                    return orientation_index

for main_index, main in enumerate(scanners):
    print(main_index)
    for secondary_index, secondary in enumerate(scanners):
        if main_index == secondary_index: continue
        # goal
        check_res = check_if_scanner_match(main, secondary)
        if check_res is not None:
            relative_scanner_orientations.append([[main_index, secondary_index], check_res])

dump(relative_scanner_orientations, open(f'data/scan_rel_orient_{inp_type}.json', 'w'))