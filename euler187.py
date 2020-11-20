# A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.
# There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.
# How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?

import math

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

l = sieveOfEratosthenes(50000000)
print('Sieve generated')

result = 0
count = 0
print(len(l))
for i in l:
    count +=1
    if count % 100000 == 0:
        print(count, ' Tussenstandje ', result)
    for j in l:
        if i <= j:
            if i*j < 10**8:
                result +=1
        if i*j > 10**8:
            break

print(result)
