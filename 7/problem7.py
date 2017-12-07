from collections import Counter
from itertools import izip

class Prog:
    def __init__(self, name, weight):
        self.n = name
        self.p = None
        self.w = weight
        self.c = []

    def add_child(self, child):
        self.c.append(child)

    def add_parent(self, parent):
        self.p = parent

    def __repr__(self):
        return "(n: %s )" % (self.n)


def parse_prog(param):
    split = param.split(None)
    p = Prog(split[0], int(split[1].strip("()")))
    if len(split) > 2:
        map(p.add_child, map(lambda x: x.strip(","), split[3:]))
    return p


def set_parent(p, progs):
    children = filter(lambda pro: pro.n in p.c, progs)
    p.c = children
    for child in children:
        child.p = p

def is_unbalanced(p):
    return len(Counter(map(sum_prog, p.c))) > 1


def find_weight(p):
    sums = map(sum_prog, p.c)
    soloSum = filter(lambda x: x[1] == 1, Counter(sums).items())
    diff = sums[0] - sums[sums.index(soloSum[0][0])]
    return p.c[sums.index(soloSum[0][0])].w + diff

def find_unbalanced(progs):
    unbalanced = filter(is_unbalanced, progs)
    return find_weight(unbalanced[0])


def sum_prog(p):
    summa = p.w + sum(map( lambda x: x.w if len(x.c) == 0 else sum_prog(x), p.c))
    return summa

def find_progs(file_name):
    with open(file_name) as testfile:
        content = testfile.readlines()
    progs = map(parse_prog, content)
    for prog in progs:
        set_parent(prog, progs)
    return progs

def find_base(file_name):
    progs = find_progs(file_name)

    base = filter(lambda p: p.p == None, progs)[0]
    return base

