file = open('data.txt', 'r')

data = file.read()
data = data.split('\n')
data = [int(i) for i in data]

count = 0
i = 3
while i < len(data):
    if data[i] > data[i - 3]:
        count += 1
    i += 1

print(count)