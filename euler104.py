# The Fibonacci sequence is defined by the recurrence relation:
#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.
# Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

import sys

def isPandigital(s):
    return set(s) == set('123456789')

loop = True
count = 1
a = 0
b = 1
while loop:
    c = a + b
    a = b
    b = c
    count+=1
    last = c % 1000000000
    if isPandigital(str(last)):
        first = str(c)[:9]
        if isPandigital(str(first)):
            print('Resultaat: ', count)
            loop = False
            sys.exit()
    if count % 1000 == 0:
        print('tussenstandje: ', count, ' nog een hondertjah bitchaes')
