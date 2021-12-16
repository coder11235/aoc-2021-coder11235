data = open('data.txt', 'r').read()

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

for _ in range(10):
    tobeadded = [None]
    for i in range(len(template)-1):
        coll = tuple(template[i:i+2])
        if coll in rules:
            tobeadded.append(rules[coll])
        else:
            tobeadded.append(None)
    newarr = []
    for i in range(len(template)):
        if tobeadded[i] is not None:
            newarr.append(tobeadded[i])
        newarr.append(template[i])
    template = newarr

least = float("inf")
most = 0

for i in letters:
    ct = template.count(i)
    if ct < least and ct != 0:
        least = ct
    if ct > most:
        most = ct

print(most - least)