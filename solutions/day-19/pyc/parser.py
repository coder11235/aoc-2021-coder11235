data = open('sample.txt').read()
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
    lambda a: [-a[0], a[1], a[2]],
    lambda a: [a[0], -a[1], a[2]],
    lambda a: [a[0], a[1], -a[2]],
    lambda a: [-a[0], -a[1], a[2]],
    lambda a: [a[0], -a[1], -a[2]],
    lambda a: [-a[0], a[1], -a[2]],
    lambda a: [-a[0], -a[1], -a[2]],
    lambda a: [a[0], a[1], a[2]],
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
    for i in range(7):
        for j in range(3):
            lst.append([i, j])
    return lst

scanners = data.split('\n\n')

scanners_proc = []
for scanner in scanners:
    orientations = []
    for tri in get_tr_indices():
        beacons_raw = scanner.splitlines()[1:]
        beacons_proc = [
            translate(tri[0], tri[1], [
                int(val) for val in be.split(',')
            ]) for be in beacons_raw
        ]
        beacons_relatives = []
        for beacon in beacons_proc:
            relative_beacons = [find_relative_beacon_pos(beacon, sec) for sec in beacons_proc]
            beacons_relatives.append(relative_beacons)
        orientations.append({
            "orientation": tri,
            "beacons": beacons_relatives
            })
    scanners_proc.append(orientations)

with open('scanner_detecter/parsed_scanners.json', 'w') as fl:
    json.dump(scanners_proc, fl)