# Data
f = open('/Users/macuser/Desktop/AdventOfCode/day6_entry.txt', 'r')
l = f.read()
f.close()
l = l.split('\n\n')

# Puzzle 1
def solution1(l):
    s = 0
    for group in l:
        group = group.replace('\n', '')
        s += len(set(group))
    return s

# Puzzle 2
def same_answer(group):
    d = {}
    group = group.split('\n')
    group_size = len(group)
    for person in group:
        for letter in person:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
    same_answers = 0
    for key in d:
        if d[key] == group_size:
            same_answers += 1
    return same_answers
    
def solution2(l):
    total = 0
    for group in l:
        total += same_answer(group)
    return total


if __name__ == "__main__":
    print('--------------------------')
    print('Total puzzle 1:', solution1(l))
    print('--------------------------')
    print('Total puzzle 2:', solution2(l))
    print('--------------------------')