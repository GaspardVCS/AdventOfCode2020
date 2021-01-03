import sys 
sys.setrecursionlimit(10**6)  # trop de recursion, obligé d'augmenter la limite

# data
def load_data():
    d = {}
    f = open('/Users/macuser/Desktop/AdventOfCode/day08_input.txt')
    l = f.readlines()
    f.close()
    for i, el in enumerate(l):
        el = el.replace('\n', '').split(' ')
        commande = el[0]
        delta = int(el[1])
        d[i] = [commande, delta, False]
    return d

# puzzle 1

def solution1(index, d, accumulation):
    if index >= len(d):
        return accumulation
    if d[index][2]:
        return accumulation
    d[index][2] = True
    if d[index][0] == 'acc':
        accumulation += d[index][1]
        index += 1
    elif d[index][0] == 'jmp':
        index += d[index][1]
    else:
        index += 1
    return solution1(index, d, accumulation)


# Puzzle 2
def clean_dict(d):
    for k in d:
        d[k][2] = False
    return d

def solution2(index, d, pile):
    if index == len(d) - 1:
        print('Finish')
        return d
    if d[index][2]:
        new_index = pile.pop()
        d[new_index][0] = 'jmp' if d[new_index][0]=='nop' else 'nop'
        return solution2(new_index, clean_dict(d), pile)
    d[index][2] = True
    if d[index][0] == 'jmp':
        pile.append(index)
        new_index = index + d[index][1]
    elif d[index][0] == 'nop':
        pile.append(index)
        new_index = index + 1
    else:
        new_index = index + 1
    return solution2(new_index, d, pile)

if __name__ == "__main__":
    d = load_data()
    d2 = load_data()
    d2 = solution2(0, d2, [])
    print('-----------------')
    print('Accumulation puzzle 1:', solution1(0, d, 0))
    print('------------------')
    print('Accumulation puzzle 2:', solution1(0, clean_dict(d2), 0))
    print('------------------')