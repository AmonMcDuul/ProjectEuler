# Consider quadratic Diophantine equations of the form:
# x2 – Dy2 = 1
# For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
# It can be assumed that there are no solutions in positive integers when D is square.
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
# 32 – 2×22 = 1
# 22 – 3×12 = 1
# 92 – 5×42 = 1
# 52 – 6×22 = 1
# 82 – 7×32 = 1
# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

# pells equation

import math

def is_square(n):
    if n<1:
        return False
    else:
        for i in range(int(n/2)+1):
            if (i*i)==n:
                return True
        return False

def fun(a, b, c):
    t = a[0]
    a[0] = b[0]
    b[0] = b[0] * c + t
 
def solvePell(n, a, b):
    x = int(math.sqrt(n))
    y = x
    z = 1
    r = x << 1
    e1 = [1]
    e2 = [0]
    f1 = [0]
    f2 = [1]
    while True:
        y = r * z - y
        z = ((n - y * y) // z)
        r = (x + y) // z
        fun(e1, e2, r)
        fun(f1, f2, r)
        a[0] = f2[0]
        b[0] = e2[0]
        fun(b, a, x)
        if a[0] * a[0] - n * b[0] * b[0] == 1:
            return

numbers = []
x = [0]
y = [0]
for i in range(10,1000):
    if not is_square(i):
        solvePell(i, x, y)
        result = x[0], i
        numbers.append(result)
print(max(numbers))