inp = open('sample.txt','r').read()
import itertools

def parse_scanner(scannertxt: str):
    lines = scannertxt.splitlines()
    parsedcoords = []
    for i in lines[1:]:
        parsedcoords.append(tuple([int(j) for j in i.split(',')]))
    return parsedcoords

scanners = [parse_scanner(i) for i in inp.split('\n\n')]

scanners = [scanners[0]]

rots = [
    lambda a: (a[0], a[1], a[2]),
    lambda a: (a[2], a[0], a[1]),
    lambda a: (a[1], a[2], a[0]),
]

negtrans = [
    lambda a: (-a[0], a[1], a[2]),
    lambda a: (a[0], -a[1], a[2]),
    lambda a: (a[0], a[1], -a[2]),
    lambda a: (-a[0], -a[1], a[2]),
    lambda a: (a[0], -a[1], -a[2]),
    lambda a: (-a[0], a[1], -a[2]),
    lambda a: (-a[0], -a[1], -a[2]),
    lambda a: (a[0], a[1], a[2]),
]