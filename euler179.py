# Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. 
# For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

import math

def sieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    primeList = [1]
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

numbers = set(sieveOfEratosthenes(10000000))

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n // i)
    for divisor in (large_divisors):
        yield divisor

result = 0
check = 0
for i in range(2,10000000):
    # if i not in numbers:
    if i % 100000 == 0:
        print('tussenstandje: ', i)
    a = len(list(divisorGenerator(i)))
    if a == check:
        result+=1
    check = a
print(result)
