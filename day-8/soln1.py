data = open('data.txt', 'r').read().split('\n')

data = [list(d.split(' | ')) for d in data]

total = 0
for i in data:
    values = i[1].split(' ')
    for i in values:
        le = len(i)
        if le == 3 or le == 2 or le == 4 or le == 7:
            total += 1

print(total)