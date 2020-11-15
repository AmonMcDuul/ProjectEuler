# Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.
# For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.
# The least value of n for which the remainder first exceeds 109 is 7037.
# Find the least value of n for which the remainder first exceeds 1010.

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

numbers = sieveOfEratosthenes(10000000)
print('primes generated')

loop = True
i = 1
limit = pow(10,10)
while loop:
    i+=4
    if i % 1001 == 0:
        print('tussenstandje: ',i)
        print('      ', numbers[i], result, len(str(result)))
    result = (pow(numbers[i]-1,i) + pow(numbers[i]+1,i)) % pow(numbers[i],2)
    if result > limit:
        if (pow(numbers[i-2]-1,i) + pow(numbers[i-2]+1,i)) % pow(numbers[i-2],2) > limit:
            print('Result = ', result, i-2)
        else: 
            print('Result = ', result, i)
        loop = False