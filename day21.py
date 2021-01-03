import itertools

# Data 
def load_data():
    f = open('day21_input.txt', 'r')
    l = f.readlines()
    f.close()
    d = {}
    for i in range(len(l)):
        l[i] = l[i].replace('\n', '')
        a = l[i].split(' (')
        products = a[0].split(' ')
        allergens = a[1].split('contains ')[1].split(', ')
        allergens[-1] = allergens[-1][:-1]
        for allergen in allergens:
            if allergen in d:
                d[allergen].append(products)
            else:
                d[allergen] = [products]
    for k in d:
        a = d[k]
        possible_products = []
        for p in a[0]:
            if all(p in sublist for sublist in a):
                possible_products.append(p)
        d[k] = possible_products
    return d

# Puzzle 1
def products_allergens(products):
    new_dict = {}
    n = len(products)
    for _ in range(n):
        for p in products:
            if len(products[p]) == 1:
                position = products[p][0]
                new_dict[p] = position
                for c in products:
                    if position in products[c]:
                        products[c].remove(position)
                del products[p]
                break
    return new_dict


def list_products():
    p = []
    f = open('day21_input.txt', 'r')
    l = f.readlines()
    f.close()
    for i in range(len(l)):
        l[i] = l[i].replace('\n', '')
        a = l[i].split(' (')
        products = a[0].split(' ')
        p.append(products)
    return list(itertools.chain.from_iterable(p))

def solution1(allergens):
    s = 0
    products = list_products()
    for p in products:
        if p not in allergens.values():
            s += 1
    return s

# Puzzle 2
def solution2(product_allergen):
    canonical = ''
    allergens = list(product_allergen.keys())
    allergens.sort()
    for a in allergens:
        canonical += product_allergen[a] + ','
    return canonical[:-1]

if __name__ == "__main__":
    d = load_data()
    allergens = products_allergens(d)
    print('--------------------')
    print('Puzzle 1:', solution1(allergens))
    print('--------------------')
    print('Puzzle 2:', solution2(allergens))
    print('--------------------')
