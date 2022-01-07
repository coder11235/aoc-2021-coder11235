file = open('data.txt', 'r')

data = file.read()
data = data.split('\n')
data = [int(i) for i in data]

count = 0
for i in range(3, len(data)):
    if data[i] > data[i - 3]:
        count += 1

print(count)