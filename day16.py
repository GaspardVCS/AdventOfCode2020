# Data 
def load_data():
    f = open('/Users/macuser/Desktop/AdventOfCode/day16_input.txt', 'r')
    l = f.read()
    f.close()
    category, ticket, nearby_tickets = l.split('\n\n')
    category = category.split('\n')

    # category
    c = {}
    for i in range(len(category)):
        category[i] = category[i].replace('\n', '').split(': ')
        name = category[i][0]
        valid = category[i][1].split(' or ')
        first = [int(valid[0].split('-')[0]), int(valid[0].split('-')[1])]
        last = [int(valid[1].split('-')[0]), int(valid[1].split('-')[1])]
        valid = first + last
        c[name] = valid
    
    # ticket
    ticket = ticket.split(':\n')[1].split(',')
    for i in range(len(ticket)):
        ticket[i] = int(ticket[i])
    
    # nearby_tickets
    nearby_tickets = nearby_tickets.split(':\n')[1].split('\n')
    for i in range(len(nearby_tickets)):
        nearby_tickets[i] = nearby_tickets[i].split(',')
        for j in range(len(nearby_tickets[i])):
            nearby_tickets[i][j] = int(nearby_tickets[i][j])
    
    return c, ticket, nearby_tickets

# Puzzle 1

def valid_ticket(ticket, category):
    invalid = 0
    for i in range(len(ticket)):
        for c in category:
            if not ((category[c][0] <= ticket[i] <= category[c][1]) or (category[c][2] <= ticket[i] <= category[c][3])):
                invalid += 1
        if invalid == len(category):
            return ticket[i]
        invalid = 0
    return 0

def solution1(category, tickets):
    s = 0
    for t in tickets:
        s += valid_ticket(t, category)
    return s

# Puzzle 2

def valid_ticket2(ticket, category):
    invalid = 0
    for i in range(len(ticket)):
        for c in category:
            if not ((category[c][0] <= ticket[i] <= category[c][1]) or (category[c][2] <= ticket[i] <= category[c][3])):
                invalid += 1
        if invalid == len(category):
            return False
        invalid = 0
    return True

def keep_only_valid_tickets(nearby_tickets, category):
    return [t for t in nearby_tickets if valid_ticket2(t, category)]

def valid_position(category, ticket):
    v = {}
    for c in category:
        v[c] = [i for i in range(len(ticket))]
    return v

def get_category_valid_position(tickets, category, valid_pos):
    for ticket in tickets:
        for i in range(len(ticket)):
            for c in category:
                if not ((category[c][0] <= ticket[i] <= category[c][1]) or (category[c][2] <= ticket[i] <= category[c][3])):
                    if i in valid_pos[c]:
                        valid_pos[c].remove(i)
    return valid_pos


def category_position(valid):
    d = {}
    n = len(valid)
    for _ in range(n):
        for v in valid:
            if len(valid[v]) == 1:
                position = valid[v][0]
                d[v] = position
                for c in valid:
                    if position in valid[c]:
                        valid[c].remove(position)
                del valid[v]
                break
    return d

def solution2(ticket, d):
    m = 1
    for c in d:
        if 'depart' in c:
            m *= ticket[d[c]]
    return m

if __name__ == "__main__":
    category, ticket, nearby_tickets = load_data()
    print('--------------------------')
    print('Puzzle 1:', solution1(category, nearby_tickets))
    print('--------------------------')
    valid_pos = valid_position(category, ticket)
    tickets = keep_only_valid_tickets(nearby_tickets, category)
    valid = get_category_valid_position(tickets, category, valid_pos)
    d = category_position(valid)
    print('Puzzle 2:', solution2(ticket, d))
    print('--------------------------')


