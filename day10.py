# Data
def load_data():
    f = open('/Users/macuser/Desktop/AdventOfCode/day10_input.txt', 'r')
    l = f.readlines()
    f.close()
    for i in range(len(l)):
        l[i] = int(l[i].replace('\n', ''))
    return l

# Puzzle 1
def solution1(l):
    m = max(l)
    l.append(0)
    l.append(m + 3)
    l.sort()
    one_step = 0
    three_step = 0
    for i in range(len(l) - 1):
        if l[i+1] - l[i] == 1:
            one_step+=1
        if l[i+1] - l[i] == 3:
            three_step+=1
    return one_step*three_step

# Puzzle 2
def solution2(target):
    table = {}
    table[0] = 1
    table[1] = 1 if 1 in l else 0
    if 2 in l:
        if 1 in l:
            table[2] = 2
        else:
            table[2] = 1
    else:
        table[2] = 0
    for i in range(3, target+1):
        if i in l:
            table[i] = table[i-1] + table[i-2] + table[i-3]
        else:
            table[i] = 0
    return table[target]

if __name__ == "__main__":
    l =load_data()
    l.append(max(l) + 3)
    target = max(l)
    print('--------------------')
    print('Solution puzzle 1:', solution1(l))
    print('--------------------')
    print('Number of distinct ways:', solution2(target))
    print('--------------------')