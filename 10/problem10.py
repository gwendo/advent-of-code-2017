
from itertools import chain
from itertools import repeat
from operator import xor

def twist(size, params):

    skip_size = 0
    curr_pos = 0
    my_list = range(size)
    for length in map(lambda x: int(x), params.split(",")):
        if curr_pos + length < size:
            first = my_list[0: curr_pos]
            rev = my_list[curr_pos : curr_pos + length]
            rev.reverse()
            rest = my_list[curr_pos + length:]
            my_list = first + rev + rest
        else:
            first = my_list[curr_pos:]
            second = my_list[0 : (curr_pos + length) % size]
            rest = my_list[(curr_pos + length) % size: curr_pos]
            rev = first + second
            rev.reverse()
            my_list = rev[len(first):] + rest + rev[:len(first)] 

        curr_pos = (curr_pos + length + skip_size) % size 
        skip_size += 1
    return my_list[0] * my_list[1]





def twist2(size, params):

    curr_pos = 0
    my_list = range(size)
    skip_size = 0

    params = map(lambda x: ord(x), params)
    params = params + [17, 31, 73, 47, 23]
    
    ix = 64
    my_result = []
    while ix > 0:
        for length in params:
            if curr_pos + length < size:
                first = my_list[0: curr_pos]
                rev = my_list[curr_pos : curr_pos + length]
                rev.reverse()
                rest = my_list[curr_pos + length:]
                my_list = first + rev + rest
            else:
                first = my_list[curr_pos:]
                second = my_list[0 : (curr_pos + length) % size]
                rest = my_list[(curr_pos + length) % size: curr_pos]
                rev = first + second
                rev.reverse()
                my_list = rev[len(first):] + rest + rev[:len(first)] 

            curr_pos = (curr_pos + length + skip_size) % size
            skip_size += 1
        ix -= 1

    for sub_list in list(chunks(my_list, 16)):
        nr = reduce(xor, sub_list)
        my_result.append(nr)

    return "".join(map(lambda x: format(x, 'x').zfill(2), my_result))

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]