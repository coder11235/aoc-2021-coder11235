# NOT COMPLETED YET.NOT SURE WHAT TO DO


data = open('smallersmpl.txt', 'r').read().split('\n')

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

def withsmallfindbig(remaining: list, small, big):
    for i in range(len(remaining)):
        if checkifitisinside(small, remaining[i]):
            big = remaining[i]
            remaining.pop(i)
            break

def withbigfindsmall(remaining: list,big):
    for i in range(0, len(remaining)):
        if checkifitisinside(remaining[i], big):
            small = remaining[i]
            remaining.pop(i)
            return small

# accepts the input entry and returns an array with all digits sorted
def makevalues(input):
    orderarray: list = []
    # def
    a1 = []
    # def
    a7 = []
    # def
    a4 = []
    # def
    a8 = []
    a9 = []
    a0 = []
    a3 = []
    a6 = []
    a5 = []
    a2 = []

    remaining: list[list[str]] = []
    # predefined sizes : 1,4,7,8,
    for i in input:
        spl = list(i)
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

    withsmallfindbig(remaining, a4, a9)
    # a0 = withbigfindsmall(remaining, a8)
    withsmallfindbig(remaining, a1, a3)
    withsmallfindbig(remaining, sub(a8, a7), a6)
    # a5 = withbigfindsmall(remaining, a6)
    a2 = remaining
    orderarray = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
    return orderarray

data = list(map(parse, data))

for entry in data:
    input = entry[0]
    order = makevalues(input)
    print(order)
