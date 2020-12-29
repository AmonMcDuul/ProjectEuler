# For a positive integer n, let f(n) be the sum of the squares of the digits (in base 10) of n, e.g.
# f(3) = 32 = 9,
# f(25) = 22 + 52 = 4 + 25 = 29,
# f(442) = 42 + 42 + 22 = 16 + 16 + 4 = 36
# Find the last nine digits of the sum of all n, 0 < n < 1020, such that f(n) is a perfect square.


from itertools import combinations

import math

l = set()
for i in range(1,10000):
    if i % 1000 == 0:
        print('tussenstand: ', i)
    A = []
    for j in str(i):
        if j != '0':
            A.append(int(j))
    A = sorted(A)
    r = ''
    for p in list(combinations(A, len(str(i)))):
        r = str(p) + r
    g = ''
    for q in p:
        g += str(q)
    l.add(g)
    A.clear()

print(sorted(l))
# def is_perfect_square(number: int) -> bool:
#     return pow(math.sqrt(number),2) == number

# values = [0]
# for i  in range(1,10):
#     values.append(pow(i,2))
# print(values)

# def annagram_square(n):
#     r = 0
#     for i in str(n):
#         r += values[int(i)]
#     if is_perfect_square(r):
#         return True
#     else:
#         return False

# x = 0
# sortedNumbers = []

# for i in range(1,10**20):
#     if sorted(str(i)) not in sortedNumbers:
#         sortedNumbers.append(sorted(str(i)))
#         if i % 1000000 == 0:
#             print('Tussenstand: ', i)
#         if annagram_square(i):
#             x += i % 1000000000

# print(x)
