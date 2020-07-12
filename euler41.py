# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

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

numbers = sieveOfEratosthenes(9999999)

def isPandigital(nr, n):
    nr = str(nr)
    beg=set(nr[0:n])
    end=set(nr[-n:])
    return beg==end and beg==set(map(str, range(1, n + 1)))

for i in numbers:
    if isPandigital(i,len(str(i))):
        print (i)