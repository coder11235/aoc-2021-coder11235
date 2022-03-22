data = open('../data/data.txt').read()
from functools import cache
import json

"""
schema(?) for each scanner
scanners
    - scanner
        - orientation data
        - beacons
            beacon
                - all beacons relative to it
"""

negative_functions = [
    lambda a: [a[0], a[1], a[2]],
    lambda a: [-a[0], a[1], a[2]],
    lambda a: [a[0], -a[1], a[2]],
    lambda a: [a[0], a[1], -a[2]],
    lambda a: [-a[0], -a[1], a[2]],
    lambda a: [a[0], -a[1], -a[2]],
    lambda a: [-a[0], a[1], -a[2]],
    lambda a: [-a[0], -a[1], -a[2]],
]

rotation_functions = [
    (
        lambda a: [a[0], a[1], a[2]],
        lambda a: [a[0], a[1], a[2]],
    ),
    (
        lambda a: [a[2], a[0], a[1]],
        lambda a: [a[1], a[2], a[0]],
    ),
    (
        lambda a: [a[1], a[2], a[0]],
        lambda a: [a[2], a[0], a[1]],
    )
]

def translate(neg, rot, coord):
    return negative_functions[neg](rotation_functions[rot][0](coord))


def find_relative_beacon_pos(main_beacon, seconday_beacon):
    """
    accepts: 2 beacon coords
    returns the coord of the second beacon with respect to the first beacon
    """
    return [main_beacon[axis]-val for axis, val in enumerate(seconday_beacon)]

cache
def get_tr_indices():
    """
    just gets a tuple from 0-7 and 0-2
    """
    lst = []
    for i in range(8):
        for j in range(3):
            lst.append([i, j])
    return lst

scanners = data.split('\n\n')

processed_scanners = []
for scanner in scanners:
    orientations = []
    beacons_raw = scanner.splitlines()[1:]
    beacons_parsed = [[int(axis) for axis in beacon.split(',')] for beacon in beacons_raw]
    for neg_index, rot_index in get_tr_indices():
        transformed_beacons = [translate(neg_index, rot_index, beacon) for beacon in beacons_parsed]
        all_beacons_relatives = []
        for beacon in transformed_beacons:
            relative_beacons = [find_relative_beacon_pos(beacon, secondary_beacon) for secondary_beacon in transformed_beacons]
            all_beacons_relatives.append(relative_beacons)
        orientations.append({
            "orientation": [neg_index, rot_index],
            "beacons": all_beacons_relatives
        })
    processed_scanners.append(orientations)

with open('../data/data_parsed_1.json', 'w') as fl:
    json.dump(processed_scanners, fl)