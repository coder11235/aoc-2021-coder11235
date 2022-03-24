from functools import cache
from collections import deque
from json import dump

inp_type = "data"

data = open(f'data/{inp_type}.txt').read()

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
];

def find_relative(orig, second):
    """
    finds relative coordinate of second beacon to orig beacon
    """
    return [s_axis_val - orig[s_axis_index] for s_axis_index, s_axis_val in enumerate(second)]

scanners = []

for scanner in data.split('\n\n'):
     # raw data of all beacons in str format
    beacon_strs = scanner.splitlines()[1:]

    # the beacons but parsed to integer arrays
    beacon_orig_proc = [[int(axis) for axis in be.split(',')] for be in beacon_strs]

    # all the beacon sets in the orientation to be filled in below loop
    orientations = []

    for orientation_index in range(24):
        # all the beacon coordinates in this specefic orientation
        beacon_trans = [transforms[orientation_index](beacon) for beacon in beacon_orig_proc] 

        # the final beacon sets of this orientation to be filled
        main_beacons_proc = []
        for main_beacon in beacon_trans:
            relative_beacons = [find_relative(main_beacon, second_beacon) for second_beacon in beacon_trans]
            main_beacons_proc.append(relative_beacons)

        # appends the way the scanner was rotated for this, the list of beacon sets(each containing relative beacons to one beacon) and all beacons in this orientation
        orientations.append([orientation_index, main_beacons_proc, beacon_trans])
    scanners.append(orientations)

dump(scanners, open(f'data/parsed_{inp_type}.json', 'w'))