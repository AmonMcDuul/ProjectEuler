# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

number = 0

for i in range(3,100000):
    s = str(i)
    result = 0
    for item in s:
        result += factorial(int(item))
        if result == int(s):
            number += result
    
print("Result is: ", number)