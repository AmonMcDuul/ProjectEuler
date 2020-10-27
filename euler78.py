# Let p(n) represent the number of different ways in which n coins can be separated into piles. 
# For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n for which p(n) is divisible by one million.

from sympy.ntheory import npartitions

for i in range(1,100000):
    x = npartitions(i)
    if x % 1000000 == 0:
        print('resultaat: ', x)
        print('n: ', i)
        break
    if i % 1000 == 0:
        print('tussenstand: ', i, x)