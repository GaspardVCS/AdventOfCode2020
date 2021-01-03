# Data
def load_data():
    f = open('/Users/macuser/Desktop/AdventOfCode/day18_input.txt', 'r')
    l = f.readlines()
    f.close()
    for i in range(len(l)):
        l[i] = l[i].replace('\n', '')
    return l


# Puzzle 1
import operator

ops = {
    '+' : operator.add,
    '*' : operator.mul,
}

def calculate(s):
    s = s.split(' ')
    result = int(s[0])
    for i in range(1, len(s), 2):
        result = ops[s[i]](result, int(s[i+1]))
    return result

def get_bracket(s):
    opened = []
    brackets = []
    for i in range(len(s)):
        if s[i] == '(':
            opened.append(i)
        elif s[i] == ')':
            couple = [opened.pop(), i]
            brackets.append(couple)
    return brackets

def replace(s, bracket):
    start = bracket[0]
    end = bracket[1]
    s = s[:start] + str(calculate(s[start + 1:end])) + s[end+1:]
    return s

def calculate_full_string(s):
    brackets = get_bracket(s)
    while brackets != []:
        b = brackets.pop(0)
        s = replace(s, b)
         # Pas efficace, on recalcule à chaque fois les positions 
         # des parenthèses alors qu'on a juste a les updatea chaque 
         # remplacement
        brackets = get_bracket(s)
    return calculate(s)

def solution1(l):
    s = 0
    for expression in l:
        s += calculate_full_string(expression)
    return s

# Puzzle 2

def calculate2(s):
    s = s.split(' * ')
    p = 1
    for expression in s:
        p *= calculate(expression)
    return p

def replace2(s, bracket):
    start = bracket[0]
    end = bracket[1]
    s = s[:start] + str(calculate2(s[start + 1:end])) + s[end+1:]
    return s


def calculate_full_string2(s):
    brackets = get_bracket(s)
    while brackets != []:
        b = brackets.pop(0)
        s = replace2(s, b)
         # Pas efficace, on recalcule à chaque fois les positions 
         # des parenthèses alors qu'on a juste a les updatea chaque 
         # remplacement
        brackets = get_bracket(s)
    return calculate2(s)


def solution2(l):
    s = 0
    for expression in l:
        s += calculate_full_string2(expression)
    return s

if __name__ == "__main__":
    l = load_data()
    print('--------------------------')
    print('Puzzle 1:', solution1(l))
    print('--------------------------')
    print('Puzzle 2:', solution2(l))
    print('--------------------------')





