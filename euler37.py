# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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

numbers = sieveOfEratosthenes(1000000)

lijstje = []
result = 0
n = 0
for i in numbers[4:]:
    count = 0
    for j in range(len(str(i))):
        numLeft = (str(i)[:-j])
        numRight = (str(i)[j:])
        lijstje.append(numLeft)
        lijstje.append(numRight)
    for item in lijstje:
        lengte = len(lijstje)
        if item != '':
            if int(item) in numbers:
                count += 1
                if count == lengte-1:
                    print("Succes bitches!",i)
                    result += i
                    n+=1
                    if n == 11:
                        print(result)
                        sys.exit()
            else:
                break
    lijstje.clear()