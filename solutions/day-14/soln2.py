"""
well here is soln
first parse it and then convert it to a dict having the pairs and the number of them

loop
    create an empty dict for the updated values
    iterate through the pairs
    split the pair
    form 2 new one by looking up the table
    set or add the values to the new dict

when you are done
count the first number in all keys
incomplete soln over
--------------------
edit
get the last element of the template too because u only count the first of the pair
last += 1
complete soln over
"""

inp = open('data.txt', 'r').read()

def parse(inp: str):
    template, rls = inp.split('\n\n')
    last = template[-1:]
    tmpl = {}
    rules = {}
    for i in range(len(template) - 1):
        if (template[i], template[i+1]) in tmpl:
            tmpl[(template[i], template[i+1])] = tmpl[(template[i], template[i+1])] + 1
        else:
            tmpl[(template[i], template[i+1])] = 1
    for rl in rls.splitlines():
        t, i = rl.split(' -> ')
        rules[tuple(t)] = i
    return tmpl, rules, last

template, rules, last = parse(inp)

for c in range(40):
    newtmpl = {}
    for tmpl in template:
        (l, r) = tmpl
        cnt = template[tmpl]
        i = rules[(l, r)]
        ln = (l, i)
        rn = (i, r)
        if ln in newtmpl:
            newtmpl[ln] = newtmpl[ln] + cnt
        else:
            newtmpl[ln] = cnt
        if rn in newtmpl:
            newtmpl[rn] = newtmpl[rn] + cnt
        else:
            newtmpl[rn] = cnt
    template = newtmpl

def count(template: dict):
    counthash = {}
    for i in template:
        cnt = template[i]
        l = i[0]
        if l in counthash:
            counthash[l] = counthash[l] + cnt
        else:
            counthash[l] = cnt
    counthash[last] += 1
    return counthash

def sub(counthash: dict):
    lowest = float("inf")
    highest = 0
    for i in counthash:
        cnt = counthash[i]
        if cnt < lowest:
            lowest = cnt
        if cnt > highest:
            highest = cnt
    print(highest - lowest)

counthash = count(template)

sub(counthash)
