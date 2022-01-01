inp = open('sample.txt', 'r').read()

def parse(inp: str):
    alg, img = inp.split('\n\n')
    alg = [True if i == '#' else False for i in alg]
    imgarr = [[True if i == '#' else False for i in ln] for ln in img.splitlines()]
    return alg, imgarr

alg, inpimg = parse(inp)