
def find_severity(inputs):
    splits = map(lambda x: x.split(":"), inputs)
    severities = [sum_caught(x, 0) for x in  splits]
    return sum(severities)


def sum_caught(x, delay):
    return int(x[0]) * int(x[1]) if int(x[0]) + delay % ((int(x[1])-1)*2) == 0 else 0 

def read_file(file_name):
    with open(file_name) as testfile:
        content = testfile.readlines()
    return content

def find_delay(inputs):
    splits = map(lambda x: x.split(":"), inputs)
    my_sum = 1
    delay = 0
    while my_sum > 0:
        delay += 1
        severities = [sum_caught(x, delay) for x in  splits]
        my_sum = sum(severities)
        
    return delay