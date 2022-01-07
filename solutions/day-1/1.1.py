file = open('data.txt', 'r')

data = file.read()
data = data.split('\n')

count  = 0
for i in range(1, len(data)):
    if int(data[i - 1]) < int(data[i]):
        count += 1

print(count)