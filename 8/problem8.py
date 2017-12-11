import operator
from collections import defaultdict 

def find_largest_input(file_name):
    register = defaultdict(lambda: 0)
    with open(file_name) as testfile:
        content = testfile.readlines()
    max_value_in_process = 0
    for instr in content:
        i = instr.split(None)
        if operators[i[5]](register[i[4]], int(i[6])):
            val = operators[i[1]](register[i[0]], int(i[2]))
            max_value_in_process = val if val > max_value_in_process else max_value_in_process
            register[i[0]] = val
    return max(register.values()), max_value_in_process


operators = {
    '==' : operator.eq,
    '<' : operator.lt,
    '>' : operator.gt,
    '>=' : operator.ge,
    '<=' : operator.le,
    '!=' : operator.ne,
    'inc' : operator.add,
    'dec' : operator.sub
}
