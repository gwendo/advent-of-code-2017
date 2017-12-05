
def current_instruction(param):
    return param.split(None).index(filter(lambda x: x.startswith("("), param.split(None)))
    