fishes = open('data.txt', 'r').read().split(',')

fishes = [int(fish) for fish in fishes]

for day in range(0, 80):
    newfishes = 0
    for i in range(0, len(fishes)):
        fish = fishes[i]
        fish -= 1
        fishes[i] = fish
        if fish < 0:
            fishes[i] = 6
            newfishes += 1
    for i in range(0, newfishes):
        fishes.append(8)
    print(day)

print(len(fishes))