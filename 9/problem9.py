def read_file(file_name):
    with open(file_name) as testfile:
        content = testfile.readlines()
    return content

def find_groups(param):
    cnt = 0
    pos = 0
    groupsum = 0
    garbage_cnt = 0
    char_list = list(param)
    ignore = False
    while pos < len(char_list):
        c = char_list[pos]
        if c == '!':
            pos += 1
        elif c == '<':
            if ignore:
                garbage_cnt += 1
            ignore = True
        elif c == '>':
            ignore = False
        else:
            if not ignore:
                if c == '{':
                    cnt += 1
                elif c == '}':
                    groupsum = groupsum + cnt
                    cnt -= 1
            else:
                garbage_cnt += 1
        pos += 1
    return groupsum, garbage_cnt
