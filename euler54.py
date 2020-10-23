# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
# Consider the following five hands dealt to two players:
# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD
# Pair of Fives
# 	 	2C 3S 8S 8D TD
# Pair of Eights
# 	 	Player 2
# 2	 	5D 8C 9S JS AC
# Highest card Ace
# 	 	2C 5C 7D 8S QH
# Highest card Queen
# 	 	Player 1
# 3	 	2D 9C AS AH AC
# Three Aces
# 	 	3D 6D 7D TD QD
# Flush with Diamonds
# 	 	Player 2
# 4	 	4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
# 	 	3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
# 	 	Player 1
# 5	 	2H 2D 4C 4D 4S
# Full House
# With Three Fours
# 	 	3C 3D 3S 9S 9D
# Full House
# with Three Threes
# 	 	Player 1
# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
# How many hands does Player 1 win?

#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

#     Straight Flush: All cards are consecutive values of same suit.

#     Four of a Kind: Four cards of the same value.

#     Full House: Three of a kind and a pair.

#     Flush: All cards of the same suit.

#     Straight: All cards are consecutive values.

#     Three of a Kind: Three cards of the same value.

#     Two Pairs: Two different pairs.

#     One Pair: Two cards of the same value.

#     High Card: Highest value card.

ranks = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

tie = 0
pOne = 0
pTwo = 0

def checkCard(one,two):
    global tie
    global pOne
    global pTwo

    if royalFlush(one):
        if royalFlush(two):
            tie+=1
            return
        pOne+=1
        return
    if royalFlush(two):
        pTwo+=1
        return

    if straightFlush(one):
        if straightFlush(two):
            if points(one,two) == 0:
                tie+=1
                return
            if points(one,two) == 1:
                pOne+=1
                return
            if points(one,two) == 2:
                pTwo+=1
                return
        pOne+=1
        return
    if straightFlush(two):
        pTwo+=1
        return

    if fourOfAKind(one):
        if fourOfAKind(two):
            if points(one,two) == 0:
                tie+=1
                return
            if points(one,two) == 1:
                pOne+=1
                return
            if points(one,two) == 2:
                pTwo+=1
                return
        pOne+=1
        return
    if fourOfAKind(two):
        pTwo+=1
        return

    if fullHouse(one):
        if fullHouse(two):
            if points(one,two) == 0:
                tie+=1
                return
            if points(one,two) == 1:
                pOne+=1
                return
            if points(one,two) == 2:
                pTwo+=1
                return
        pOne+=1
        return
    if fullHouse(two):
        pTwo+=1
        return 

    if flush(one):
        if flush(two):
            if points(one,two) == 0:
                tie+=1
                return
            if points(one,two) == 1:
                pOne+=1
                return
            if points(one,two) == 2:
                pTwo+=1
                return
        pOne+=1
        return
    if flush(two):
        pTwo+=1
        return 

    if straight(one):
        if straight(two):
            if points(one,two) == 0:
                tie+=1
                return
            if points(one,two) == 1:
                pOne+=1
                return
            if points(one,two) == 2:
                pTwo+=1
                return
        pOne+=1
        return
    if straight(two):
        pTwo+=1
        return 

    if threeOfAKind(one):
        if threeOfAKind(two):
            if points(one,two) == 0:
                tie+=1
                return
            if points(one,two) == 1:
                pOne+=1
                return
            if points(one,two) == 2:
                pTwo+=1
                return
        pOne+=1
        return
    if threeOfAKind(two):
        pTwo+=1
        return 

    if twoPairs(one):
        if twoPairs(two):
            if points(one,two) == 0:
                tie+=1
                return
            if points(one,two) == 1:
                pOne+=1
                return
            if points(one,two) == 2:
                pTwo+=1
                return
        pOne+=1
        return
    if twoPairs(two):
        pTwo+=1
        return

    if onePair(one):
        if onePair(two):
            if points(one,two) == 0:
                tie+=1
                return
            if points(one,two) == 1:
                pOne+=1
                return
            if points(one,two) == 2:
                pTwo+=1
                return
        pOne+=1
        return
    if onePair(two):
        pTwo+=1
        return

    if highCard(one):
        if highCard(two):
            if points(one,two) == 0:
                tie+=1
                return
            if points(one,two) == 1:
                pOne+=1
                return
            if points(one,two) == 2:
                pTwo+=1
                return
        pOne+=1
        return

def royalFlush(n):
    x = set()
    s = set()
    for i in n:
        x.add(i[:1])
        s.add(i[1:2])
    if set(['T', 'J', 'Q', 'K', 'A']) == x:
        if len(s) == 1:
            return True

def straightFlush(n):
    x = set()
    s = set()
    f = 16
    l = 0
    for i in n:
        res = ranks[i[:1]]
        if f > res:
            f = res 
        if l < res:
            l = res
        s.add(i[1:2])
    r = l - f
    if len(s) == 1:
        if r == 4:
            return True

def fourOfAKind(n):
    d = []
    for i in n:
        d.append(i[:1]) 
    dupl = {i:d.count(i) for i in d}
    for i in dupl:
        if dupl[i] == 4:
            return True

def fullHouse(n):
    l = set()
    count = 0
    for i in n:
        l.add(i[:1])
    if len(l) == 2:
        return True   

def flush(n):
    s = set()
    for i in n:
        s.add(i[1:2])
    if len(s) == 1:
        return True

def straight(n):
    x = set()
    f = 16
    l = 0
    for i in n:
        res = ranks[i[:1]]
        if f > res:
            f = res 
        if l < res:
            l = res
        x.add(i[:1])
    r = l - f
    if len(x) == 5:
        if r == 4:
            return True

def threeOfAKind(n):
    d = []
    for i in n:
        d.append(i[:1]) 
    dupl = {i:d.count(i) for i in d}
    for i in dupl:
        if dupl[i] == 3:
            return True

def twoPairs(n):
    l = set()
    for i in n:
        l.add(i[:1])
    if len(l) == 3:
        return True

def onePair(n):
    l = set()
    for i in n:
        l.add(i[:1])
    if len(l) == 4:
        return True

def highCard(n):
    card = 0
    for i in n:
        x = ranks[i[:1]]
        if card < x:
            card = x
    return True

def points(one, two):
    d = []
    e = []
    result = 0
    for i in one:
        d.append(ranks[i[:1]])
    for j in two:
        e.append(ranks[j[:1]])
    countOne = {k:d.count(k) for k in d}
    countTwo = {l:e.count(l) for l in e}
    q = max(d.count(k) for k in d)
    w = max(e.count(k) for k in e)
    if q <= w:
        r = w
    else:
        r = q
    first = dupliPoints(countOne,r)
    second = dupliPoints(countTwo,r)
    if first < second:
        result = 2
    elif first == second:
        r -= 1
        first = dupliPoints(countOne,r)
        second = dupliPoints(countTwo,r)
        if first < second:
            result = 2
        elif first == second:
            r -= 1
            first = dupliPoints(countOne,r)
            second = dupliPoints(countTwo,r)
            if first < second:
                result = 2
            elif first == second:
                return 0
            else:
                result = 1
        else:
            result = 1
    else:
        result = 1
    return result

def dupliPoints(n,t):
    highOne = 0  
    for x in n:
        if n[x] == t:
            if highOne < x:
                highOne = x
    return highOne



cards = []
for item in open("euler54poker.txt", "r"):
    cards.append([item.strip()]) 

hands = []

for item in cards:
    one = ''
    two = ''
    for x in item:
        one = (x[:14].strip().split(' '))
        two = (x[15:].strip().split(' '))
        checkCard(one,two)

print('Tie:', tie,   'P1:', pOne,   'P2:', pTwo)