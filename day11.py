import copy

# Data
def load_data():
    f = open('/Users/macuser/Desktop/AdventOfCode/day11_input.txt', 'r')
    l = f.readlines()
    f.close()
    for i in range(len(l)):
        l[i] = list(l[i].replace('\n', ''))
    return l

# Puzzle 1
def num_neighbors(i, j, l):
    num_n = 0
    x_pos = [i, i-1, i+1]
    y_pos = [j, j-1, j+1]
    for x in x_pos:
        for y in y_pos:
            if x != i or y != j:
                try:
                    if l[x][y] == '#' and x >= 0 and y >= 0:
                        num_n += 1
                except:
                    pass
    return num_n

def next_step(l):
    new_list = copy.deepcopy(l)
    length = len(l)
    height = len(l[0])
    for i in range(length):
        for j in range(height):
            n_neighbors = num_neighbors(i, j, l)
            if l[i][j] == 'L' and n_neighbors == 0:
                new_list[i][j] = '#'
            if l[i][j] == '#' and n_neighbors >= 4:
                new_list[i][j] = 'L'
    return new_list

def game_of_life(l):
    k = [['#']]
    occupied = 0
    while k != l:
        k, l = copy.deepcopy(l), next_step(l)
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == '#':
                occupied += 1
    return occupied

# Puzzle 2
def get_column(i, j, l):
    c = []
    index = i
    n = len(l)
    for i in range(n):
        c.append(l[i][j])
    return index, c

def get_row(i, j, l):
    r = []
    index = j
    n = len(l[0])
    for j in range(n):
        r.append(l[i][j])
    return index, r

def get_second_diagonal(i, j, l):
    length = len(l) - 1 #i
    height = len(l[0]) - 1 #j
    d = []
    i_, j_ = i + 1, j - 1
    while i >= 0 and j <= height:
        d.append(l[i][j])
        i -= 1
        j += 1
    d = d[::-1]
    index = len(d) - 1
    while i_ <= length and j_ >= 0:
        d.append(l[i_][j_])
        i_ += 1
        j_ -= 1
    return index, d

def get_first_diagonal(i, j, l):
    length = len(l) - 1 #i
    height = len(l[0]) - 1 #j
    d = []
    i_, j_ = i + 1, j + 1
    while i >= 0 and j >= 0:
        d.append(l[i][j])
        i -= 1
        j -= 1
    d = d[::-1]
    index = len(d) - 1
    while i_ <= length and j_ <= height:
        d.append(l[i_][j_])
        i_ += 1
        j_ += 1
    return index, d

def num_n_list(input):
    index, k = input
    n_neighbor = 0
    start = k[:index]
    end = k[index+1:][::-1]
    if start:
        s = start.pop()
        while s == '.' and start:
            s = start.pop()
        if s == '#':
            n_neighbor+=1
    if end:
        e = end.pop()
        while e == '.' and end:
            e = end.pop()
        if e == '#':
            n_neighbor += 1
    return n_neighbor

def num_neighbors2(i, j, l):
    n = 0
    n += num_n_list(get_column(i, j, l))
    n += num_n_list(get_row(i, j, l))
    n += num_n_list(get_first_diagonal(i, j, l))
    n += num_n_list(get_second_diagonal(i, j, l))
    return n

def next_step2(l):
    new_list = copy.deepcopy(l)
    length = len(l)
    height = len(l[0])
    for i in range(length):
        for j in range(height):
            n_neighbors = num_neighbors2(i, j, l)
            if l[i][j] == 'L' and n_neighbors == 0:
                new_list[i][j] = '#'
            if l[i][j] == '#' and n_neighbors >= 5:
                new_list[i][j] = 'L'
    return new_list

def game_of_life2(l):
    k = [['#']]
    occupied = 0
    while k != l:
        k, l = copy.deepcopy(l), next_step2(l)
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == '#':
                occupied += 1
    return occupied

if __name__ == "__main__":
    l=load_data()
    print('------------------')
    print('Occupied seats puzzle 1:', game_of_life(l))
    print('------------------')
    print('Occupied seats puzzle 2:', game_of_life2(l))
    print('------------------')