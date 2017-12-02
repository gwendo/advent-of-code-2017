from itertools import tee
from itertools import izip
from itertools import islice
from itertools import chain
from collections import deque

def return_if_equal(tup):
    if tup[0] == tup[1]:
        return int(tup[0])
    return 0

def pairwise(iterable, offSet):
    head = islice(iterable, 0, offSet)
    tail = islice(iterable, offSet, None)
    return izip(iterable, chain(tail, head))

def circle_sum(my_input, offSet):
    return sum(map(return_if_equal, pairwise(my_input, offSet))) 

def circle_sum_next(my_input):
    return circle_sum(my_input, 1)

def circle_sum_half(my_input):
    return circle_sum(my_input, len(my_input)/2)
