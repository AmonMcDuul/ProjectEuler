# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

from math import factorial

def factor(n):
    r = 0
    for j in str(n):
        r += factorial(int(j))
    return r

result = 0
for i in range (1,1000000):
    l = [1]
    r = factor(i)
    count = 0   
    q = 1
    q = max(l.count(k) for k in l)
    while q < 2 and count < 62:
        l.append(r)
        r = factor(r)
        q = max(l.count(k) for k in l)
        count+=1
    if count == 60:
        result +=1 
        print(i, count)
print('Resultaat: ', result)
