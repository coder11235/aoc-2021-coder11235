file = open('data.txt', 'r')

data = file.read()
data = data.split('\n')

count  = 0
i = 1
while i < len(data):
    if int(data[i - 1]) < int(data[i]):
        count += 1
    i += 1

print(count)