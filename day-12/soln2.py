data = open('sample.txt', 'r').read()

from termcolor import colored

class Caves:
    caves: list['Cave'] = []
    pathsofar: list = []
    doubledone: str = None

    def search(self, name: str):
        for i in self.caves:
            if i.name == name:
                return i

    def append(self, cave):
        self.caves.append(cave)

def rmv(path: list, cavemap: Caves):
    cavename = path.pop()
    print(colored(cavename, 'green'))
    cave = cavemap.search(cavename)
    if cave.name == cavemap.doubledone:
        cavemap.doubledone = None
    else:
        cave.visited = False

class Cave:
    isbig: bool
    connections: list['Cave']
    name: str
    visited: bool
    hasbeendoubled: bool = False

    def __init__(self, name: str):
        self.name = name
        self.connections = []
        if name != 'end':
            self.isbig = name.isupper()
        else:
            self.isbig = True
        self.visited = False

    def __str__(self) -> str:
        return self.name
        
    def dfs(self, path: list, cavemap: 'Caves'):
        print(colored(self, 'red'))
        if self.name != 'start':
            if cavemap.doubledone is None:
                if not self.isbig:
                    cavemap.doubledone = self.name
                else:
                    self.visited = False
            else:
                self.visited = True
        else:
            self.visited = True
        path.append(self.name)
        print(path)

        if self.name == 'end':
            cavemap.pathsofar.append(path.copy())
            rmv(path, cavemap)
            return True

        totr = self.connections.copy()
        totr = list(filter(lambda cv: (not cv.visited or cv.isbig) and cv.name != 'start', totr))
        if len(totr) == 0:
            rmv(path, cavemap)
            return False

        for cave in totr:
            cave.dfs(path, cavemap)
        rmv(path, cavemap)

cavemap = Caves()

for i in data.splitlines():
    lst = i.split('-')
    for cv in lst:
        if cavemap.search(cv) is None:
            cave = Cave(cv)
            cavemap.caves.append(cave)

for i in data.splitlines():
    l, r = i.split('-')
    l = cavemap.search(l)
    r = cavemap.search(r)
    l.connections.append(r)
    r.connections.append(l)

start = cavemap.search('start')
path = []
start.dfs(path, cavemap)
for i in cavemap.pathsofar:
    print(i)
print(len(cavemap.pathsofar))