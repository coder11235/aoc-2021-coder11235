from termcolor import colored


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
        if not self.isbig:
            if cavemap.ctwice == "" and cavemap.twiced.count(self.name) == 0 and self.name != 'start':
                print(colored(cavemap.twiced, 'green'))
                print(self)
                print(cavemap.ctwice)
                cavemap.ctwice = self.name
                cavemap.twiced.append(self.name)
            else:
                self.visited = True
        path.append(self.name)

        print(path)
        if self.name == 'end':
            cavemap.pathsofar.append(path.copy())
            print(colored(path, 'red'))
            cavemap.search(path.pop()).visited = False
            return True

        totr = self.connections.copy()
        totr = list(filter(lambda cv: not cv.visited, totr))

        for cave in totr:
            cave.dfs(path, cavemap)
        if cavemap.ctwice == self.name and path.count(self.name) == 1:
            print(colored(path, 'blue'))
            cavemap.ctwice = ""
            cavemap.twiced.append(self.name)
            self.visited = True
            for cave in totr:
                cave.dfs(path, cavemap)
        cavemap.search(path.pop()).visited = False

class Caves:
    caves: list[Cave] = []
    pathsofar: list = []
    twiced: list[str] = []
    ctwice = ""
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
# for i in cavemap.pathsofar:
#     print(i)
print(len(cavemap.pathsofar))