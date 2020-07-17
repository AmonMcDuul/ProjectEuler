# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# 2–√=1+12+12+12+…
# By expanding this for the first four iterations, we get:
# 1+12=32=1.5
# 1+12+12=75=1.4
# 1+12+12+12=1712=1.41666…
# 1+12+12+12+12=4129=1.41379…
# The next three expansions are 9970
# , 239169, and 577408, but the eighth expansion, 1393985
# , is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

# n/d
# 3/2
# 7/5
# 17/12
# 41/29
# 99/70
# d = n minus de vorige d
# n = n plus 2 * d

num = 3
den = 2
count = 0
for i in range(1,1001):
    num += 2 * den
    den = num - den
    if len(str(num)) > len(str(den)):
        count+=1

print(count)