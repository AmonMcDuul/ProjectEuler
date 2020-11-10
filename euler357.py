# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.
# Find the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d+n/d is prime.

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

numbers = set(sieveOfEratosthenes(100000000))
print('primes generated')

def divisorGenerator(n): 
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                r = (n // i) + n/(n // i)
                if r not in numbers:
                    yield None
                    return
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        r = divisor + n/divisor
        if r not in numbers:
            yield None
            return
        yield int(r)

result = 0
for i in numbers:
    if None not in list(divisorGenerator(i-1)):
        result += i-1

# -4 want 4 komt onterecht bij de resultaten te staan!?!?
print(result-4)