data = open('sample.txt').read()

def parse(data: str):
    data = data.split(': ')[1]
    coords = data.split(', ')
    target = []
    for i in coords:
        i = i.split('=')[1]
        target.append(tuple(i.split('..')))
    return target

target = parse(data)