# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

maxCount = 0
result = 0
for i in range(0,1000):
    count = 0
    num = 0
    for j in range(i,1000):
        num += numbers[j]
        count += 1
        if count > maxCount and num in numbers:
            maxCount = count
            print("New highest!", maxCount, "   ", num)
            result = num
        if num > 1000000:
            break
print("bigest number: ", result, " count: ", maxCount )