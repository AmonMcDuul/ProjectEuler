# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

import sys
import math 

def primeFactors(n): 
    primeSet = set()
    while n % 2 == 0: 
        n = n // 2
        primeSet.add(2)
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            primeSet.add(i)
            n = n // i 
    if n > 2: 
        primeSet.add(n)
    return primeSet

for i in range(1,1000000):
    if len(primeFactors(i)) >= 4:
        if len(primeFactors(i+1)) >= 4:
            if len(primeFactors(i+2)) >= 4:
                if len(primeFactors(i+3)) >= 4:
                    print("yessss: ", i)
                    sys.exit()