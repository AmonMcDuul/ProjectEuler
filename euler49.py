# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

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

numbers = sieveOfEratosthenes(10000)

result = 0

for r in numbers:
    if len(str(r)) == 4:
        i = 3330
        if len(str(r+i+i)) == 4:
            x = r+i+i 
            y = r+i
            z = r
            if x in numbers and y in numbers:
                s = sorted(str(x))
                d = sorted(str(y))
                f = sorted(str(z))
                if s == d and d == f:
                    result = str(r) + (str(r + i)) + (str(r + i +i))
                    print("Number is: ", result)