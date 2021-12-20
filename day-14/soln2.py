data = open('sample.txt', 'r').read()

def parse(data: str):
    template, rules = data.split('\n\n')
    letters = set(template)
    rules = rules.splitlines()
    hashrl = {}
    for i in rules:
        ln = i.split(' -> ')
        hashrl.update({(ln[0][0], ln[0][1]): ln[1]})
        letters.add(ln[1])
    return list(template), hashrl, letters

template, rules, letters = parse(data)

tplcnt = {}

for i in range(len(template) - 1):
    s = (template[i], template[i+1])
    if s in tplcnt:
        tplcnt.update({s: tplcnt[s] + 1})
    else:
        tplcnt.update({s: 1})

for _ in range(10):
    tmp = {}
    for key in tplcnt:
        m = rules[key]
        l, r = key
        lef = (l, m)
        rig = (m, r)
        if not lef in tmp:
            tmp.update({lef: 0})
        if not rig in tmp:
            tmp.update({rig: 0})
        tmp.update({lef: tmp[lef] + 1})
        tmp.update({rig: tmp[rig] + 1})
    for key in tmp:
        if not key in tplcnt:
            tplcnt.update({key: 0})
        tplcnt.update({key: tmp[key] + tplcnt[key]})

ltcnt = {}

for i in tplcnt:
    count = tplcnt[i]
    l = i[0]
    ltcnt.update({l: count})

print(ltcnt)