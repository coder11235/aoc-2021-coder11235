file = open('data.txt', 'r')
data = file.read()
data = data.split('\n')
horizontal = 0
depth = 0
for i in data :
    cmd, num = i.split(' ')
    num = int(num)
    if cmd == "up":
        depth -= num
    elif cmd == "down":
        depth += num
    else:
        horizontal += num

print(horizontal , depth)