import math

# Data 
def load_data(puzzle):
    f = open('/Users/macuser/Desktop/AdventOfCode/day13_input.txt')
    l = f.readlines()
    f.close()
    l[0] = int(l[0])
    l[1] = l[1].split(',')
    if puzzle == 1:
        k = []
        for i in range(len(l[1])):
            if l[1][i] != 'x':
                k.append(int(l[1][i]))
        return [l[0], k]
    else:
        k = []
        for i in range(len(l[1])):
            try:
                k.append(int(l[1][i]))
            except:
                k.append(l[1][i])
        return k
    

# Puzzle 1

def solution1(l):
    objective = l[0]
    min_ = math.inf
    b = 0
    for bus in l[1]:
        print(bus, objective%bus)
        n = (int(objective//bus) + 1)*bus - objective
        if  n <= min_:
            min_ = n
            b = bus
    return min_*b

# Puzzle 2
def euclide(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, u, v) = euclide(b, a%b)
        return (d, v, u - int(a/b)*v)
    

def compute_n(l):
    n = 1
    for i in range(len(l)):
        if l[i] == 'x':
            pass
        else:
            n *= l[i]
    return n

def solution2(l):
    n = compute_n(l)
    solution = 0
    for i in range(len(l)):
        if l[i] == 'x':
            pass
        else:
            n_i = l[i]
            n2 = int(n/n_i)
            v = euclide(n_i, n2)[2]
            solution += v*n2*(l[i] - i - 1)
    return solution%n + 1



l = load_data(2)
print(solution2(l))