# Data 
def load_data():
    f = open('day22_input.txt', 'r')
    l = f.read()
    f.close()
    l = l.split('\n\n')
    player1 = l[0].split(':\n')[1].split('\n')
    player2 = l[1].split(':\n')[1].split('\n')
    for i in range(len(player1)):
        player1[i] = int(player1[i])
        player2[i] = int(player2[i])
    return player1, player2

# Puzzle 1

def solution1(player1, player2):
    while player1 and player2:
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if p1 > p2:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)
    p = player1 + player2
    s = 0
    for i in range(len(p)):
        s += p[i]*(len(p) - i)
    return s

# Puzzle 2

def recursive_combat(player1, player2, precedent_games = {}):
    while player1 and player2:
        if tuple(player1) in precedent_games:
            if player2 == precedent_games[tuple(player1)]:
                return 'player1', player1
        precedent_games[tuple(player1)] = player2
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if p1 <= len(player1) and p2 <= len(player2):
            winner, _ = recursive_combat(player1[:p1], player2[:p2])
            if winner == 'player1':
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
        else:
            if p1 > p2:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
    if player1:
        winner = 'player1'
        return winner, player1
    winner = 'player2'
    return winner, player2

def solution2(player):
    n = len(player)
    s = sum([(n-i)*player[i] for i in range(n)])
    return s

if __name__ == "__main__":
    p1, p2 = load_data()
    _, player = recursive_combat(p1, p2)
    p1, p2 = load_data()
    print('-----------------')
    print('Score winner puzzle 1:', solution1(p1, p2))
    print('-----------------')
    print('Score winner puzzle 2:', solution2(player))
    print('-----------------')
