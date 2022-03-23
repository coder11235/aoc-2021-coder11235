from functools import cache
from collections import deque
from json import dump

inp_type = "sample"

data = open(f'data/{inp_type}.txt').read()

negative_orientations = [
    lambda x: [x[0], x[1], x[2]],
    lambda x: [-x[0], x[1], x[2]],
    lambda x: [x[0], -x[1], x[2]],
    lambda x: [x[0], x[1], -x[2]],
    lambda x: [-x[0], -x[1], x[2]],
    lambda x: [x[0], -x[1], -x[2]],
    lambda x: [-x[0], x[1], -x[2]],
    lambda x: [-x[0], -x[1], -x[2]],
]

def rotate(coordinate, rot_num):
    queue = deque(coordinate)
    queue.rotate(rot_num)
    return list(queue)

cache
def all_possible_orientation_values():
    """
    returns simply a list between [0,0] and [7,2]
    """
    lst = []
    for i in range(8):
        for j in range(3):
            lst.append([i, j])
    return lst

def transform(neg, rot, coord):
    """
    rotates coordinate by a negation and rotation value
    negation is when any of the axis get negated eg (-x,y,z)
    rotation is when the axis switch eg: (y,z,x)
    """
    rotated = rotate(coord, rot)
    negatived = negative_orientations[neg](rotated)
    return negatived

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

    for orientation_method_data in all_possible_orientation_values():
        neg_orient_val, rot_orient_val = orientation_method_data

        # all the beacon coordinates in this specefic orientation
        beacon_trans = [transform(neg_orient_val, rot_orient_val, beacon) for beacon in beacon_orig_proc] 

        # the final beacon sets of this orientation to be filled
        main_beacons_proc = []
        for main_beacon in beacon_trans:
            relative_beacons = [find_relative(main_beacon, second_beacon) for second_beacon in beacon_trans]
            main_beacons_proc.append(relative_beacons)

        # appends the way the scanner was rotated for this, the list of beacon sets(each containing relative beacons to one beacon) and all beacons in this orientation
        orientations.append([orientation_method_data, main_beacons_proc, beacon_trans])
    scanners.append(orientations)

dump(scanners, open(f'data/parsed_{inp_type}.json', 'w'))