#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def sieveOfEratosthenes(n):
    result = 0
    prime = [True for i in range(n+1)]
    p = 2
    while (p*p <= n):
        if (prime[p] == True):
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    
    for p in range(2, n):
        if prime[p]:
            result += p
    
    print (result)

n = 2000000
sieveOfEratosthenes(n)