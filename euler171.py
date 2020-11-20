# For a positive integer n, let f(n) be the sum of the squares of the digits (in base 10) of n, e.g.
# f(3) = 32 = 9,
# f(25) = 22 + 52 = 4 + 25 = 29,
# f(442) = 42 + 42 + 22 = 16 + 16 + 4 = 36
# Find the last nine digits of the sum of all n, 0 < n < 1020, such that f(n) is a perfect square.

import math
def is_perfect_square(number: int) -> bool:
    return pow(math.sqrt(number),2) == number

values = [0]
for i  in range(1,10):
    values.append(pow(i,2))
print(values)

result = 0
for i in range(1, pow(10,20)):
    if i % 1000000 == 0:
        print('tussenstand: ', i)
    res = 0
    for num in str(i):
        res += values[int(num)]
    if is_perfect_square(res):
        result += i
print(result)
