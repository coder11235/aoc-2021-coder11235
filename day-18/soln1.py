inp = open('sample.txt', 'r').read().splitlines()
import math

class Node:
    def __init__(self, node: 'Node' = None):
        self.parent = node
        self.left = None
        self.right = None

    def set(self, val):
        if self.left is None:
            self.left = val
        else:
            self.right = val

    def get_right_par(self):
        """
        returns:
        the node which has a right element which is not a part of the start node
        or None if the start node is the rightmost node
        """
        if self.parent is None:
            return None
        if self.parent.right == self:
            return self.parent.get_right_par()
        else:
            return self.parent

    def get_left_par(self):
        if self.parent is None:
            return None
        if self.parent.left == self:
            return self.parent.get_left_par()
        else:
            return self.parent

    def get_leftest_child_parent(self):
        if isinstance(self.left, int):
            return self
        else:
            return self.left.get_leftest_child_parent()

    def get_rightest_child_parent(self):
        if isinstance(self.right, int):
            return self
        else:
            return self.right.get_rightest_child_parent()

    def __str__(self) -> str:
        vals = self.__dict__.copy()
        vals['idhash'] = hex(id(self))
        return str(vals)

    def debugprint(self, pr = False):
        print('[', end='')
        if isinstance(self.left, int):
            print(self.left,end='')
        else:
            self.left.debugprint(True)
        print(',', end='')
        if isinstance(self.right, int):
            print(self.right, end='')
        else:
            self.right.debugprint(True)
        print(']', end='')
        if not pr:
            print()

def parse(line: str):
    current_node = Node()
    for i in line:
        if i == '[':
            current_node = Node(current_node)
        elif i.isdigit():
            current_node.set(int(i))
        elif i == ']':
            finished = current_node
            current_node = current_node.parent
            current_node.set(finished)
    return current_node

def explode(node: Node):
    right = node.right
    left= node.left

    # add to rightmode element
    right_par = node.get_right_par()
    if right_par is not None:
        if isinstance(right_par.right, int):
            right_par.right += right
        else:
            cp = right_par.right.get_leftest_child_parent()
            cp.left += right

    left_par = node.get_left_par()
    if left_par is not None:
        if isinstance(left_par.left, int):
            left_par.left += left
        else:
            cp = left_par.left.get_rightest_child_parent()
            cp.right += left

    if node.parent.right == node:
        node.parent.right = 0
    else:
        node.parent.left = 0

count = -1
def reduce_num(node: Node):
    global count
    count += 1
    if not isinstance(node, int):
        if count == 4:
            explode(node)
        elif isinstance(node.left, int) and node.left >= 10:
            newnode = Node()
            newnode.left = node.left//2
            newnode.right = math.ceil(node.left/2)
            newnode.parent = node
            node.left = newnode
        elif isinstance(node.right, int) and node.right >= 10:
            newnode = Node()
            newnode.left = node.right//2
            newnode.right = math.ceil(node.right/2)
            newnode.parent = node
            node.right = newnode

    if not isinstance(node.left, int):
        reduce_num(node.left)
    if not isinstance(node.right, int):
        reduce_num(node.right)
    count -= 1

def propparse(line: str):
    node: Node = parse(line)
    node = node.left
    node.parent = None
    return node

def add(node1: Node, node2: Node):
    parent = Node()
    parent.left = node1
    parent.right = node2
    node1.parent = parent
    node2.parent = parent
    return parent

first = inp.pop(0)
first = propparse(first)
for _ in range(5):
    reduce_num(first)

for i in inp:
    node = propparse(i)
    for _ in range(40):
        reduce_num(node)
        reduce_num(first)
    first = add(first, node)
    for _ in range(40):
        reduce_num(node)
        reduce_num(first)

first.debugprint()