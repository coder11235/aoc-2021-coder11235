from functools import cache
from collections import deque
from json import dump

inp_type = "data"

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
    returns simple a list between [0,0] and [7,2]
    """
    lst = []
    for i in range(8):
        for j in range(3):
            lst.append([i, j])
    return lst

def transform(neg, rot, coord):
    rotated = rotate(coord, rot)
    negatived = negative_orientations[neg](rotated)
    return negatived

def find_relative(orig, second):
    """
    finds relative coordinate of second becon to orig beacon
    """
    return [s_axis_val - orig[s_axis_index] for s_axis_index, s_axis_val in enumerate(second)]

scanners = []

for scanner in data.split('\n\n'):
    beacon_strs = scanner.splitlines()[1:]
    beacon_orig_proc = [[int(axis) for axis in be.split(',')] for be in beacon_strs]
    orientations = []
    for orientation_method_data in all_possible_orientation_values():
        neg_orient_val, rot_orient_val = orientation_method_data
        beacon_trans = [transform(neg_orient_val, rot_orient_val, beacon) for beacon in beacon_orig_proc]
        main_beacons_proc = []
        for main_beacon in beacon_trans:
            relative_beacons = [find_relative(main_beacon, second_beacon) for second_beacon in beacon_trans]
            main_beacons_proc.append(relative_beacons)
        orientations.append([orientation_method_data, main_beacons_proc])
    scanners.append(orientations)

dump(scanners, open(f'data/parsed_{inp_type}.json', 'w'))