import numpy as np 

# Data
def load_data():
    f = open('day20_input.txt', 'r')
    l = f.read().replace('#', '1').replace('.', '0')
    f.close()
    l = l.split('\n\n')
    d = {}
    for image in l:
        tile = image.split('\n')
        name = tile[0].split(' ')[1][:-1]
        up = tile[1]
        down = tile[-1]
        right = ''.join([tile[i][-1] for i in range(1, len(tile[0]) + 1)])
        left = ''.join([tile[i][0] for i in range(1, len(tile[0]) + 1)])
        d[name] = {
            'sides' : {
                'up': up,
                'down': down,
                'right': right,
                'left': left
            },
            'neighbors': {},
            'orientation': []
        }
    return d

d = load_data()


def get_neighbor(tile_name, d):
    tile = d[tile_name]
    n = list(d.keys())
    n.remove(tile_name)
    for t in n:
        for side in tile['sides']:
            for s in d[t]['sides']:
                if d[t]['sides'][s] == tile['sides'][side]:
                    tile['neighbors'][t] = [side, s]
                    break
                elif d[t]['sides'][s][::-1] == tile['sides'][side]:
                    tile['orientation'].append(side)
                    tile['neighbors'][t] = [side, s]
                    break
    return d

def solution1(d):
    for tile in d.keys():
        d = get_neighbor(tile, d)
    p = 1
    for tile in d:
        if len(d[tile]['neighbors']) == 2:
            p*=int(tile)
    return p, d

p , d = solution1(d)

def trim_orientate(image):
    #tile = d['image']
    pass
    

print(d)


