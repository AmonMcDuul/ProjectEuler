# The Fibonacci sequence is defined by the recurrence relation:
#     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.
# Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

from utils import is_pandigital

def isPandigital(s):
    for c in "123456789":
        if not c in s:
            return False
    return True


loop = True
count = 1
a = 0
b = 1
first = 0
last = 0
while loop:
    c = a + b
    a = b
    b = c
    count+=1
    i = c
    if is_pandigital(str(i)[:9]): 
        if is_pandigital(str(i)[-9:]):
            print('Resultaat: ', count)
            loop = False
    if count % 100 == 0:
        print('tussenstandje: ', count, ' nog een hondertjah bitchaes')

