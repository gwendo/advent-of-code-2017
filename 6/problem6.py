
def redistribute_twice(param):
    step, banks = find_first_duplicate(map(lambda x: int(x), param.split(None)))
    step, banks = find_first_duplicate(banks)
    return step


def find_first_duplicate(banks):
    seen_configs = []
    step = 0
    while banks not in seen_configs:
        first = banks.index(reduce(lambda x, y: x if x > y else y, banks))
        seen_configs.append(list(banks))
        banks = spread(first, banks)
        step += 1
    return step, banks

def spread(first, banks):
    count = banks[first]
    banks[first] = 0
    while count > 0:
        first += 1
        count -= 1 
        if first >= len(banks):
            first = 0
        banks[first] = banks[first]+1
    return banks
        