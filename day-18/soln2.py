inp = open('data.txt', 'r').read().splitlines()

import math
from termcolor import colored

class Node:
    count = 0
    debugcnt = -1
    bpr: 'Node' = None
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

    def perform_explode(self):
        # print()
        # print(Node.count)
        # Node.bpr.debugprint()
        Node.count += 1
        # self.debugprint()
        if Node.count == 4:
            if not isinstance(self.left, int):
                self.left.explode()
                return True
            if not isinstance(self.right, int):
                self.right.explode()
                return True
        if not isinstance(self.left, int):
            if self.left.perform_explode():
                return True
        if not isinstance(self.right, int):
            if self.right.perform_explode():
                return True
        Node.count -= 1
        return False

    def perform_split(self):
        # Node.bpr.debugprint()
        if isinstance(self.left, int):
            if self.left >= 10:
                newnode = Node()
                newnode.left = self.left//2
                newnode.right = math.ceil(self.left/2)
                newnode.parent = self
                self.left = newnode
                return True
        else:
            if self.left.perform_split():
                return True
        if isinstance(self.right, int):
            if self.right >= 10:
                newnode = Node()
                newnode.left = self.right//2
                newnode.right = math.ceil(self.right/2)
                newnode.parent = self
                self.right = newnode
                return True
        else:
            if self.right.perform_split():
                return True
        

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

    def retclr():
        if Node.debugcnt == 0:
            return 'cyan'
        elif Node.debugcnt == 1:
            return 'blue'
        elif Node.debugcnt == 2:
            return 'yellow'
        elif Node.debugcnt == 3:
            return 'red'
        elif Node.debugcnt ==4:
            return 'white'
        else:
            return 'red'
            
    def debugprint(self, pr = False):
        Node.debugcnt += 1
        print(colored('[', Node.retclr()), end='')
        if isinstance(self.left, int):
            print(self.left,end='')
        else:
            self.left.debugprint(True)
        print(',', end='')
        if isinstance(self.right, int):
            print(self.right, end='')
        else:
            self.right.debugprint(True)
        print(colored(']',Node.retclr()), end='')
        if not pr:
            print()
        Node.debugcnt -= 1

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
    Node.bpr = parent
    return parent

def check_magnitude(node: Node):
    left = 0
    right = 0
    if isinstance(node.left, int):
        left = node.left
    else:
        left = check_magnitude(node.left)
    if isinstance(node.right, int):
        right = node.right
    else:
        right = check_magnitude(node.right)
    return 3*left + 2*right


maxmag = 0
for i in inp:
    for j in inp:
        if i != j:
            first = propparse(i)
            second = propparse(j)
            sm = add(first, second)
            Node.bpr = sm
            for _ in range(500):
                if not sm.perform_explode():
                    sm.perform_split()
                Node.count = 0
            mag = check_magnitude(sm)
            if mag > maxmag:
                maxmag = mag

print(maxmag)