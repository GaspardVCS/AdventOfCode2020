# Data

def load_data(puzzle):
    f = open('/Users/macuser/Desktop/AdventOfCode/day14_input.txt', 'r')
    l = f.readlines()
    f.close()
    for i in range(len(l)):
        l[i] = l[i].replace('\n', '')
    if puzzle == 1:
        for i in range(len(l)):
            if "mask" in l[i]:
                l[i] = l[i].split('= ')[1]
            else:
                mem = l[i].split(' = ')[0][4:-1]
                value = format(int(l[i].split(' = ')[1]), "036b")
                l[i] = [mem, value]
        return l
    elif puzzle == 2:
        for i in range(len(l)):
            if "mask" in l[i]:
                l[i] = l[i].split('= ')[1]
            else:
                mem = format(int(l[i].split(' = ')[0][4:-1]), "036b")
                value = int(l[i].split(' = ')[1])
                l[i] = [mem, value]
        return l

# Puzzle 1

def app_mask1(mask, value):
    new_value = ''
    for i in range(len(mask)):
        if mask[i] == 'X':
            new_value += value[i]
        else:
            new_value += mask[i]
    return int(new_value, 2)

def solution1(l):
    d = {}
    mask = ''
    for el in l:
        if len(el) == 2:
            mem = el[0]
            value = el[1]
            d[mem] = app_mask1(mask, value)
        else:
            mask = el
    return sum(v for v in d.values())

# Puzzle 2

def app_mask2(mask, mem):
    new_mem = ''
    for i in range(len(mask)):
        if mask[i] == '1':
            new_mem += '1'
        elif mask[i] == '0':
            new_mem += mem[i]
        else:
            new_mem += 'X'
    return new_mem

def solution2(l):
    d = {}
    mask = ''
    for el in l:
        if len(el) == 2:
            mem = app_mask2(mask, el[0])
            value = el[1]
            number_X = mem.count('X')
            for i in range(2**number_X):
                new_mem = ''
                floating_bits = list(format(i, '0{}b'.format(number_X)))
                for j in range(len(mem)):
                    new_mem += floating_bits.pop() if mem[j] == 'X' else mem[j]
                d[int(new_mem, 2)] = value
        else:
            mask = el
    return sum(v for v in d.values())

if __name__ == "__main__":
    l1 = load_data(1)
    l2 = load_data(2)
    print('-----------------')
    print('Answer puzzle 1:', solution1(l1))
    print('------------------')
    print('Answer puzzle 2:', solution2(l2))
    print('------------------')