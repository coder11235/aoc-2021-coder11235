from enum import Enum, auto
from xml.etree.ElementPath import ops


inp = open('sample.txt').read()

"""
first parse all lines
get the coordinates of the rect in ((x1, x2),(y1, y2),(z1, z2))
the others = 
(x1,y1,z1),
(x2,y1,z1),
(x1,y2,z1),
(x1,y1,z2),
(x2,y2,z1),
(x1,y2,z2),
(x2,y1,z2),
(x2,y2,z2)
if the cube is off-
    create a new list of rects
    run through the list of on rectangles b of cubes and
        if the b is completely inside, do nothing
        if it is completely outside, return the full thing
        if it is intersecting
        perform a b-a subtraction, return the set of cubes
        append whateve u got to the new list
"""

oncubes = []

class CheckContact(Enum):
    INDEPENDENT = auto()
    INTERSECTS = auto()
    ON_IN_OPS = auto()
    OPS_IN_ON = auto()
    SAME = auto()

def remove_inner(big, small):
    pass


def check_contact(on: tuple[tuple], ops: tuple[tuple]):
    """
    accepts a block coordinates of onned cubes and a current operation
    returns a CheckContact having status managing the contact status between the cubes
    """
    if on == ops:
        return CheckContact.SAME
    # having all 3 axis states
    states = []
    #assign the states
    for i in range(3):
        con = on[i]
        cops = ops[i]
        if (con[0] < cops[0]) and (con[1] > cops[1]):
            states.append(CheckContact.OPS_IN_ON)
        elif (con[0] > cops[0]) and (con[1] < cops[1]):
            states.append(CheckContact.ON_IN_OPS)
        elif ((con[0]-cops[0]) / (con[1]-cops[1]) >= 0):
            # if any axes are independent then it is independednt on total
            return CheckContact.INDEPENDENT
        else:
            states.append(CheckContact.INTERSECTS)
    # check for total containment
    if states.count(states[0]) == len(states):
        return states[0]
    # otherwise it intersects so return the list of states
    return states

def off_work(ondims, dims):
    newlist = []
    for ondim in ondims:
        cnt = check_contact(ondim, ops)
        if not cnt is list:
            if cnt == CheckContact.ON_IN_OPS or cnt == cnt.SAME:
                pass
            elif cnt == CheckContact.INDEPENDENT:
                newlist.append(ondim)
            


def parse(inp: str, oncubes: set):
    """
    accepts a line of on x=10..12,y=10..12,z=10..12 format and parses it
    """
    for ln in inp.splitlines():
        state, dims = ln.split(' ')
        state = True if state == 'on' else False
        current_op_dim = []
        for i in dims.split(','):
            _, i = i.split('=')
            current_op_dim.append(tuple(int(j) for j in i.split('..')))
        print(current_op_dim)
        if state:
            pass
        else:
            off_work(oncubes, current_op_dim)


parse(inp, oncubes)