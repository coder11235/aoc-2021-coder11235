data = open('data.txt', 'r').read().split('\n')

def parse(entry: str):
    input, output = entry.split(' | ')
    return [input.split(' '), output.split(' ')]

def checkifitisinside(small, big):
    for i in small:
        if not (i in big):
            return False
    return True

def sub(a, b):
    return [i for i in a if not i in b or b.remove(i)]

def withsmallfindbig(remaining: list, small):
    for i in range(len(remaining)):
        if checkifitisinside(small, remaining[i]):
            return remaining.pop(i)

def withbigfindsmall(remaining: list,big):
    for i in range(0, len(remaining)):
        if checkifitisinside(remaining[i], big):
            return remaining.pop(i)

# accepts the input entry and returns an array with all digits sorted
def makevalues(input):
    orderarray: list = []
    a1: set = {}
    a7: set = {}
    a4: set = {}
    a8: set = {}

    remaining: list[list[str]] = []
    # predefined sizes : 1,4,7,8,
    for i in input:
        spl = set(i)
        if len(i) == 2:
            a1 = spl
        elif len(i) == 3:
            a7 = spl
        elif len(i) == 4:
            a4 = spl
        elif len(i) == 7:
            a8 = spl
        else:
            remaining.append(spl)

    a9 = withsmallfindbig(remaining, a4)
    a6 = withsmallfindbig(remaining, sub(a8, a7.copy()))
    a5 = withbigfindsmall(remaining, a6)
    a3 = withbigfindsmall(remaining, a9)
    a0 = withsmallfindbig(remaining, a1)
    a2 = remaining[0]
    orderarray = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
    return orderarray

data = list(map(parse, data))

sum = 0

for entry in data:
    input, output = entry
    order = makevalues(input)

    calcedout = []
    for i in output:
        for j in range(len(order)):
            if set(i) == order[j]:
                calcedout.append(j)
                break
    num = ""
    for i in calcedout:
        num += str(i)
    sum += int(num)

print(sum)