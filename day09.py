# Data 
def load_data():
    f = open('/Users/macuser/Desktop/AdventOfCode/day09_input.txt', 'r')
    l = f.readlines()
    f.close()
    for i in range(len(l)):
        l[i] = int(l[i].replace('\n', ''))
    return l

# Day 01 puzzle 1
def is_sum(l, target):
    d = {}
    for el in l:
        if (target - el) not in d:
            d[el] = 1
        else:
            return True
    return False


def solution1(l):
    n = len(l)
    for i in range(25, n - 25):
        previous = l[i-25:i]
        target = l[i]
        if not is_sum(previous, target):
            return l[i]

# Puzzle 2
def solution2(l):
    target = solution1(l)
    for i in range(len(l)):
        s = 0
        index = i
        while s < target:
            s += l[index]
            index += 1
        if s == target:
            return l[i] + l[index-1]
        

if __name__ == "__main__":
    l = load_data()
    print('----------------------')
    print('Incorrect number in puzzle 1 is:', solution1(l))
    print('----------------------')
    print('Encryption weakness in puzzle 2 is:', solution2(l))
    print('----------------------')