file = open('data.txt', 'r')
# file = open('sample.txt', 'r')
data = file.read()
data = data.split('\n')

def getdigit(data: list, index: int, max: bool):
    num0 = 0
    num1 = 0
    for i in data:
        if i[index] == '0':
            num0 += 1
        else:
            num1 += 1
    if max:
        return '0' if num0 > num1 else '1'
    else:
        return '0' if num0 < num1 else '1'

gammarate = ''
epsilonrate = ''

for i in range(0,len(data[0])):
    gammarate += getdigit(data, i, True)
    epsilonrate += getdigit(data, i, False)

print(int(epsilonrate, 2) * int(gammarate, 2))