import sys

trihex = []

for n in range(40755,100000):
    trinumber = (n*(n+1))/2
    indexhex = trinumber/n
    if indexhex.is_integer() == True:
        if indexhex * (2*indexhex - 1) == trinumber:
            trihex.append([int(trinumber),int(n),int(indexhex)])

for number in trihex:
    if number[0] > 40755:
        for x in range(number[2],number[1]):
            if number[0] == (x*(3*x-1))/2:
                    print(number[0])
                    sys.exit()