def jump_from(instruction_pointer, clean_list):
    curr = clean_list[instruction_pointer]
    clean_list[instruction_pointer] = curr + 1
    return instruction_pointer + curr, clean_list


def strange_jump_from(instruction_pointer, clean_list):
    curr = clean_list[instruction_pointer]
    if curr >= 3:
        clean_list[instruction_pointer] = curr - 1
    else:
        clean_list[instruction_pointer] = curr + 1

    return instruction_pointer + curr, clean_list


def solve_for_file_with_strange_jump(file_name):
    return perform_instructions(get_instructions_from_file(file_name), strange_jump_from)


def solve_for_file(file_name):
    return perform_instructions(get_instructions_from_file(file_name), jump_from)


def solve_for_string(input_string):
    return perform_instructions(map(lambda x: int(x), input_string.split(None)), jump_from)


def solve_for_string_with_strange_jump(input_string):
    return perform_instructions(map(lambda x: int(x), input_string.split(None)), strange_jump_from)


def get_instructions_from_file(file_name):
    with open(file_name) as testfile:
        content = testfile.readlines()
    return map(lambda x: int(x), content)


def perform_instructions(instruction_list, jump_func):
    instruction_pointer = 0
    step = 0
    while instruction_pointer < len(instruction_list):
        instruction_pointer, instruction_list = jump_func(instruction_pointer, instruction_list)
        step += 1
    return step
