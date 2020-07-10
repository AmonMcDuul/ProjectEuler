# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import math
import functools 

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

def countdigits(N): 
    count = 0; 
    while (N): 
        count = count + 1; 
        N = int(math.floor(N / 10)); 
    return count; 
      
def cyclic(N): 
    num = N; 
    n = countdigits(N); 
    cyclicList = []
    while (1): 
        cyclicList.append(int(num))
          
        rem = num % 10; 
        div = math.floor(num / 10); 
        num = ((math.pow(10, n - 1)) * 
                           rem + div); 
        if (num == N): 
            break;
    return(cyclicList)  

count = 0
result = 0

numbers = sieveOfEratosthenes(1000000)

for i in numbers:
    count=0
    for item in cyclic(i):
        res = item
        n = len(cyclic(i))
        if int(res) in numbers:
            count+=1
        else:
            count =0
            break
        if count == n:
            result += 1
            break
print(result)