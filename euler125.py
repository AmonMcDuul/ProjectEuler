# The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.
# There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. 
# Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.
# Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.1

l = []
for i in range(1,10001):
    l.append(i**2)

s = set()

for i in l:
    r = 0
    for k in l:
        if k >= i:
            r += k
            if r != i:
                if r > 10**8:
                    break
                else:
                    if str(r) == str(r)[::-1]:
                        s.add(r)
print(sum(s))