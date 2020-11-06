# The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. 
# As the sum of these divisors is equal to 28, we call it a perfect number.
# Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. 
# For this reason, 220 and 284 are called an amicable pair.
# Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
# 12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
# Since this chain returns to its starting point, it is called an amicable chain.
# Find the smallest member of the longest amicable chain with no element exceeding one million.
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

numbers = set(sieveOfEratosthenes(1000000))

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                if n//i < 1000000:
                    large_divisors.append(n // i)
                else: 
                    return 0
    for divisor in large_divisors:
        if divisor != n:
            yield divisor

l = []
d = set()

def chains(n):
    if n not in numbers:
        a = sum(list(divisorGenerator(n)))
        if a not in numbers:
            if a not in d:
                if a not in l:
                    if a != 1:
                        l.append(a)
                        return(chains(a))
                else:
                    l.append(a)
                    result = len(l) - (l.index(a)) -1
                    newList = l[(l.index(a)):len(l)+1]
                    l.clear()
                    for p in newList:
                        d.add(p)
                    # print(n, result, newList, l) 
                    return result, min(newList)
    return None

result = 0
smallest = 0
for i in range(1, 10000):
    l.clear()
    if i not in numbers:
        if i not in d:
            if i % 10000 == 0:
                print('tussenstandje: ', i)
            r = chains(i)
            if r is not None:
                chainResult = r[0]
                if chainResult is not None:
                    if result < chainResult:
                        result = chainResult
                        smallest = r
print('result: ', smallest[1])