data = open('sample.txt', 'r').read()

from termcolor import colored

class Cave:
    isbig: bool
    connections: list['Cave']
    name: str
    visited: bool
    hasbeentwiced: bool = False
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
        mustredocuztwiced = False
        if self.name == 'start' and len(path) != 0:
            return
        if not self.isbig:
            if (not cavemap.smallcavedoubledalready) and (not self.hasbeentwiced):
                cavemap.smallcavedoubledalready = True
                self.hasbeentwiced = True
                mustredocuztwiced = True
            else:
                self.visited = True
        path.append(self.name)

        if self.name == 'end':
            cavemap.pathsofar.append(path.copy())
            print(colored(path, 'red'))
            cavemap.search(path.pop()).visited = False
            return True
        else:
            print(path)

        totr = self.connections.copy()
        totr = list(filter(lambda cv: not cv.visited, totr))

        for cave in totr:
            cave.dfs(path, cavemap)

        if mustredocuztwiced:
            print(colored(f"second timind{self}", 'blue'))
            print(colored(path, 'green'))
            cavemap.smallcavedoubledalready = False
            self.hasbeentwiced = True
            for cave in totr:
                cave.dfs(path, cavemap)

        cavemap.search(path.pop()).visited = False

class Caves:
    caves: list[Cave] = []
    pathsofar: list = []
    smallcavedoubledalready: bool = False
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
for i in cavemap.pathsofar:
    print(i)
print(len(cavemap.pathsofar))