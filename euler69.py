# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
# n 	Relatively Prime 	φ(n) 	n/φ(n)
# 2 	1 	1 	2
# 3 	1,2 	2 	1.5
# 4 	1,3 	2 	2
# 5 	1,2,3,4 	4 	1.25
# 6 	1,5 	2 	3
# 7 	1,2,3,4,5,6 	6 	1.1666...
# 8 	1,3,5,7 	4 	2
# 9 	1,2,4,5,7,8 	6 	1.5
# 10 	1,3,7,9 	4 	2.5

# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

# Hoe:
# 1) Initialize result as n
# 2) Consider every number 'p' (where 'p' varies from 2 to ?n). 
#    If p divides n, then do following
#    a) Subtract all multiples of p from 1 to n [all multiples of p
#       will have gcd more than 1 (at least p) with n]
#    b) Update n by repeatedly dividing it by p.
# 3) If the reduced n is more than 1, then remove all multiples
#    of n from result.

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

result = 0
for i in range(1,1000000):
    x = (i/phi(i))
    if x > result:
        result = x
        print("highest: ", result, " from number: ", i)
