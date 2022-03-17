import json

# from .parser import negative_functions, rotation_functions

data = json.loads(open('../data/parsed2.json').read())

beacon_map = {0: []}

print(data)
cset = set()
for i in data:
    c,_ = i
    a, b = c
    cset.add(a)
    cset.add(b)

for i in range(30):
    if i not in cset:
        print(i)
exit()

while len(data) > 0:
    new = []
    print(data)
    print(beacon_map)
    for conn in data:
        c, orientation = conn
        l, r = c
        if l in beacon_map and r in beacon_map:
            pass
        elif l in beacon_map:
            lo = beacon_map[l]
            beacon_map[r] = lo + [(1, orientation)]
        elif r in beacon_map:
            ro = beacon_map[r]
            beacon_map[l] = ro + [(-1, orientation)]
        else:
            new.append(conn)
    data = new

print(beacon_map)