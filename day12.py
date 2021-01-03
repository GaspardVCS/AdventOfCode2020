# Data 
def load_data():
    f = open('/Users/macuser/Desktop/AdventOfCode/day12_input.txt', 'r')
    l = f.readlines()
    f.close()
    for i in range(len(l)):
        l[i] = (l[i][0], int(l[i].replace('\n', '')[1:]))
    return l

l = load_data()

# Puzzle 1

def new_direction(facing, direction, degrees):
    d = ['N', 'E', 'S', 'W']
    n = int(degrees/90) if direction == 'R' else -int(degrees/90)
    for i in range(len(d)):
        if d[i] == facing:
            return d[(i+n)%4]

def solution1(l):
    facing = 'E'
    d = {'E': 0, 'N': 0, 'W': 0, 'S': 0}
    for direction in l:
        if direction[0] == 'R' or direction[0] == 'L':
            facing = new_direction(facing, direction[0], direction[1])
        elif direction[0] == 'F':
            d[facing] += direction[1]
        else:
            d[direction[0]] += direction[1]
    return abs(d['E'] - d['W']) + abs(d['N'] - d['S'])

# Puzzle 2

def new_way_point(way_point, direction, degrees):
    d = ['N', 'E', 'S', 'W']
    new_way = {}
    n = int(degrees/90) if direction == 'L' else -int(degrees/90)
    for i in range(len(d)):
        new_way[d[i]] = way_point[d[(i+n)%4]]
    return new_way

def solution2(l):
    way_point = {'E': 10, 'N': 1, 'W': 0, 'S': 0}
    d = {'E': 0, 'N': 0, 'W': 0, 'S': 0}
    for direction in l:
        if direction[0] == 'R' or direction[0] == 'L':
            way_point = new_way_point(way_point, direction[0], direction[1])
        elif direction[0] == 'F':
            for k in way_point:
                d[k] += direction[1]*way_point[k]
        else:
            way_point[direction[0]] += direction[1]
    return abs(d['E'] - d['W']) + abs(d['N'] - d['S'])

print(solution2(l))
        