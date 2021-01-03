# Data 
f = open('/Users/macuser/Desktop/AdventOfCode/day5_entry.txt', 'r')
l = f.readlines()
f.close()
for i in range(len(l)):
    l[i] = l[i].replace('\n', '')

# Puzzle 1
def get_seat_id(seat):
    row_id = seat[:7]
    seat_id = seat[-3:]
    row_id = row_id.replace('F', '0').replace('B', '1') #The 7 first letters gives you the rrow ID in binary
    row_id = int(row_id, 2)
    seat_id = seat_id.replace('L', '0').replace('R', '1') # same
    seat_id = int(seat_id, 2)
    return seat_id + 8*row_id

def solution1(l):
    max_ = 0
    for seat in l:
        seat_id = get_seat_id(seat)
        if seat_id >= max_:
            max_ = seat_id
    return max_

# Puzzle 2

def solution2(l):
    max_ = 991
    seats= [get_seat_id(seat) for seat in l]
    missing_seats = []
    for i in range(max_):
        if i not in seats:
            missing_seats.append(i)
    return missing_seats

if __name__ == "__main__":
    print('----------------------')
    print('Max seat id puzzle 1:', solution1(l))
    print('----------------------')
    print('Missing seats puzzle 2:', solution2(l))
    print('----------------------')