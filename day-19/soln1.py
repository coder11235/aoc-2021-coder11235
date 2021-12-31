inp = open('sample.txt','r').read()
import itertools

def parse_scanner(scannertxt: str):
    lines = scannertxt.splitlines()
    parsedcoords = []
    for i in lines[1:]:
        parsedcoords.append(tuple([int(j) for j in i.split(',')]))
    return parsedcoords

scanners = [parse_scanner(i) for i in inp.split('\n\n')]
