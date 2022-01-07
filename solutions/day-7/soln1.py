positions = open('data.txt', 'r').read().split(',')

positions = [int(pos) for pos in positions]

minenergy = float("inf")
for i in range(0, len(positions)):
    energy_consumed = 0
    for j in positions:
        energy_consumed += abs(j - i)
    if energy_consumed < minenergy:
        minenergy = energy_consumed

print(minenergy)