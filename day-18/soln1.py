inp = open('sample.txt', 'r').read().splitlines()
import math

class Node:
    count = -1
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

    def reduce_num(self):
        Node.count += 1
        if not isinstance(self, int):
            if Node.count == 4:
                self.explode()
            elif isinstance(self.left, int) and self.left >= 10:
                newnode = Node()
                newnode.left = self.left//2
                newnode.right = math.ceil(self.left/2)
                newnode.parent = self
                self.left = newnode
            elif isinstance(self.right, int) and self.right >= 10:
                newnode = Node()
                newnode.left = self.right//2
                newnode.right = math.ceil(self.right/2)
                newnode.parent = self
                self.right = newnode

        if not isinstance(self.left, int):
            self.left.reduce_num()
        if not isinstance(self.right, int):
            self.right.reduce_num()
        Node.count -= 1

    def explode(self):
        right = self.right
        left= self.left

        # add to rightmode element
        right_par = self.get_right_par()
        if right_par is not None:
            if isinstance(right_par.right, int):
                right_par.right += right
            else:
                cp = right_par.right.get_leftest_child_parent()
                cp.left += right

        left_par = self.get_left_par()
        if left_par is not None:
            if isinstance(left_par.left, int):
                left_par.left += left
            else:
                cp = left_par.left.get_rightest_child_parent()
                cp.right += left

        if self.parent.right == self:
            self.parent.right = 0
        else:
            self.parent.left = 0

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
    first.reduce_num()

for i in inp:
    node = propparse(i)
    for _ in range(40):
        node.reduce_num()
        first.reduce_num()
    first = add(first, node)
    for _ in range(40):
        node.reduce_num()
        first.reduce_num()

first.debugprint()