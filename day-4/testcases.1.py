from soln41 import *

print(checkforhorizontalwin([
    [False, True, False, False, False],
    [False, False, False, False, False],
    [True, True, True, True, True],
    [False, False, False, False, False],
    [False, False, False, False, False],]
))

print(checkforverticalwin([
    [True, True, True, True, True],
    [False, True, True, False, False],
    [True, False, False, True, True],
    [True, True, True, False, False],
    [True, True, True, False, False],]
))

markedarr = []
for i in range(0, 6):
    marked = [False]*5
    markedarr.append(marked)

checkoff(
[
['24', '22', '17', '11', '0'],
['8', '2', '23', '4', '24'],
['21', '9', '14', '16', '7'],
['6', '10', '3', '18', '5'],
['1', '12', '20', '15', '19']
],'22',markedarr)

print(markedarr)