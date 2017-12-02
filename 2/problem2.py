from itertools import permutations

def get_int_list(my_input):
    return map(int, my_input.split(None))

def get_evenly_divided_sum(my_input):
    return sum(map(divide, permutations(get_int_list(my_input), 2)))

def divide(tup):
    return tup[0] / tup[1] if tup[0] % tup[1] == 0 else 0


def get_diff(my_input):
    int_list = get_int_list(my_input)
    lowest = reduce(lambda x, y: x if x < y else y, int_list)
    highest = reduce(lambda x, y: x if x > y else y, int_list)
    return highest - lowest

def calc_check_sum(fileName):
    with open(fileName) as testfile:
        content = testfile.readlines()
    return sum(map(get_diff,content))

def calc_even_sum(fileName):
    with open(fileName) as testfile:
        content = testfile.readlines()
    return sum(map(get_evenly_divided_sum, content))
