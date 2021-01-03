from tqdm import tqdm

def solution1(l, num_spoken):
    d = {} # Keys: number, values: last round spoken
    previous = l[-1]
    for i in range(len(l)):
        d[l[i]] = [i, 1]
    for i in tqdm(range(len(l), num_spoken)):
        if d[previous][1] == 1:
            previous = 0
            d[0][1] += 1
        else:
            index = d[previous][0]
            d[previous][0] = i - 1
            previous = i - 1 - index
            if previous in d:
                d[previous][1] += 1
            else:
                d[previous] = [i, 1]
    return previous

l = [0,6,1,7,2,19,20]

if __name__ == "__main__":
    print('----------------')
    print('2020th number spoken:', solution1(l, 2020))
    print('----------------')
    print('30000000th number spoken:', solution1(l, 30000000))
    print('----------------')
    