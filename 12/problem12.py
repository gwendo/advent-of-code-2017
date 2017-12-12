

def find_connected(list):
    pairs = map(lambda x: (x.split("<->")[0], x.split("<->")[1]) , list)