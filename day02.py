# Data 
def load_data():
    l = open('day02_input.txt', 'r').readlines()
    for i in range(len(l)):
        l[i] = l[i].replace('\n', '')
    return l

# Puzzle 1
def solution1(l):
    valid_passwords = 0
    for p in l:
        sep = p.split(' ')
        password = sep[2]
        min_ = int(sep[0].split('-')[0])
        max_ = int(sep[0].split('-')[1])
        letter = sep[1][0]
        count = 0
        for l in password:
            if l==letter:
                count += 1
        if count<=max_ and count>=min_:
            valid_passwords+=1
    return valid_passwords

# Puzzle 2
def solution2(l):
    valid_passwords = 0
    for p in l:
        sep = p.split(' ')
        password = sep[2]
        pos1 = int(sep[0].split('-')[0]) - 1
        pos2 = int(sep[0].split('-')[1]) - 1
        letter = sep[1][0]
        if (letter == password[pos1]) != (letter == password[pos2]):
            valid_passwords+=1
    return valid_passwords


if __name__ == "__main__":
    l = load_data()
    print('-----------------------')
    print('Valid passwords, puzzle 1:', solution1(l))
    print('-----------------------')
    print('Valid passwords, puzzle 2:', solution2(l))
    print('-----------------------')