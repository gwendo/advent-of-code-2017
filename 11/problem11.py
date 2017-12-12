from math import floor

directions_map = {
    'nw' : (0, 1),
    'n' : (1, 1) ,
    'ne' : (1, 0),
    'se' : (0, -1 ),
    's' :(-1, -1),
    'sw' : (-1, 0)
}

def find_path(directions):
    origin = (0, 0)
    directions = map(lambda x: directions_map[x], directions.split(","))
    end_point = reduce(lambda x, y: go(x, y), directions)
    return distance(end_point)

def max_dist(directions):
    origin = (0, 0)
    point = origin
    directions = map(lambda x: directions_map[x], directions.split(","))
    distances = []
    for direction in directions:
        point = go(point, direction)
        distances.append(distance(point))
    return max(distances)



def go(point, direction):
    return (point[0] + direction[0], point[1] + direction[1])

def distance(point):
    x0 = 0
    y0 = 0
    x1 = point[0]
    y1 = point[1]
    dx = x1 - x0
    dy = y1 - y0
    dz = (point[0]-point[1])*-1
    dist = max(abs(dx), abs(dy), abs(dz))
    return dist

def read_file(file_name):
    with open(file_name) as testfile:
        content = testfile.readlines()
    return content