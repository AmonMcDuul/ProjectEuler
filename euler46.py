# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import sys

def sieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    primeList = []
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(n + 1): 
        if prime[p]: 
           primeList.append(p)
    return primeList

numbers = sieveOfEratosthenes(5000)

def isComposite(n): 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return False
    if (n % 2 == 0 or n % 3 == 0): 
        return True
    i = 5
    while(i * i <= n):          
        if (n % i == 0 or n % (i + 2) == 0): 
            return True
        i = i + 6         
    return False

numbersToCheck = set()
for primes in numbers:
    for square in range(0,1000,1):
        if (int(primes)+(2*(square*square)) not in numbersToCheck):
            numbersToCheck.add(int(primes)+(2*(square*square)))
    
for i in range(1,10000,2):
    if(isComposite(i)):
        if i not in numbersToCheck:
            print(i)
            sys.exit()
