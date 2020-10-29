# The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
# In fact, there are exactly four numbers below fifty that can be expressed in such a way:
# 28 = 22 + 23 + 24
# 33 = 32 + 23 + 24
# 49 = 52 + 23 + 24
# 47 = 22 + 33 + 24
# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

s = set()
for i in range(1,7200):
    if isPrime(i):
        for j in range(1,370):
            if isPrime(j):
                for x in range(1,85):
                    if isPrime(x):
                        n = (i**2+j**3+x**4)
                        if n < 50000001:
                            s.add(n)

print('Result: ', len(s))