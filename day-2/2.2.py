file = open('data.txt', 'r')
# file = open('sample.txt', 'r')
data = file.read()
data = data.split('\n')

horizontal = 0
depth = 0
aim = 0

for i in data :
    cmd, num = i.split(' ')
    num = int(num)
    if cmd == "up":
        aim -= num
    elif cmd == "down":
        aim += num
    else:
        horizontal += num
        depth += aim * num

print(horizontal * depth)