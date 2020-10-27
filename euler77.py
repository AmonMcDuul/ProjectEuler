# It is possible to write ten as the sum of primes in exactly five different ways:
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
# What is the first value which can be written as the sum of primes in over five thousand different ways?

import sys

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

def count_number_of_ways_to_sum(target_sum):
    if target_sum <= 1:
        raise ValueError('there are no numbers greater than 0 less than the target sum')
    # ith index contains the answer to the (i + 1)th subproblem
    num_ways_to_sum = [0] * (target_sum + 1)
    # There is only 1 way to sum to 1
    num_ways_to_sum[0] = 1
    # Consider sums involving numbers in [1, target_sum)
    for i in range(1, target_sum):
        if i in setOfPrimes:
        # Every subproblem j >= i depends on i
            for j in range(i, target_sum + 1):
                # The number of ways to sum j includes all the ways to sum i 
                # with all the ways to sum (j - i) appended (like the parenthesis)
                num_ways_to_sum[j] += num_ways_to_sum[j - i]
    return num_ways_to_sum[target_sum]

setOfPrimes = set()
for i in range(1,1000):
    if isPrime(i):
        setOfPrimes.add(i)

for i in range(2,100):
    if count_number_of_ways_to_sum(i) > 5000:
        print(i)
        sys.exit()

