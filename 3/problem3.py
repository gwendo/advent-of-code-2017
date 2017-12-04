
_right = (1, 0)
_east = (1, 0)
_up = (0, 1) 
_north = (0, 1)
_left = (-1, 0)
_west = (-1, 0)
_down = (0, -1)
_south = (0, -1)
_northeast = (1, 1)
_nortwest = (-1, 1)
_southeast = (1, -1)
_southwest = (-1, -1)

adjecent = [_north, _northeast, _east, _southeast, _south, _southwest, _west, _nortwest]

directions = [_right, _up, _left, _down]
oddDir = [_right, _up]
evenDir = [_left, _down]

def find_distance(my_input):
    return distance(get_coordinate(my_input))

def get_coordinate(my_input):
    nextVal = next_coordinate()
    coord = (0,0)
    for (i) in xrange(1, my_input+1):
        coord = nextVal.next()
    return coord

def find_sum_larger_than_input(my_input):
    mySum = 0
    coords = []
    nextCoord = next_coordinate()
    while mySum <= my_input:
        coord = nextCoord.next()
        mySum = sum_adjecent(coord, coords)
        print "c: %s, sum: %s" % (coord, mySum)
        coords.append((coord, mySum))
    return mySum


def get_adjecent(point):
    coords = []
    for direction in adjecent:
        coords.append(go(point, direction))
    return coords        

def sum_adjecent(point, coords):
    return  1 if len(coords) == 0 else sum(map(lambda x: x[1], filter(lambda c: c[0] in get_adjecent(point), coords)))

def distance(point):
    return abs(point[0]) + abs(point[1])        

def go(point, direction):
    return (point[0] + direction[0], point[1] + direction[1])

def get_next_direction():
    callCount = 1
    stepSize = 1
    dirSelector = 0
    while True:
        dirGroup = evenDir if stepSize % 2 == 0 else oddDir
        yield dirGroup[dirSelector]
        dirSelector = callCount // stepSize 
        if callCount == stepSize * 2:
            callCount = 1
            stepSize += 1
            dirSelector = 0
        else :
            callCount += 1 
        

def next_coordinate():
    point = (0, 0)
    while True:
        for next_dir in get_next_direction():
            yield point
            point = go(point, next_dir)
            
