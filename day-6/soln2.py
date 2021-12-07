fishes = open('data.txt', 'r').read().split(',')

fishes = [int(fish) for fish in fishes]

def initialprocess(fishes: list[int]):
    newlist = [0]*9
    for i in fishes:
        newlist[i] += 1
    return newlist

fishes = initialprocess(fishes)

for i in range(0, 256):
    newfishes = fishes.pop(0)
    fishes[6] += newfishes
    fishes.append(newfishes)

count = 0
for i in fishes:
    count += i
print(count)