# The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. 
# Another example of a number with this property is 614656 = 284.
# We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.
# You are given that a2 = 512 and a10 = 614656.
# Find a30.

import sys

numbers = set()
for i in range(2,1000):
    for j in range(2,20):
        numbers.add(pow(i,j))

count = 0
i = 9
loop = True

for i in sorted(numbers):
    x = 0
    for item in str(i):
        x += int(item)
    for j in range(2,20):
        r = pow(x,j)
        if i == r:
            count+=1
            if count == 30:
                print('Result = ', i)
                sys.exit()
            if i < r:
                break
            