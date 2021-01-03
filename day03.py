#Data 
def load_data():
    f = open('day03_input.txt', 'r')
    pattern = f.readlines()
    f.close()
    return pattern

pattern = load_data()
#global variable
length = len(pattern) - 1
width = len(pattern[0]) - 1

# Solution 1 puzzle 1
def explore(x, y, number_trees, slope):
    if y > length:
        return number_trees
    while x <= width - 1 and y <= length:
        number_trees += 1 if pattern[y][x] == '#' else 0
        x += slope[0]
        y += slope[1]
    x = x % width
    return explore(x, y, number_trees, slope)

# Solution 2 puzzle 1
def generate_coordinates(slope):
    number_trees = 0
    x = 0
    y = 0
    while y <= length:
        number_trees += 1 if pattern[y][x] == '#' else 0
        x = (x + slope[0]) % width
        y += slope[1]
    return number_trees

# Puzzle 2
def solution2(slopes):
    product = 1
    for slope in slopes:
        product *= generate_coordinates(slope)
    return product

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

if __name__ == "__main__":
    print('---------------------------')
    print('Number of trees Puzzle 1, solution 1:', generate_coordinates((3, 1)))
    print('Number of trees Puzzle 1, solution 2:', explore(0, 0, 0, (3, 1)))
    print('---------------------------')
    print('Product dor puzzle 2:', solution2(slopes))
    print('---------------------------')