# It is well known that if the square root of a natural number is not an integer, then it is irrational. 
# The decimal expansion of such square roots is infinite without any repeating pattern at all.
# The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

import math
from decimal import *

getcontext().prec = 102

result = 0

for i in range(1,101):
    x = Decimal(i).sqrt()
    if x % int(x) != 0:
        p = 0
        c = 0
        for i in str(x):
            if i != '.':
                c += 1
                result += int(i)
                if c == 100:
                    break
print(result)
