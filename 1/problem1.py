from itertools import tee
from itertools import izip
from collections import deque

def returnIfEqual(tup):
    if tup[0] == tup[1]:
        return tup[0]
    return 0

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def circleSum(iter):
    q = deque(iter)
    return sum(map(returnIfEqual, pairwise(map(int, iter)))) + returnIfEqual((int(q.pop()), int(q.popleft())))
