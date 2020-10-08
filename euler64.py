# All square roots are periodic when written as continued fractions and can be written in the form:
# n−−√=a0+1a1+1a2+1a3+1a4....

# For example, let us consider 2–√3:
# 2–√3=4+2–√3−4=4+112–√3−4=4+11+2–√3−37
# If we continue we would get the following expansion:
# 2–√3=4+11+13+11+18...
# The process can be summarised as follows:
# a0=4,12–√3−4=2–√3+47=1+2–√3−37
# a1=1,72–√3−3=7(2–√3+3)14=3+2–√3−32
# a2=3,22–√3−3=2(2–√3+3)14=1+2–√3−47
# a3=1,72–√3−4=7(2–√3+4)7=8+2–√3−4
# a4=8,12–√3−4=2–√3+47=1+2–√3−32
# a5=1,72–√3−3=7(2–√3+3)14=3+2–√3−32
# a6=3,22–√3−3=2(2–√3+3)14=1+2–√3−47
# a7=1,72–√3−4=7(2–√3+4)7=8+2–√3−4
# It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely. 
# The first ten continued fraction representations of (irrational) square roots are:
# 2–√ = [1;(2)], period=1
# 3–√ = [1;(1,2)], period=2
# 5–√ = [2;(4)], period=1
# 6–√ = [2;(2,4)], period=2
# 7–√ = [2;(1,1,1,4)], period=4
# 8–√ = [2;(1,4)], period=2
# 1–√0 = [3;(6)], period=1
# 1–√1 = [3;(3,6)], period=2
# 1–√2 = [3;(2,6)], period=2
# 1–√3 = [3;(1,1,1,1,6)], period=5

# Exactly four continued fractions, for N ≤ 13, have an odd period.
# How many continued fractions for N ≤ 10000 have an odd period? 
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#section6

import math

count = 0
for i in range(1,10001):
    number = int(math.sqrt(i))
    result = number
    m = 0
    d = 1 
    period = 0
    if result != math.sqrt(i):
        while number != 2*result:
            m = d*number - m
            d = (i - m**2)/d
            number = int((result + m)/d)
            period += 1
    if (period) % 2 != 0:
        count+=1
print(count)