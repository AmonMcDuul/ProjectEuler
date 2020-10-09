# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 21 elements in this set.
# How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

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
for i in range(2, 1000001):
    result += phi(i)

print(result)


# bruteforce shitzle
# 
# from fractions import Fraction
# count = 0
# for i in range(1,1000000):
#     num = set()
#     if i < 500001:
#         num.add(i)
#     if i % 100 == 0:
#         print("status: ", i)
#     for j in range(1,1000000):
#         dum = set()
#         if j < 500001:
#             dum.add(j)
#         if i < j:
#             for n in num:
#                 for d in dum:
#                     if i % n == 0 and j % d == 0:
#                         break
#                 count+=1
# print(count)
