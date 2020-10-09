# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
# Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

# 10000000

def phi(n):    
    result = n
    p = 2
    while(p * p <= n):
        if (n % p == 0):              
            while (n % p == 0):
                n = int(n / p)
            result -= int(result / p)
        p += 1
    if (n > 1):
        result -= int(result / n)
    return result

result = 100

for i in range(2, 10000000):
    x = phi(i)
    if sorted(str(i)) == sorted(str(x)): 
        x = i/x 
        if x < result:
            result = x
            print("lowest: ", result, " from number: ", i)
