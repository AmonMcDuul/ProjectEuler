import math
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if i in numbers:
            if n % i == 0:
                # yield i
                if i*i != n:
                    if n//i in numbers:
                        print('yeah')
                        
print(list(divisorGenerator(30)))