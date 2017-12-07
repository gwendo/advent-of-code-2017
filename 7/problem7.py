

class Prog:
    def __init__(self, weight, children):
       self.c = children
       self.w = weight
    
def parse_prog(param):
    split = param.split(None)
    p = Prog(int(param[1].trim("()"))), param[0])
    if len(split) > 2:
        p.children = split[3].split(",")
    return p

def find_base(file_name):
    with open(file_name) as testfile:
        content = testfile.readlines()
    progs = map(parse_prog, content)
    return filter(l)
    