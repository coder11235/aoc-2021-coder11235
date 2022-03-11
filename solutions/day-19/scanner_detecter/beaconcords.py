import json


scanners = json.load(open('parsed_scanners.json', 'r'))

overlapping_scanners = []

def compare_lists(a, b):
    count = 0
    for ba in a:
        for bb in b:
            if ba == bb:
                count += 1
    return count >= 12

def compare_beacons(a, b):
    """
    checks if two beacon sets are in the same area
    """
    for relative_beacons_in_a in a:
        for relative_beacons_in_b in b:
            if compare_lists(relative_beacons_in_a, relative_beacons_in_b):
                return True
    return False

def compare_scanners(si, sj):
    for orientationi, beaconsi in si:
        for orientationj, beaconsj in sj:
            if compare_beacons(beaconsi, beaconsj):
                return orientationi, orientationj
    
for indexi, si in enumerate(scanners):
    print(indexi)
    for indexj , sj in enumerate(scanners):
        if indexi == indexj: continue
        comp_res = compare_scanners(si, sj)
        if comp_res is not None:
            overlapping_scanners.append((indexi, indexj, comp_res))

print(overlapping_scanners)