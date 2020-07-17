# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, (53)=10
# .
# In general, (nr)=n!r!(n−r)!
# , where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1
# .
# It is not until n=23
# # , that a value exceeds one-million: (2310)=1144066
# .
# How many, not necessarily distinct, values of (nr)
# for 1≤n≤100, are greater than one-million?

from math import factorial

# n = 16 * 15 * 14
# r = 3 * 2 * 1
# r = n//r
# print(r)

count=0
for i in range(1,101):
    for j in range(1,i):
        n = factorial(i)
        x = factorial(i-j)
        r = factorial(j)
        result = n//(r*x)
        if result > 999999:
            count+=1
print(count)