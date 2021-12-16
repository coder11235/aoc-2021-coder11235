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