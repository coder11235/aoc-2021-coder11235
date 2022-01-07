data = open('sample.txt', 'r').read()

class Cave:
    isbig: bool
    connections: list['Cave']
    name: str
    visited: bool

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
        tmp = False
        if not self.isbig:
            if not cavemap.currentsmallcave and self.name != 'start':
                cavemap.currentsmallcave = True
                tmp = True
            else:
                self.visited = True
        path.append(self.name)

        if self.name == 'end':
            if not path in cavemap.pathsofar:
                cavemap.pathsofar.append(path.copy())
            cavemap.search(path.pop()).visited = False
            return True

        totr = self.connections.copy()
        totr = list(filter(lambda cv: not cv.visited, totr))

        for cave in totr:
            cave.dfs(path, cavemap)
        if tmp:
            cavemap.currentsmallcave = False
            self.visited = True
            for cave in totr:
                cave.dfs(path, cavemap)
        cavemap.search(path.pop()).visited = False

class Caves:
    caves: list[Cave] = []
    pathsofar = []
    currentsmallcave = False

    def search(self, name: str):
        for i in self.caves:
            if i.name == name:
                return i

    def append(self, cave):
        self.caves.append(cave)

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
print(len(cavemap.pathsofar))