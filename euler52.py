# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import sys

for i in range(10,1000000):
    count = 0
    for j in range(2,7):
        if sorted(str(i*j)) == sorted(str(i)):
            count+=1
            if count == 5:
                print(i)
                sys.exit()