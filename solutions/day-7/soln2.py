positions = open('data.txt', 'r').read().split(',')

positions = [int(pos) for pos in positions]

minenergy = float("inf")
for i in range(0, len(positions)):
    total_energy_consumed = 0
    for crab in positions:
        diff = abs(crab - i)
        total_fuel_by_crab = 0
        for k in range(1, diff+ 1):
            total_fuel_by_crab += k
        total_energy_consumed += total_fuel_by_crab
    if total_energy_consumed < minenergy:
        minenergy = total_energy_consumed

print(minenergy)