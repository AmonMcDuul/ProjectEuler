import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                if n/2 < 1000000:
                    large_divisors.append(n / i)
                else: 
                    return 0
    for divisor in reversed(large_divisors):
        if divisor != n:
            yield int(divisor)

print(sum(list(divisorGenerator(2000000))))