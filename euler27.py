def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
        else:
            return True

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
 
boundary = 1000
count = 0
for b in sieveOfEratosthenes(boundary):
    for a in range(-b, 0, 2):      
        n = 1 
        while isPrime((n*n) + (a*n) + b) == True: 
            n += 1
            if n > count: 
                count = n
                result = a*b
print("Longest streak: ", count-1)               
print("coefficients a*b: ", result)