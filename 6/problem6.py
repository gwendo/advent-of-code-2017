

def redistribute(param):
    banks = map(lambda x: int(x), param.split(None))
    seen_configs = []
    step = 0
    print banks
    while True:
        if banks in seen_configs:
            break
        first = banks.index(reduce(lambda x, y: x if x > y else y, banks))
        banks = spread(first, banks)
        seen_configs.append(banks)
        step += 1
    return step    

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
        