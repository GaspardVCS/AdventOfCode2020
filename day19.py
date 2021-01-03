import itertools

# Data

def load_data():
    f = open('/Users/macuser/Desktop/AdventOfCode/day19_input.txt', 'r')
    l = f.read().split('\n\n')
    f.close()
    rules = l[0].split('\n')
    grammar = {}
    for rule in rules:
        rule = rule.split(': ')
        rule_name = rule[0]
        rule1 = rule[1].split(' | ')[0]
        try:
            rule2 = rule[1].split(' | ')[1]
            if rule2 in grammar:
                grammar[rule2].append(rule_name)
            else:
                grammar[rule2] = [rule_name]
            
        except:
            pass
        if rule1 in grammar:
            grammar[rule1].append(rule_name)
        else:
            grammar[rule1] = [rule_name]
        
    words = l[1].split('\n')
    return grammar, words

grammar, words = load_data()

word = words[0]
#print(word)
#print(grammar)

def match(word, grammar):
    word = list(word)
    for i in range(len(word)):
        if word[i] == 'a':
            word[i] = ['69']
        else:
            word[i] = ['12']
    for i in range(len(word) - 1):
        new_word = []
        for i in range(len(word)-1):
            combination = []
            keys = [id1 + ' ' + id2 if id1 and id2 else id1 + id2 for id1 in word[i] for id2 in word[i+ 1]]
            for key in keys:
                if key in grammar:
                    for idx in grammar[key]:
                        combination.append(idx)
            new_word.append(combination if combination else [''])
            del combination
        del word
        word = new_word.copy()
        del new_word
        print(word)
    return list(itertools.chain.from_iterable(word)) == ['0']

word = 'aaa'
match(word, grammar)