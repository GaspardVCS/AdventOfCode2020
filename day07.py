# Data
f = open('/Users/macuser/Desktop/AdventOfCode/day7_entry.txt')
l = f.readlines()
f.close()
for i in range(len(l)):
    l[i] = l[i].replace('\n', '')

# Create a dictionnary of bags and their components
def create_dictionary(l):
    d = {}
    for i in range(len(l)):
        s = l[i].split('contain')
        container = '_'.join(s[0].split(' ')[:2])
        d[container] = {}
        bags = s[1].split(',')
        if 'no other' in bags[0]:
            pass
        else:
            for b in bags:
                b = b.split(' ')
                number = b[1]
                bag = '_'.join(b[2:4])
                d[container][bag] = int(number)
    return d

bags = create_dictionary(l)

# puzzle 1
# list of bags that could contain an 'objective' bag including the 'objective' bag itself
def reach(objective, length):
    if len(objective) == length:
        return objective
    length = len(objective)
    for bag in bags:
        for i in range(len(objective)):
            if objective[i] in bags[bag]:
                objective.append(bag)
    return reach(list(set(objective)), length)

def solution1(l):
    objective = ['shiny_gold']
    list_of_bags = reach(objective, 0)
    return len(list_of_bags) - 1 # Shiny gold bag cannot contain shiny gold bags

# puzzle 2
def solution2(bag):
    if bags[bag] == {}:
        return 1
    else:
        s = 0
        for b in bags[bag]:
            s += bags[bag][b] if bags[b] != {} else 0
        return sum(bags[bag][b]*solution2(b) for b in bags[bag]) + s

if __name__ == "__main__":
    print('-------------')
    print('Number of bags that can contain a shiny gold bag:', solution1(l))
    print('-------------')
    print('Number of bags that a shiny gold bag shoud contain:', solution2('shiny_gold'))
    print('-------------')