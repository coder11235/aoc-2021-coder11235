# HEAVILY UNOPTIMISED SOLUTION


file = open('data.txt', 'r')
# file = open('sample.txt', 'r')
data = file.read()
data = data.split('\n')

# im gonna try to do some wonky recursion in here
def filteraction(listtp: list, max: bool, index: int = 0):
    num0 = 0
    num1 = 0
    # base case
    if len(listtp) == 1:
        return listtp

    for i in listtp:
        if i[index] == '0':
            num0 += 1
        else:
            num1 += 1
    more0s = num0 > num1 if max else num1 >= num0
    if num0 == 0 or num1 == 0:
        return filteraction(listtp, max, index+1)
    nl = []
    for i in range(0, len(listtp)):
        if more0s:
            if listtp[i][index] == '0':
                nl.append(listtp[i])
        else:
            if listtp[i][index] == '1':
                nl.append(listtp[i])
    return filteraction(nl, max, index+1)

ogerating = filteraction(data.copy(), True)[0]
cogerating = filteraction(data.copy(), False)[0]

print(
    int(ogerating, 2)*
    int(cogerating, 2)
)