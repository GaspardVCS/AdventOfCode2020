# Data 
def load_data():
    l = open('day01_input.txt', 'r').readlines()
    for i in range(len(l)):
        l[i] = int(l[i].replace('\n', ''))
    return l

# Puzzle 1
def solution1(l, target):
    d = {}
    for el in l:
        if (target - el) not in d:
            d[el] = 1
        else:
            return el * (target-el)

# Puzzle 2
def solution2(l):
    for i in range(len(l)):
        l2 = l[:i] + l[i:]
        target = 2020 - l[i]
        d = {}
        for el in l2:
            if (target - el) not in d:
                d[el] = 1
            else:
                return l[i]*el*(2020 - l[i] - el)

if __name__ == "__main__":
    l = load_data()
    print('---------------------------')
    print('Puzzle 1:', solution1(l, 2020))
    print('---------------------------')
    print('Puzzle 2:', solution2(l))
    print('---------------------------')
